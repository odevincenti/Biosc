hw_timer_t *timer = NULL;
volatile SemaphoreHandle_t timerSemaphore;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;

int level = 1;
int waveValue = 0;
bool increasing = true;


void ARDUINO_ISR_ATTR onTimer() {
  xSemaphoreGiveFromISR(timerSemaphore, NULL);
}

void setup() {
  Serial.begin(115200);

  // Set BTN_STOP_ALARM to input mode
  pinMode(LED_BUILTIN, OUTPUT);

  // Create semaphore to inform us when the timer has fired
  timerSemaphore = xSemaphoreCreateBinary();

  // Set timer frequency to 1Mhz
  timer = timerBegin(1000000);

  // Attach onTimer function to our timer.
  timerAttachInterrupt(timer, &onTimer);

  // Set alarm to call onTimer function every second (value in microseconds).
  // Repeat the alarm (third parameter) with unlimited count = 0 (fourth parameter).
  timerAlarm(timer, 1000, true, 0);
}

void loop() {
  // If Timer has fired
  if (xSemaphoreTake(timerSemaphore, 0) == pdTRUE) {
    
    digitalWrite(LED_BUILTIN, level);
      if (increasing) {
        waveValue++;
    if (waveValue >= 256) {
      increasing = false;
      level = !level;
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
}

