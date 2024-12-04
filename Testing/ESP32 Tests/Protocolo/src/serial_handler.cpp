#include <Arduino.h>
#include "serial_handler.h"

boolean recvWithStartEndMarkers(char* receivedChars, boolean* newData) {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && *newData == false) {
        rc = Serial.read();
#ifdef DEBUG
		Serial.print(rc);
#endif

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= MAX_CHARS) {
					Serial.write("Error: Maximum char count exceeded");
					recvInProgress = false;
					ndx = 0;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                *newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }

	return *newData;

}


