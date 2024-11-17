### Capacitive Voltage-to-Current (V-to-I) Differentiator

A Capacitive V-to-I Differentiator is a circuit that converts an input voltage signal into a current proportional to the rate of change (time derivative) of the input voltage. This is achieved using a capacitor, which inherently differentiates the input voltage due to its relationship with current:

\[
I_C = C \cdot \frac{dV}{dt}
\]

### Concepts

1. Capacitive Behavior:
   - The current through a capacitor is proportional to the time rate of change of the voltage across it.
   - Faster voltage changes result in higher currents.

2. Output Current:
   - The output current \( I_C \) is given by:
     \[
     I_C = C \cdot \frac{dV_{in}}{dt}
     \]
     Where:
     - \( C \): Capacitance in farads.
     - \( \frac{dV_{in}}{dt} \): Time derivative of the input voltage.

3. Applications:
   - Signal differentiation in waveform analysis.
   - High-pass filtering.
   - Edge detection in signal processing.

### Experiment

#### Objective

To demonstrate the concept of a Capacitive V-to-I Differentiator using a capacitor and observe the output current for varying input voltages.

#### Components

1. AC Voltage Source (\( V_{in} = 5V_{peak}, f = 1kHz \)).
2. Capacitor (\( C = 1\mu F \)).
3. Resistor (\( R = 1k\Omega \)) for current-to-voltage conversion (optional).
4. Multimeter (to measure current).
5. Oscilloscope (to observe voltage and current waveforms).
6. Breadboard and wires.

### Circuit

1. Voltage Source:
   - Connect the AC voltage source (\( V_{in} \)) to one terminal of the capacitor (\( C \)).

2. Current Measurement:
   - Connect the other terminal of the capacitor to ground through a multimeter in current measurement mode.

3. Optional Resistor:
   - Place a resistor (\( R \)) in series with the capacitor to observe the voltage drop corresponding to the current (\( V_R = I_C \cdot R \)).

4. Oscilloscope Connections:
   - Channel 1: Monitor the input voltage (\( V_{in} \)).
   - Channel 2: Monitor the voltage across the resistor (\( V_R \)), which is proportional to the current.

### Steps

1. Set Input Signal:
   - Configure the AC voltage source to generate a sine wave:
     - Amplitude: \( 5V_{peak} \).
     - Frequency: \( 1kHz \).

2. Measure Current:
   - Observe the current through the capacitor using the multimeter.
   - Expected \( I_C \):
     \[
     I_C = C \cdot 2\pi f \cdot V_{peak}
     \]

3. Observe Waveforms:
   - Use the oscilloscope to compare the input voltage waveform (\( V_{in} \)) and the output current waveform (\( I_C \)).

4. Change Input Frequency:
   - Increase the frequency of \( V_{in} \) (e.g., \( 2kHz, 5kHz \)).
   - Observe how the output current increases with the frequency.

### Results

1. Current Proportional to Derivative:
   - The current waveform (\( I_C \)) will be a sine wave that leads the input voltage waveform by 90°, representing the time derivative.

2. Frequency Dependence:
   - The current amplitude increases with input signal frequency (\( f \)):
     \[
     I_C = C \cdot 2\pi f \cdot V_{peak}
     \]

3. Voltage-to-Current Conversion:
   - The current is directly proportional to the rate of change (\( \frac{dV}{dt} \)) of the input voltage.

### Insights

1. High-Pass Behavior:
   - The circuit behaves as a high-pass filter, passing higher frequency components more effectively.

2. Applications:
   - Used in edge detection, waveform differentiation, and signal conditioning.

3. Component Selection:
   - The capacitor value (\( C \)) determines the sensitivity to voltage changes.

This experiment can be implemented in Tinkercad, allowing you to observe the differentiating effect of a capacitor on an AC voltage signal and how the output current varies with input signal frequency and amplitude.
