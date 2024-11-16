### Capacitive Voltage Divider

A Capacitive Voltage Divider is a circuit that divides the input voltage across two capacitors connected in series. The output voltage is determined by the capacitance ratio, making it ideal for high-frequency AC signals.

---

### Key Concepts:

1. Voltage Division Principle:
   - The output voltage (\( V_{out} \)) depends on the ratio of the two capacitances:
     \[
     V_{out} = V_{in} \cdot \frac{C_2}{C_1 + C_2}
     \]

2. Applications:
   - High-frequency AC signal scaling.
   - Impedance matching in RF circuits.
   - AC coupling and filtering.

3. Frequency Dependency:
   - Works effectively for AC signals where capacitive reactance is significant:
     \[
     X_C = \frac{1}{2 \pi f C}
     \]

---

### Experiment Design for Tinkercad:

#### Objective:
To design and simulate a Capacitive Voltage Divider and observe how the output voltage changes with different capacitance ratios.

#### Components:
1. AC Voltage Source (\( V_{in} = 5V_{peak}, f = 1kHz \)).
2. Capacitors (\( C_1 = 1\mu F, C_2 = 2\mu F \)).
3. Oscilloscope (to observe waveforms).
4. Breadboard and wires.

---

### Circuit Configuration:

1. Voltage Divider:
   - Connect \( C_1 \) and \( C_2 \) in series.
   - Connect the AC voltage source (\( V_{in} \)) across \( C_1 + C_2 \).

2. Output Voltage:
   - Take \( V_{out} \) across \( C_2 \).

3. Ground Reference:
   - Connect the bottom terminal of \( C_2 \) to the ground of the AC voltage source.

4. Oscilloscope Connections:
   - Channel 1: Monitor the input voltage (\( V_{in} \)).
   - Channel 2: Monitor the output voltage (\( V_{out} \)).

---

### Steps to Perform:

1. Set Up the Circuit:
   - Assemble the capacitors and voltage source on the breadboard as described.

2. Apply Input Signal:
   - Configure the AC voltage source to provide a sinusoidal waveform (\( 5V_{peak}, 1kHz \)).

3. Observe Waveforms:
   - Use the oscilloscope to monitor the input voltage (\( V_{in} \)) and output voltage (\( V_{out} \)).

4. Experiment with Capacitance Values:
   - Replace \( C_1 \) and \( C_2 \) with different values (\( 0.1\mu F, 10\mu F \)) to observe changes in \( V_{out} \).

---

### Expected Results:

1. Output Voltage:
   - For \( C_1 = 1\mu F \), \( C_2 = 2\mu F \), and \( V_{in} = 5V \):
     \[
     V_{out} = 5V \cdot \frac{2\mu F}{1\mu F + 2\mu F} = 3.33V
     \]

2. Capacitance Ratio:
   - Increasing \( C_2 \) increases \( V_{out} \), while increasing \( C_1 \) decreases \( V_{out} \).

3. Frequency Dependence:
   - The divider works effectively at high frequencies where \( X_C \) is small and the capacitive reactance is significant.

---

### Key Insights:

1. High-Frequency Applications:
   - Capacitive dividers are ideal for RF and AC circuits due to their high-frequency characteristics.

2. Component Ratios:
   - The output voltage is directly proportional to the capacitance ratio.

3. Advantages:
   - No energy dissipation in resistors (unlike resistive dividers), making it efficient for AC applications.

---

This experiment can be implemented in Tinkercad, where you can visualize the input and output voltages on an oscilloscope. By adjusting \( C_1 \) and \( C_2 \), you can observe the impact of capacitance ratios on the output voltage in a Capacitive Voltage Divider.
