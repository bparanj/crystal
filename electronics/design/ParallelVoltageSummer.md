Requires IC

Can this experiment be done without IC.

### Parallel Voltage Summer

A Parallel Voltage Summer is a circuit that sums multiple input voltages and provides a weighted or unweighted total voltage at the output. It is often implemented using resistors in parallel with an operational amplifier to achieve precise voltage addition.

### Concepts

1. Summing Principle:
   - The output voltage (\( V_{out} \)) is the weighted sum of the input voltages:
     \[
     V_{out} = -\left( \frac{V_1}{R_1} + \frac{V_2}{R_2} + \dots \right) \cdot R_f
     \]
     - \( R_1, R_2 \): Input resistors.
     - \( R_f \): Feedback resistor.

2. Applications:
   - Audio mixing.
   - Analog signal processing.
   - Voltage level scaling.

### Circuit

#### Objective:

To design and simulate a Parallel Voltage Summer circuit using an operational amplifier.

#### Components:
1. Operational Amplifier (e.g., LM741).
2. Resistors (\( R_1, R_2, R_f = 10k\Omega \)).
3. DC Voltage Sources (\( V_1 = 2V, V_2 = 3V \)).
4. Multimeter to measure \( V_{out} \).
5. Breadboard and wires.

### Circuit

1. Input Voltages:
   - Connect the positive terminals of the voltage sources (\( V_1, V_2 \)) to their respective resistors (\( R_1, R_2 \)).
   - Connect the other ends of \( R_1 \) and \( R_2 \) to the inverting input (\( - \)) of the op-amp.

2. Feedback Resistor:
   - Connect the feedback resistor (\( R_f \)) between the op-amp output and its inverting input (\( - \)).

3. Non-Inverting Input:
   - Connect the non-inverting input (\( + \)) of the op-amp to ground.

4. Output Voltage:
   - Measure \( V_{out} \) at the op-amp output terminal.

### Steps

1. :
   - Assemble the circuit on the breadboard as described.

2. Apply Input Voltages:
   - Set \( V_1 = 2V \) and \( V_2 = 3V \) using DC voltage sources.

3. Measure Output Voltage:
   - Use a multimeter to measure \( V_{out} \).

4. Experiment with Resistor Values:
   - Change \( R_1, R_2 \), or \( R_f \) to observe their effect on \( V_{out} \).

### Results:

1. Unweighted Summer:
   - If \( R_1 = R_2 = R_f \):
     \[
     V_{out} = -(V_1 + V_2)
     \]
     For \( V_1 = 2V \) and \( V_2 = 3V \):
     \[
     V_{out} = -(2V + 3V) = -5V
     \]

2. Weighted Summer:
   - If \( R_1 \neq R_2 \):
     \[
     V_{out} = -\left( \frac{V_1}{R_1} + \frac{V_2}{R_2} \right) \cdot R_f
     \]
     For \( R_1 = 10k\Omega, R_2 = 20k\Omega, R_f = 10k\Omega \):
     \[
     V_{out} = -\left( \frac{2V}{10k\Omega} + \frac{3V}{20k\Omega} \right) \cdot 10k\Omega = -3.5V
     \]

3. Linearity:
   - \( V_{out} \) varies linearly with the input voltages.

### Insights:

1. Flexibility:
   - Adjusting \( R_1, R_2, \dots, R_f \) allows for weighted summation of input voltages.

2. Inversion:
   - The output voltage is inverted due to the inverting configuration of the op-amp. A non-inverting summer can be designed if inversion is undesirable.

3. Applications:
   - Used in audio mixers, waveform generators, and signal processing circuits.

you can vary input voltages and resistor values to observe the summing behavior of the circuit.
