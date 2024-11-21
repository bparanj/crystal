### Inductive Current-to-Voltage (I-to-V) Differentiator

An Inductive I-to-V Differentiator is a circuit that converts an input current signal into an output voltage proportional to the rate of change (time derivative) of the current. This is achieved by utilizing the relationship between the voltage across an inductor and the time rate of change of the current passing through it:

\[
V_L = L \cdot \frac{dI}{dt}
\]

### Concepts:

1. Inductive Behavior:
   - The voltage across an inductor is proportional to the time rate of change of the current flowing through it.
   - A faster-changing current (\( \frac{dI}{dt} \)) induces a larger voltage.

2. Output Voltage:
   - The output voltage of the circuit is given by:
     \[
     V_{out} = L \cdot \frac{dI_{in}}{dt}
     \]

3. Applications:
   - Waveform differentiation in signal processing.
   - Current-to-voltage conversion in high-frequency circuits.
   - Edge detection and noise filtering.

### Experiment

#### Objective:

To design and simulate an Inductive I-to-V Differentiator and observe how the output voltage responds to time-varying input current.

#### Components:

1. Inductor (\( L = 10mH \)).
2. Current Source (\( I_{in} \), simulated with a function generator or resistor and voltage source).
3. Resistor (\( R = 1k\Omega \)) to measure voltage across the inductor.
4. Oscilloscope (to observe input current and output voltage waveforms).
5. Breadboard and wires.

### Circuit

1. Input Current:
   - Connect the input current source (\( I_{in} \)) to the inductor (\( L \)).

2. Inductive Voltage:
   - Place the resistor (\( R \)) in series with the inductor to measure the voltage drop across the inductor.

3. Output Voltage:
   - Take the output voltage (\( V_{out} \)) across the resistor (\( R \)).

4. Oscilloscope Connections:
   - Channel 1: Monitor the input current (\( I_{in} \)).
   - Channel 2: Monitor the voltage across the inductor (\( V_{out} \)).

### Steps

1. :
   - Build the circuit as described, ensuring correct connections for the inductor and resistor.

2. Apply Input Current:
   - Use a sinusoidal or time-varying input current (\( I_{in} \)) from a current source or a function generator.

3. Observe Waveforms:
   - Use the oscilloscope to observe:
     - The input current waveform (\( I_{in} \)).
     - The output voltage waveform (\( V_{out} \)).

4. Experiment with Frequency:
   - Vary the frequency of \( I_{in} \) and observe changes in \( V_{out} \).

5. Change Inductance:
   - Replace \( L \) with different inductors (\( 5mH, 20mH \)) and observe how \( V_{out} \) changes.

### Results:

1. Output Voltage:
   - \( V_{out} \) is proportional to the derivative of \( I_{in} \):
     \[
     V_{out} = L \cdot \frac{dI_{in}}{dt}
     \]

2. Waveform Relationship:
   - For a sinusoidal \( I_{in}(t) = I_{peak} \cdot \sin(2\pi f t) \):
     \[
     V_{out}(t) = L \cdot 2\pi f \cdot I_{peak} \cdot \cos(2\pi f t)
     \]
     - \( V_{out} \) is 90° phase-shifted from \( I_{in} \).

3. Frequency Dependence:
   - Higher frequency (\( f \)) leads to larger \( V_{out} \), as \( V_{out} \propto f \).

4. Inductance Effect:
   - Larger \( L \) results in higher \( V_{out} \) for the same \( \frac{dI_{in}}{dt} \).

### Insights:

1. Waveform Differentiation:
   - The circuit emphasizes high-frequency components, acting as a differentiator for current waveforms.

2. Inductor Selection:
   - The value of \( L \) determines the sensitivity and scaling of \( V_{out} \).

3. Applications:
   - Used in signal processing, waveform shaping, and high-frequency circuit design.

you can visualize the input current and output voltage waveforms using the oscilloscope. It demonstrates the principles of differentiation using an inductor in a simple I-to-V converter circuit.
