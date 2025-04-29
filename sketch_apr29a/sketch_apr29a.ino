#define RELAY_PIN 7  // Connect relay IN pin to digital pin 7

void setup() {
  Serial.begin(9600);         // Initialize serial communication
  pinMode(RELAY_PIN, OUTPUT); // Set relay pin as output
  digitalWrite(RELAY_PIN, LOW); // Ensure relay is off on startup
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(RELAY_PIN, HIGH); // Turn ON the relay
    } else if (command == '0') {
      digitalWrite(RELAY_PIN, LOW);  // Turn OFF the relay
    }
  }
}
