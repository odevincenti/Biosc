// serial_handler.h

#ifndef SERIAL_H  // Directiva del preprocesador para evitar inclusiones múltiples
#define SERIAL_H

#include <Arduino.h>

#define MAX_CHARS	32
#define BAUD_RATE	9600

// Declaración de funciones o clases

boolean recvWithStartEndMarkers(char* receivedChars, boolean* newData);

#endif  // SERIAL_H
