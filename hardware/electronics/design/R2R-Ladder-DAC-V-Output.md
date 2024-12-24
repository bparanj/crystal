### R/2R Ladder DAC (Voltage Output)

An R/2R Ladder Digital-to-Analog Converter (DAC) with a voltage output converts a binary digital input into a proportional analog voltage. This is achieved using a resistor network (R/2R ladder) that generates a weighted voltage sum corresponding to the binary input.

### Concepts

1. R/2R Resistor Network:
   - The network consists of resistors in a repeating R and 2R configuration.
   - It performs binary-weighted division of the input voltages.

2. Binary Weighted Output:
   - Each digital bit contributes a specific fraction of the reference voltage (\( V_{ref} \)) to the output:
     \[
     V_{out} = V_{ref} \cdot \frac{\text{Digital Input}}{2^n}
     \]
     - \( V_{ref} \): Reference voltage.
     - \( n \): Number of bits.
     - Digital input: Decimal equivalent of the binary input.

3. Applications:
   - Audio signal generation.
   - Data acquisition systems.
   - Waveform generation.

### Experiment

#### Objective

To design and simulate an R/2R Ladder DAC (Voltage Output) using Tinkercad and demonstrate the relationship between binary input and output voltage.

#### Components

1. DC Voltage Source (\( V_{ref} = 5V \)).
2. Resistors:
   - \( R = 1k\Omega \).
   - \( 2R = 2k\Omega \).
3. SPDT Switches to simulate digital inputs (\( D_n \)).
4. Multimeter to measure output voltage (\( V_{out} \)).
5. Breadboard and wires.

### Circuit

1. R/2R Ladder Network:
   - Arrange resistors in an R/2R ladder configuration for a 3-bit DAC:
     - Connect \( 2R \) resistors in parallel branches.
     - Connect \( R \) resistors in series with each \( 2R \) branch.
     - Terminate the ladder with a \( 2R \) resistor to ground.

2. Digital Inputs:
   - Use SPDT switches to simulate the binary input (\( D2, D1, D0 \)).
   - Connect each switch to either \( V_{ref} \) (logic HIGH) or ground (logic LOW).

3. Output Voltage:
   - Take the output voltage (\( V_{out} \)) from the junction of the last \( R \) resistor and the load resistor (\( R_L \)).

4. Load Resistor:
   - Use \( R_L = 1k\Omega \) to simulate the load.

5. Measurement:
   - Use a multimeter to measure \( V_{out} \).

### Steps

1. :
   - Build the R/2R ladder as described.
   - Connect SPDT switches to simulate binary inputs.

2. Apply Digital Input:
   - Set the switches to different binary combinations (e.g., \( 000, 001, 010, 011, \dots \)).

3. Measure Output Voltage:
   - Use a multimeter to measure \( V_{out} \) for each binary input.

4. Record Observations:
   - Record \( V_{out} \) for each binary input combination.

### Results

For a 3-bit DAC with \( V_{ref} = 5V \):

1. Binary Input vs. Output Voltage:
   \[
   V_{out} = V_{ref} \cdot \frac{\text{Decimal Input}}{2^n}
   \]

| Binary Input | Decimal Equivalent | Output Voltage (\( V_{out} \)) |
|-------------------|-------------------------|------------------------------------|
| \( 000 \)         | 0                       | 0V                                 |
| \( 001 \)         | 1                       | \( 5V \cdot \frac{1}{8} = 0.625V \)|
| \( 010 \)         | 2                       | \( 5V \cdot \frac{2}{8} = 1.25V \) |
| \( 011 \)         | 3                       | \( 5V \cdot \frac{3}{8} = 1.875V \)|
| \( 100 \)         | 4                       | \( 5V \cdot \frac{4}{8} = 2.5V \)  |
| \( 101 \)         | 5                       | \( 5V \cdot \frac{5}{8} = 3.125V \)|
| \( 110 \)         | 6                       | \( 5V \cdot \frac{6}{8} = 3.75V \) |
| \( 111 \)         | 7                       | \( 5V \cdot \frac{7}{8} = 4.375V \)|

2. Linear Relationship:
   - \( V_{out} \) increases linearly with the decimal equivalent of the binary input.

### Insights

1. Scalability:
   - The R/2R ladder design is easily scalable for higher bit DACs with minimal resistors.

2. Load Dependence:
   - Use a high-value \( R_L \) to minimize loading effects and maintain accuracy.

3. Applications:
   - Used in waveform generation, signal processing, and digital audio systems.


you can observe how the output voltage changes in response to binary inputs. It demonstrates the principles of digital-to-analog conversion using an R/2R Ladder DAC.
