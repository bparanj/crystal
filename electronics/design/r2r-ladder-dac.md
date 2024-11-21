### R/2R Ladder DAC (I-Output)

An R/2R Ladder DAC is a digital-to-analog converter (DAC) that uses a resistor network to convert a digital binary input into an equivalent current or voltage output. In the current output (I-Output) configuration, the circuit produces a current proportional to the binary input.

### Concepts

1. R/2R Resistor Network:
   - The network consists of resistors arranged in a repeating pattern of \( R \) and \( 2R \), simplifying implementation.
   - Binary-weighted current division is achieved, allowing precise digital-to-analog conversion.

2. Digital Input:
   - Each digital bit controls a switch, connecting it either to a reference voltage (\( V_{ref} \)) or ground.

3. Output Current:
   - The output current (\( I_{out} \)) is proportional to the binary input:
     \[
     I_{out} = \frac{V_{ref}}{R} \cdot \frac{\text{Digital Input}}{2^n}
     \]
     Where \( n \) is the number of bits in the input.

4. Applications:
   - Digital-to-analog conversion for audio, control systems, and waveform generation.

### Experiment

#### Objective

To design and simulate an R/2R Ladder DAC with current output and observe the relationship between digital input and output current.

#### Components

1. DC Voltage Source (\( V_{ref} = 5V \)).
2. Resistors:
   - \( R = 1k\Omega \), \( 2R = 2k\Omega \).
3. SPDT Switches to simulate digital inputs.
4. Multimeter to measure output current (\( I_{out} \)).
5. Breadboard and wires.

### Circuit

1. R/2R Network:
   - Arrange resistors in an R/2R ladder pattern. For a 3-bit DAC:
     - First branch: \( 2R \) to ground.
     - Each bit connects to a \( R \) resistor in series with a \( 2R \) branch.

2. Digital Inputs:
   - Use SPDT switches to connect each bit either to \( V_{ref} \) (logic HIGH) or ground (logic LOW).

3. Output:
   - The output current (\( I_{out} \)) is taken from the bottom-most node of the resistor ladder.

4. Measurement:
   - Place a multimeter in series with the output to measure the current.

### Steps

1. :
   - Connect the R/2R ladder as described.
   - Attach SPDT switches to simulate the binary inputs (e.g., \( D2, D1, D0 \)).

2. Apply Input Combinations:
   - Set the switches to different binary combinations (e.g., \( 000, 001, 010, ... \)).
   - Observe the output current for each combination.

3. Record Output Current:
   - Measure \( I_{out} \) using the multimeter for each binary input.
   - Verify that \( I_{out} \) corresponds to the digital input.

### Results

1. Current Output:
   - The output current increases proportionally to the binary input:
     \[
     I_{out} = \frac{V_{ref}}{R} \cdot \frac{\text{Decimal Equivalent of Input}}{2^n}
     \]

2. Example for a 3-bit DAC:
   - \( R = 1k\Omega, V_{ref} = 5V \):
     \[
     I_{out} = 5mA \cdot \frac{\text{Decimal Input}}{8}
     \]
     - \( 000 \): \( I_{out} = 0 \)
     - \( 001 \): \( I_{out} = 0.625mA \)
     - \( 010 \): \( I_{out} = 1.25mA \)
     - \( 111 \): \( I_{out} = 3.75mA \)

### Insights

1. Precision:
   - The R/2R ladder structure ensures accurate and scalable digital-to-analog conversion with minimal resistor values.

2. Load Dependency:
   - The current output is ideal for applications where the load can directly utilize the current.

3. Applications:
   - Waveform generators, digital audio, and control systems.

This experiment can be implemented using SPDT switches for binary input, resistors for the R/2R ladder, and a multimeter for current measurement. It demonstrates how an R/2R Ladder DAC converts digital inputs into proportional current outputs.
