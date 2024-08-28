#include <Arduino.h>

void init_Adc(void);
long getVoltageValue(int adcPin, int avg_samples);
int mapADCValue(int value, int *ADCArr, int *VoltageArr, int arrSize);
