#include "Arduino.h"
#include "serial_handler.h"
#include "utils.h"
#include "adc.h"

// #define LED_BUILTIN 2
#define DEBUG
#define SIGNAL_LEN  100
#define CHANNEL_N   2//4

char receivedChars[MAX_CHARS];
boolean newData = false;
bool blink = false;
bool running = false;
long m_signal[SIGNAL_LEN];  
enum channels {CH1 = 1, CH2};//, CH3, CH4};
bool channel_en[CHANNEL_N] = {1, 1};//, 1, 1};
typedef struct ch_range {
    double min;
    double max;
} ch_range;
ch_range channel_range[CHANNEL_N] = {{.min=0.1, .max=2.6}, {.min=1, .max=12}};//, {.min=0, .max=0},{.min=0, .max=0}, };

hw_timer_t * sample_timer = NULL;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;
 
// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 
#define POT_PIN 34
// int i= 0;
int ix = 0;
bool start = 1;

void IRAM_ATTR onTimer() {
    // digitalWrite(LED_BUILTIN, LOW);
    portENTER_CRITICAL_ISR(&timerMux);
    digitalWrite(LED_BUILTIN, HIGH);
    m_signal[ix] = getVoltageValue(POT_PIN, 2);
    ix++;
    if (ix >= SIGNAL_LEN){
        ix = 0;
        start = 0;
    }
    digitalWrite(LED_BUILTIN, LOW);
    // digitalWrite(LED_BUILTIN, HIGH);
    portEXIT_CRITICAL_ISR(&timerMux);
    // digitalWrite(LED_BUILTIN, LOW);
}

using namespace std;

void setup()
{
    init_Adc();
    pinMode(LED_BUILTIN, OUTPUT);
  	Serial.begin(BAUD_RATE);    // open serial port
    sample_timer = timerBegin(0, 80, true);
    timerAttachInterrupt(sample_timer, &onTimer, true);
    timerAlarmWrite(sample_timer, 200, true);
    timerAlarmEnable(sample_timer);
}

void send_signal(int ix, bool start){

    int signal2send[SIGNAL_LEN];
    int i = 0;
    if (start){
        for (i = 0; i < ix; i++){
            signal2send[i] = m_signal[i];
        }
        for (i; i < SIGNAL_LEN; i++){
            signal2send[i] = 0;
        }
    } else {
        for (i = ix; i < SIGNAL_LEN; i++){
            signal2send[i] = m_signal[i];
        }
        for (i = 0; i < ix; i++){
            signal2send[i] = m_signal[i];
        }
    }

    String msg = "MS-[";
    int ch;
    for (ch = 0; ch < CHANNEL_N; ch++){
        if (channel_en[ch]){
            if (ch != 0){
                msg = msg + ",";
            }
            msg = msg + "{\"channel\":" + String(ch+1) + ",";
            msg = msg + "\"range\":[" + String(channel_range[ch].min) + "," + String(channel_range[ch].max) + "],";
            msg = msg + "\"signal\":[" + array2String(signal2send, SIGNAL_LEN);
            msg = msg + "]}";
        }
    }
    msg = msg + "]-\n";
    Serial.print(msg);
}

void loop()
{
    newData = recvWithStartEndMarkers(&receivedChars[0], &newData);
    if (newData || blink || running) {
#ifdef DEBUG
		Serial.println(receivedChars);
#endif
        if (receivedChars[0] == 'H'){
            blink = false;
            digitalWrite(LED_BUILTIN, HIGH);
        } else if (receivedChars[0] == 'L'){
            blink = false;
            digitalWrite(LED_BUILTIN, LOW);
        } else if (blink || receivedChars[0] == 'B'){
            blink = true;
            digitalWrite(LED_BUILTIN, HIGH);
            delay(1000);
            digitalWrite(LED_BUILTIN, LOW);
            delay(1000);
        } else if (receivedChars[0] == 'M' && receivedChars[1] == 'S'){
            blink = false;
            // Serial.println("Sending Signal");
            send_signal(ix, start);
        } else if (receivedChars[0] == 'T'){
            Serial.print("Test\n");
        } else if (receivedChars[0] == 'R'){
            // Serial.print("Run\n");
            running = true;
        // } else if (receivedChars[0] == 'S' && receivedChars[1] == '1'){
        //     Serial.print("Single\n");
        } else if (receivedChars[0] == 'S'){
            running = false;
            // Serial.print("Stop\n");
        }

		newData = false;

    }

    if (running && !start){
        send_signal(ix, start);
    }

}