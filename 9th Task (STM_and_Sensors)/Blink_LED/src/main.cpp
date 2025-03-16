#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the built-in LED pin as an output
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED on
  delay(1000);                      // Wait for 1 second
  digitalWrite(LED_BUILTIN, LOW);   // Turn the LED off
  delay(1000);                      // Wait for 1 second
}
