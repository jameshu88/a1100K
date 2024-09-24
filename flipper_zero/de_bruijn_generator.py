import os

# Configurable parameters
SPLIT = 1000  # Number of keys per file before splitting
BASE_FREQUENCY = 433920000  # Base frequency in Hz
PRESET = "FuriHalSubGhzPresetOok650Async"  # SubGHz preset
PROTOCOL = "RAW"
CASE = 0  # Initialize file case counter
REPETITIONS = 5  # Number of signal repetitions
PADDING = "-50000 50000"  # Padding between signals

# Sliding window parameters for pulse durations (in microseconds)
LOW_DURATION_RANGE = range(300, 400, 10)  # e.g., 300 to 390 with step 10
HIGH_DURATION_RANGE = range(600, 700, 10)  # e.g., 600 to 690 with step 10

def generate_command(binary, low_duration, high_duration):
    """
    Generates a sequence command based on the binary representation with 
    dynamic durations.
    
    Parameters:
    - binary (str): A 12-bit binary string representing the current key.
    - low_duration (int): Duration (in microseconds) for low signal.
    - high_duration (int): Duration (in microseconds) for high signal.
    
    Returns:
    - str: A concatenated string of OOK signal durations.
    """
    # Mapping binary digits to OOK signal durations with dynamic parameters
    mapping = {

        '0': f'-{low_duration} {high_duration} ',
        # Example adjustment
        '1': f'-{low_duration * 2} {high_duration - 300} '
    }
    return ''.join([mapping[char] for char in binary])

def write_header(filecase, frequency):
    """
    Writes the header for the .sub file with dynamic frequency.
    
    Parameters:
    - filecase (str): The filename for the current .sub file.
    - frequency (int): Frequency in Hz.
    """
    with open(filecase, 'w') as f:
        f.write("Filetype: Flipper SubGhz RAW File\n")
        f.write("Version: 1\n")
        f.write(f"Frequency: {frequency}\n")
        f.write(f"Preset: {PRESET}\n")
        f.write(f"Protocol: {PROTOCOL}\n")

def append_command(command, filecase):
    """
    Appends the command and padding to the existing file.
    
    Parameters:
    - command (str): The RAW_Data command string.
    - filecase (str): The filename for the current .sub file.
    """
    with open(filecase, 'a') as f:
        f.write(f"RAW_Data: {command}\n")
        f.write(f"RAW_Data: {PADDING}\n")

def parameter_sweep():
    """
    Generates .sub files by sweeping through defined parameter ranges using a 
    sliding window approach.
    """
    global CASE
    for low in LOW_DURATION_RANGE:
        for high in HIGH_DURATION_RANGE:
            # Adjust frequency if needed, for simplicity we keep it constant
            frequency = BASE_FREQUENCY  
            # Iterate through all possible 12-bit values
            for x in range(4096):
                binary = f"{x:012b}"  # Convert to 12-bit binary
                # Generate command with repetitions
                command = generate_command(binary, low, high) * REPETITIONS 
                # Handle file splitting
                if x % SPLIT == 0:
                    CASE += 1
                    filecase = f'output_freq{frequency}_low{low}_high{high}_case{CASE}.sub'
                    write_header(filecase, frequency)
                # Append to file
                append_command(command, filecase)

if __name__ == "__main__":
    parameter_sweep()
