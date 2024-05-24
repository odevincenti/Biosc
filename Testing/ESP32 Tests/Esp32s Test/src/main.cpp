#include "Arduino.h"
#include "serial_handler.h"

// #define LED_BUILTIN 2
#define DEBUG

char receivedChars[MAX_CHARS];
boolean newData = false;
bool blink = false;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  	Serial.begin(BAUD_RATE);    // open serial port
	Serial.write("Ready!\n");	
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
        }

		newData = false;

    }
}