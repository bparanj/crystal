### Inductive Voltage-to-Voltage (V-to-V) Differentiator

An Inductive V-to-V Differentiator is a circuit that generates an output voltage proportional to the rate of change (time derivative) of the input voltage. This is achieved by utilizing an inductor in series with the input voltage source, with the output voltage taken across a resistor.

---

### Key Concepts:

1. Inductive Differentiation:
   - The voltage across an inductor is proportional to the rate of change of the current:
     \[
     V_L = L \cdot \frac{dI}{dt}
     \]
   - In a circuit with an inductor and resistor, this relationship translates to:
     \[
     V_{out} = L \cdot \frac{dV_{in}}{dt}
     \]

2. Applications:
   - Signal processing (edge detection, pulse shaping).
   - High-pass filtering for AC signals.
   - Derivative computation in analog systems.

---

### Experiment Design for Tinkercad:

#### Objective:
To design and simulate an Inductive V-to-V Differentiator and observe how the output voltage responds to time-varying input signals.

#### Components:
1. Inductor (\( L = 10mH \)).
2. Resistor (\( R = 1k\Omega \)).
3. AC Voltage Source (\( V_{in} = 5V_{peak}, f = 1kHz \)).
4. Oscilloscope (to observe input and output waveforms).
5. Breadboard and wires.

---

### Circuit Configuration:

1. Input Voltage:
   - Connect the AC voltage source to one terminal of the inductor (\( L \)).

2. Inductive Differentiation:
   - Connect the other terminal of the inductor to one end of the resistor (\( R \)).

3. Output Voltage:
   - Measure the output voltage (\( V_{out} \)) across the resistor (\( R \)).

4. Ground Reference:
   - Connect the free end of \( R \) to the ground of the AC voltage source.

5. Oscilloscope Connections:
   - Channel 1: Monitor the input voltage (\( V_{in} \)).
   - Channel 2: Monitor the output voltage (\( V_{out} \)).

---

### Steps to Perform:

1. Set Up the Circuit:
   - Assemble the circuit on the breadboard as described.

2. Apply Input Signal:
   - Use the AC voltage source to generate a sinusoidal or square wave signal (\( 5V_{peak}, 1kHz \)) as \( V_{in} \).

3. Observe Waveforms:
   - Use an oscilloscope to monitor:
     - The input voltage (\( V_{in} \)).
     - The output voltage (\( V_{out} \)).

4. Experiment with Components:
   - Replace \( L \) (\( 5mH, 20mH \)) and \( R \) (\( 500\Omega, 10k\Omega \)) to observe their effects on the differentiation.

---

### Expected Results:

1. Sinusoidal Input:
   - For \( V_{in}(t) = V_{peak} \sin(\omega t) \):
     \[
     V_{out}(t) = \omega L \cdot V_{peak} \cos(\omega t)
     \]
   - The output voltage is phase-shifted by \( 90^\circ \) (cosine wave).

2. Square Wave Input:
   - The output shows sharp spikes at the rising and falling edges of the square wave, corresponding to the rapid changes in voltage.

3. Component Effects:
   - Larger \( L \): Increases the amplitude of the differentiated signal.
   - Larger \( R \): Increases the load impedance but does not affect the differentiation.

4. Frequency Dependence:
   - Higher frequencies result in larger output voltage amplitudes due to the proportionality to \( \omega \).

---

### Key Insights:

1. Waveform Differentiation:
   - The circuit emphasizes rapid changes in the input signal, making it effective for detecting transitions and sharp edges.

2. Frequency Response:
   - The output amplitude increases with input frequency, making the circuit function as a high-pass filter.

3. Applications:
   - Widely used in signal processing, analog computation, and waveform shaping.

---

This experiment can be implemented in Tinkercad, where you can observe the input and output waveforms on an oscilloscope. By varying the input signal and component values, you can demonstrate the behavior of the Inductive V-to-V Differentiator.
