#include <RCSwitch.h>

// Pin Definitions
#define LED_PIN 13  // LED pin for visual feedback

// Number of times to resend sniffed value. Can be adjusted dynamically.
int resendSniffedValues = 10;

// RF switch classes for 315 MHz and 434 MHz
RCSwitch rf315Switch = RCSwitch();
RCSwitch rf434Switch = RCSwitch();

// Function to convert decimal values to binary (32 bits)
char* toBinary(unsigned long value) {
    static char binary[33];  // Static to preserve value between calls
    binary[32] = '\0';  // Null-terminate the string

    for (int i = 0; i < 32; i++) {
        binary[31 - i] = (value >> i) & 0x1 ? '1' : '0';
    }
    return binary;
}

// Function to process RF values from a given switch (315 or 434 MHz)
void processRFValue(RCSwitch& rfSwitch, int rfFrequency) {
    char outputMessage[120];
    unsigned long receivedValue = rfSwitch.getReceivedValue();

    digitalWrite(LED_PIN, HIGH);  // Turn on LED for transmission feedback

    // Check if a value was received
    if (receivedValue) {
        sprintf(outputMessage, "[+] %d MHz Received: %s / %010lu / %d bit / Protocol = %d",
                rfFrequency, toBinary(receivedValue), receivedValue, rfSwitch.getReceivedBitlength(), rfSwitch.getReceivedProtocol());
        // Resend the captured value the specified number of times
        rfSwitch.send(receivedValue, rfSwitch.getReceivedBitlength());
    } else {
        sprintf(outputMessage, "[-] %d MHz Received: Unknown encoding (0)", rfFrequency);
    }
    Serial.println(outputMessage);

    // Reset switch to allow new data to be received
    rfSwitch.resetAvailable();
    digitalWrite(LED_PIN, LOW);  // Turn off LED after processing
}

void setup() {
    // Set LED as output
    pinMode(LED_PIN, OUTPUT);

    // Initialize serial communication for debugging
    Serial.begin(115200);

    // Initialize 315 MHz receiver (interrupt 0, pin 2) and transmitter (pin 4)
    rf315Switch.enableReceive(0);
    rf315Switch.enableTransmit(4);
    rf315Switch.setRepeatTransmit(resendSniffedValues);

    // Initialize 434 MHz receiver (interrupt 1, pin 3) and transmitter (pin 5)
    rf434Switch.enableReceive(1);
    rf434Switch.enableTransmit(5);
    rf434Switch.setRepeatTransmit(resendSniffedValues);

    Serial.println("[+] Ready to capture RF signals on 315 and 434 MHz.");
}

void loop() {
    // Check if a signal is available on 315 MHz
    if (rf315Switch.available()) {
        processRFValue(rf315Switch, 315);
    }

    // Check if a signal is available on 434 MHz
    if (rf434Switch.available()) {
        processRFValue(rf434Switch, 434);
    }
}
