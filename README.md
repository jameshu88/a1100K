# a1100k - Flipper Zero Integration

## Overview

**a1100k** is an ethical On-Off Keying (OOK) hacking tool designed to brute-force garage door frequencies using de Bruijn's algorithm. This tool leverages the capabilities of the [Flipper Zero](https://flipperzero.one/) device to generate and transmit unique OOK signal sequences, ensuring comprehensive coverage of all possible frequency combinations within a 12-bit range (4096 possibilities).

## What is de Bruijn's Algorithm?
A de Bruijn sequence for a given alphabet size and subsequence length is a cyclic sequence in which every possible 
subsequence of a specified length appears exactly once. In the context of OOK signal generation, de Bruijn's 
algorithm ensures that all possible frequency combinations are efficiently tested with minimal redundancy.

## Why Use de Bruijn's Algorithm?
- **Efficiency**: Generates all possible combinations without repetition, reducing the number of required signals.
- **Comprehensive Testing**: Ensures every possible frequency combination is covered, increasing the likelihood of successfully 
  brute-forcing the target system.
- **Optimized Performance**: Minimizes the time and resources needed for exhaustive testing by leveraging the mathematical 
  properties of de Bruijn sequences.


Older garage door systems often use dip switches to set unique frequency codes. Each dip switch represents a binary value, allowing for a wide range of combinations. By using de Bruijn's algorithm, the xA1100k tool can efficiently generate OOK signal sequences that cover all possible dip switch configurations without unnecessary repetition. This comprehensive approach ensures that every potential dip switch setting is tested, increasing the chances of successfully brute-forcing the garage door frequency!

## Features

- **De Bruijn Sequence Generation**: Efficiently generates all possible 12-bit OOK signal combinations without redundancy.
- **Flipper Zero Compatibility**: Produces `.sub` files compatible with Flipper Zero's Sub-GHz module.
- **Parameter Tweaking**: Allows users to adjust signal durations and frequencies to optimize brute-forcing attempts.
- **Automated File Splitting**: Organizes generated signals into manageable `.sub` files, each containing a specified number of keys.

## Prerequisites

Before setting up the project, ensure you have the following:

- **Flipper Zero Device**: [Purchase here](https://flipperzero.one/)
- **Python 3.x**: Ensure Python is installed on your system. Download from [python.org](https://www.python.org/downloads/).
- **Flipper Zero Firmware**: Make sure your Flipper Zero is updated to the latest firmware version.
- **USB Cable**: For transferring files to Flipper Zero.

## Installation

To set up the xA1100k tool for Flipper Zero, follow these steps:

1. **Clone the Repository**

   Open your terminal or command prompt and navigate to your desired directory. Clone the repository using Git:

   ```bash
   git clone https://github.com/yourusername/xA1100k.git
   ```

2. **Navigate to the Flipper Zero Directory**

    Change your working directory to the flipper_zero folder within the cloned repository:

    ```bash
    cd xA1100k/flipper_zero
    ```

## Usage

**Generating .sub files** 

The core functionality is provided by the de_brujin_generator.py script, which generates .sub files containing the OOK signal sequences.

1. **Run The Script**

   Execute the Python script to generate the .sub files:

   ```bash
   python de_brujin_generator.py
   ``````

   This will create .sub files in the flipper_zero directory, each containing up to 1000 keys by default.

2. **Script Configuration**

    The script contains configurable parameters at the top. You can adjust these settings to fit your specific needs:

    ```python
    # Configurable parameters
    SPLIT = 1000  # Number of keys per file before splitting
    FREQUENCY = 433920000  # Frequency in Hz
    PRESET = "FuriHalSubGhzPresetOok650Async"  # SubGHz preset
    PROTOCOL = "RAW"
    REPETITIONS = 5  # Number of signal repetitions
    PADDING = "-50000 50000"  # Padding between signals
   ```

    - **SPLIT**: Adjust the number of keys per .sub file.
    - **FREQUENCY**: Set the target frequency for brute-forcing.
    - **PRESET & PROTOCOL**: Define the signal preset and protocol used by Flipper Zero.
    - **REPETITIONS**: Number of times each signal pattern is repeated.
    - **PADDING**: Defines the padding between signals to ensure proper separation.

## Usage

After generating the .sub files, follow these steps to upload them to your Flipper Zero device:

1.  **Connect Flipper Zero to Your Computer**

  Use a USB cable to connect your Flipper Zero device to your computer.

2.  **Access the Flipper Zero Storage**

  Once connected, Flipper Zero should appear as a removable storage device on your computer.

3.  **Navigate to the Sub-GHz Directory**

  Open the Flipper Zero storage and navigate to the subGHz folder. The drive letter may vary based on your system (e.g., F:\subGHz\).

4.  **Copy the .sub Files**

  Transfer the generated .sub files from the flipper_zero directory to the subGHz folder on Flipper Zero.

5.  **Safely Disconnect**

Eject the Flipper Zero device to ensure all files are properly written before disconnecting.

Hap

## Customization
**Parameter Tweaking with Sliding Window**

To optimize the brute-forcing process, you can implement a sliding window approach to dynamically adjust signal parameters based on specific criteria or feedback. While this script provides a foundational setup, further enhancements can include:

- **Dynamic Adjustment**: Automatically tweak signal durations based on success rates or specific target responses.
- **Frequency Variations**: Explore a broader range of frequencies by adjusting the FREQUENCY parameter.
- **Repetition Control**: Modify the REPETITIONS parameter to balance between speed and signal reliability.
    Example: Adjusting Pulse Durations
    To modify the pulse durations, update the mapping dictionary in the generate_command function:
