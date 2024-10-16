#include "Arduino.h"
#include "serial_handler.h"
#include "utils.h"

// #define LED_BUILTIN 2
#define DEBUG
#define SIGNAL_LEN  100
#define CHANNEL_N   4

char receivedChars[MAX_CHARS];
boolean newData = false;
bool blink = false;
double m_signal[SIGNAL_LEN];  
enum channels {CH1 = 1, CH2, CH3, CH4};
bool channel_en[CHANNEL_N] = {1, 1, 1, 1};
typedef struct ch_range {
    double min;
    double max;
} ch_range;
ch_range channel_range[CHANNEL_N] = {{.min=0.1, .max=2.6}, {.min=0, .max=0}, {.min=1, .max=12}, {.min=0, .max=0}};

using namespace std;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  	Serial.begin(BAUD_RATE);    // open serial port
    int i;
    for(i = 0; i < SIGNAL_LEN; i++){    // generate signal
	    m_signal[i] = i;
    }
}

void send_signal(){
    String msg = "MS-[";
    int ch;
    for (ch = 0; ch < CHANNEL_N; ch++){
        if (channel_en[ch]){
            if (ch != 0){
                msg = msg + ",";
            }
            msg = msg + "{\"channel\":" + String(ch+1) + ",";
            msg = msg + "\"range\":[" + String(channel_range[ch].min) + "," + String(channel_range[ch].max) + "],";
            msg = msg + "\"signal\":[" + array2String(m_signal, SIGNAL_LEN);
            msg = msg + "]}";
        }
    }
    msg = msg + "]-\n";
    Serial.print(msg);
}

void loop()
{
    newData = recvWithStartEndMarkers(&receivedChars[0], &newData);
    if (newData || blink) {
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
            send_signal();
        } else if (receivedChars[0] == 'T'){
            Serial.print("Test");
        } else if (receivedChars[0] == 'R'){
            Serial.print("Run");
        } else if (receivedChars[0] == 'S'){
            Serial.print("Stop");
        } else if (receivedChars[0] == 'S1'){
            Serial.print("Single");
        } else if (receivedChars[0] == 'R'){
            Serial.print("Run");
        }


		newData = false;

    }
}