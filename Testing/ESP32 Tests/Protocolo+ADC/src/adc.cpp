#include "adc.h"

int mapADCValue(int value, int *ADCArr, int *VoltageArr, int arrSize);

// VARIABLES
int VoltageArr[] = {0,106,215,308,393,507,593,712,807,886,982,1099,1197,1301,1397,1496,1593,1704,1789,1902,2004,2095,2203,2306,2400,2503,2597,2700,2807,2897,2991,3094,3200,3283};
int ADCArr[] = {0,36,132,235,340,485,600,740,856,957,1080,1226,1345,1478,1606,1725,1845,1986,2100,2230,2355,2472,2610,2735,2860,3000,3125,3280,3450,3617,3810,4010,4090,4095};
int arrSize = 0;  

long voltage = 0;
int SampleCounter = 0;
long rawValues = 0;

void init_Adc(void){
  arrSize = sizeof(ADCArr) / sizeof(ADCArr[0]);
}

long getVoltageValue(int adcPin, int avg_samples){
  rawValues = rawValues + (long)analogRead(adcPin);
#ifdef AVG_SAMPLING
  SampleCounter = SampleCounter + 1;
  if(SampleCounter >= avg_samples){
    SampleCounter = 0;
    rawValues = rawValues / avg_samples;
    voltage = mapADCValue(rawValues, ADCArr, VoltageArr, arrSize);
    rawValues = 0;
  }
#else
  voltage = mapADCValue(rawValues, ADCArr, VoltageArr, arrSize);
  rawValues = 0;
#endif

  return voltage;
}

int mapADCValue(int value, int *ADCArr, int *VoltageArr, int arrSize) {
    
    // Find the two closest values in ADCArr
    int i;
    for (i = 0; i < arrSize - 1; i++) {
        if (value >= ADCArr[i] && value <= ADCArr[i + 1]) {
            break;
        }
    }

    // Calculate interpolated value in VoltageArr
    int x0 = ADCArr[i];
    int x1 = ADCArr[i + 1];
    int y0 = VoltageArr[i];
    int y1 = VoltageArr[i + 1];

    // Linear interpolation
    return y0 + (value - x0) * (y1 - y0) / (x1 - x0);
}
