#include <Arduino.h>

// Forward declaration of the ISR function
void IRAM_ATTR onTimer();

unsigned int buffer1[100];
unsigned int buffer2[100];
bool bufferFlag = false;
bool sendFlag = false;

int level = 0;  // value output to the LED

hw_timer_t *timer = NULL;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;

void setup() {
  // Initialize serial communications at 115200 bps:
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

  // Set up timer
  timer = timerBegin(100);
  timerAttachInterrupt(timer, &onTimer);
  timerAlarm(timer, 5000, true, 0);  // 5000 ticks = 5ms (assuming 80MHz clock)
}

void IRAM_ATTR onTimer() {
  static unsigned long counter = 0;
  static unsigned int pos = 0;

  counter++;

  // Every 500 ms
  if (counter % 100 == 0) {
    // Blink LED
    level = level ^ 1;
    digitalWrite(LED_BUILTIN, level);
  }

  // Every 5 ms
  if (counter % 1 == 0) {
    // Send the value of analog input 0:
    buffer1[pos++] = analogRead(34);  // ADC1_CH6, GPIO34
  }

  if (pos == 100) {
    for (unsigned int i = 0; i < 100; i++) {
      buffer2[i] = buffer1[i];
    }

    bufferFlag = true;
    pos = 0;
  }
}

void loop() {
  if (Serial.available() > 0) {
    sendFlag = true;
  }

  if (bufferFlag && sendFlag) {
    char data = Serial.read();
    if (data == 's') {
      for (unsigned int i = 0; i < 100; i++) {
        int high = buffer2[i] / 256;
        int low = buffer2[i] % 256;
        Serial.write(high);
        Serial.write(low);
      }
      bufferFlag = false;
      sendFlag = false;
    }
  }
}
