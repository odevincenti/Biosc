#include <math.h>
#define BUFFER_SIZE 100

hw_timer_t *timer = NULL;
volatile SemaphoreHandle_t timerSemaphore;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;
volatile uint32_t isrCounter = 0;
volatile uint32_t lastIsrAt = 0;

int level = 1;
int waveValue = 0;
bool increasing = true;

unsigned int buffer_read[BUFFER_SIZE];
unsigned int buffer_send[BUFFER_SIZE];
unsigned int sample_rate = 1e6;

bool bufferFlag = false;
bool sendFlag = false;
static unsigned int pos = 0;

void ARDUINO_ISR_ATTR onTimer() {
  // Increment the counter and set the time of ISR
  portENTER_CRITICAL_ISR(&timerMux);
  isrCounter = isrCounter + 1;
  lastIsrAt = millis();
  portEXIT_CRITICAL_ISR(&timerMux);
  xSemaphoreGiveFromISR(timerSemaphore, NULL);
}

void setup() {
  Serial.begin(115200);

  // Set BTN_STOP_ALARM to input mode
  pinMode(LED_BUILTIN, OUTPUT);

  // Create semaphore to inform us when the timer has fired
  timerSemaphore = xSemaphoreCreateBinary();

  // Set timer frequency to 1Mhz
  timer = timerBegin(sample_rate);

  // Attach onTimer function to our timer.
  timerAttachInterrupt(timer, &onTimer);

  // Set alarm to call onTimer function every second (value in microseconds).
  // Repeat the alarm (third parameter) with unlimited count = 0 (fourth parameter).
  timerAlarm(timer, 1000, true, 0);
}

void loop() {
  // If Timer has fired (this is basically the content of the onTimer call)
  if (xSemaphoreTake(timerSemaphore, 0) == pdTRUE) {
    // Every 500 ms, blink led
    if (lastIsrAt % 500 == 0){
      level = !level;
      digitalWrite(LED_BUILTIN, level);
    }

    // Update wave value
    if (increasing) {
      waveValue++;
      if (waveValue >= 255) {
        increasing = false;
      }
    } 
    else {
      waveValue--;
      if (waveValue <= 0) {
        increasing = true;
      }
    }

    // Write to buffer
    buffer_read[pos] = waveValue;
    pos++;
    if (pos == BUFFER_SIZE){
      for (unsigned int i = 0; i < BUFFER_SIZE; i++){
        buffer_send[i] = buffer_read[i];
      }
      bufferFlag = true;
      pos = 0;
    }

  // Write to serial
    if (Serial.available() > 0){
        sendFlag = true;
      }

    if (bufferFlag && sendFlag){
      char data = Serial.read();
      if (data == 's'){ 
        for (unsigned int i = 0; i < BUFFER_SIZE; i++){
          Serial.write(buffer_send[i]);
        }
        bufferFlag = false;
        sendFlag = false;
      }
    }
  }
}

