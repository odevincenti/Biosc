#include "Arduino.h"
#include "serial_handler.h"

// #define LED_BUILTIN 2
#define DEBUG
#define SIGNAL_LEN  100
#define CHANNEL_N   4

char receivedChars[MAX_CHARS];
boolean newData = false;
bool blink = false;
double m_signal[SIGNAL_LEN];  
enum channels {CH1 = 1, CH2, CH3, CH4};
bool channel_en[CHANNEL_N] = {1, 0, 0, 0};
typedef struct ch_range {
    double min;
    double max;
} ch_range;
ch_range channel_range[CHANNEL_N] = {{.min=0.1, .max=2.6}, {.min=0, .max=0}, {.min=0, .max=0}, {.min=0, .max=0}};

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
            msg = msg + "{\"channel\":" + String(ch) + ",";
            msg = msg + "\"range\":[" + String(channel_range[ch].min) + "," + String(channel_range[ch].max) + "],";
            msg = msg + "\"signal\":[" + String(m_signal[0]);
            int i;
            for (i = 1; i < SIGNAL_LEN; i++){
                msg = msg + "," + String(m_signal[i]);
            }
            msg = msg + "]}";
        }
    }
    msg = msg + "]-\0";
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
        }

		newData = false;

    }
}