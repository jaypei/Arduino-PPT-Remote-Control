#include <IRremote.h>
int RECEIVE_PIN = 2;
IRrecv irrecv(RECEIVE_PIN);
decode_results results;

void setup() {
    Serial.begin(9600);
    irrecv.enableIRIn(); // Start the receiver
}

void loop() {
    if (irrecv.decode(&results)) {
        Serial.print("0x");
        Serial.print(results.value, HEX);
        Serial.print("\n");
        delay(50);
        irrecv.resume();// Receive the next value
    }
}
