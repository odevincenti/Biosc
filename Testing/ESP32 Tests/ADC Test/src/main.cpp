#include <Arduino.h>
#include "adc.h"

// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 
const int potPin = 34;

// variable for storing the potentiometer value
long potValue = 0;

void setup() {
    init_Adc();
    Serial.begin(115200);
    delay(1000);
}

void loop() {
  // Reading potentiometer value
  potValue = getVoltageValue(potPin, 2);
  Serial.println(potValue);
  delay(500);
}