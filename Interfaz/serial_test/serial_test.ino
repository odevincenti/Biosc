#include <Arduino.h>

const int adcPin = 34;  // ADC1_CH6, GPIO34

void setup() {
  Serial.begin(115200);
  delay(1000);  // Allow time for the serial connection to initialize
}

void loop() {
  int adcValue = analogRead(adcPin);
  Serial.println(adcValue);
  delay(50);  // Adjust the delay as needed
}
