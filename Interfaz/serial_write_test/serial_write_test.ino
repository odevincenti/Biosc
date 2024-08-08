#include <Arduino.h>

int waveValue = 0;
bool increasing = true;
int level = 0;


void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {
  delay(10);
  if (increasing) {
    waveValue++;
    if (waveValue >= 256) {
      increasing = false;
      level = level^1;
      digitalWrite(LED_BUILTIN, level);
    }
  } 
  else {
    waveValue--;
    if (waveValue <= 0) {
      increasing = true;
    }
  }
  Serial.println(waveValue);
}
