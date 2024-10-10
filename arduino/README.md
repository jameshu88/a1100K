# Arduino RF Sniffer and De Bruijn Sequence Generator - all00k

This project combines an RF sniffer for capturing and replaying signals from common RF devices (like gates, cars, and remote-controlled devices) with a De Bruijn sequence generator. The generator is useful for brute-forcing OOK-based RF systems by covering all possible binary combinations of a specified bit length.

## Features

- **RF Sniffer**: Captures and replays RF signals at both 315 MHz and 434 MHz.
- **Resend Sniffed Signals**: Automatically resends captured RF signals multiple times.
- **Binary Conversion**: Converts captured signal values to binary for easy reading and analysis.
- **De Bruijn Sequence Generator**: Generates all possible binary sequences to brute-force RF systems.
- **LED Feedback**: Provides visual feedback during signal capture and transmission.

## Components

- **Arduino (Uno or similar)**
- **315 MHz and 434 MHz RF Receiver and Transmitter Modules**
- **LED (optional for feedback)**

## Pin Connections

- **315 MHz Receiver**: Pin 2 (Interrupt 0)
- **315 MHz Transmitter**: Pin 4
- **434 MHz Receiver**: Pin 3 (Interrupt 1)
- **434 MHz Transmitter**: Pin 5
- **LED**: Pin 13 (optional)

## Installation

1. Install the **RCSwitch** library in your Arduino IDE.
2. Connect the RF receiver and transmitter modules to your Arduino following the pin connections above.
3. Upload the code to your Arduino.

## How It Works

### RF Sniffer

- The Arduino listens for signals on both the 315 MHz and 434 MHz frequencies.
- When a signal is detected:
  - The signal is captured and printed to the Serial Monitor.
  - The captured signal is retransmitted a specified number of times (default: 10).
  - The binary representation of the signal is printed for analysis.

### De Bruijn Sequence Generator

The De Bruijn sequence generator transmits all possible sequences of binary values (Gray code) for a given bit length. This is particularly useful for brute-forcing systems like remote controls and gates that use OOK-based RF signals.

- **De Bruijn Sequence**: A sequence that contains every possible binary combination for a given number of bits.
- The De Bruijn sequence is used to ensure every possible code is tested, without unnecessary repetitions.

To adjust the sequence length, change the `SEQUENCE_LENGTH` variable in the code. By default, it is set to 4 bits, which generates 16 possible combinations.

    ```
    cpp
    #define SEQUENCE_LENGTH 4  // Number of bits for the De Bruijn sequence
    ```
