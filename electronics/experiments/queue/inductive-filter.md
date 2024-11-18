### AC Voltage Decoupling Using a Series Inductor

When an inductor is connected in series with an AC voltage source, it can decouple or reduce the AC voltage across the load by introducing inductive reactance (\(X_L\)). This decoupling effect depends on the frequency of the AC signal and the value of the inductor.

1. Inductive Reactance (\(X_L\)):
   - The inductor opposes changes in current, and its impedance increases with frequency:
     \[
     X_L = 2 \pi f L
     \]
   - At higher frequencies, \(X_L\) becomes large, reducing the voltage reaching the load.

2. Voltage Division:
   - The AC voltage is divided between the inductor and the load based on their impedance:
     \[
     V_{load} = V_{source} \cdot \frac{Z_{load}}{\sqrt{X_L^2 + Z_{load}^2}}
     \]

3. Phase Shift:
   - An inductor causes the current to lag the voltage by 90°.

### Experiment

#### Components:

1. AC Voltage Source (\( V_{rms} = 10V, f = 50Hz \)).
2. Resistor (Load) (\( R = 1k\Omega \)).
3. Inductor (\( L = 100mH \)).
4. Oscilloscope (to observe phase shift and voltage drop).
5. Multimeter (to measure RMS voltage across the load).
6. Breadboard and connecting wires.

### Circuit

1. Connect the AC voltage source to the breadboard.
2. Place the inductor (\( L \)) in series with the AC voltage source.
3. Connect the resistor (\( R \)) as a load in series with the inductor.
4. Attach the oscilloscope probes:
   - Across the AC source to observe the input voltage.
   - Across the resistor to observe the output voltage.
5. Optionally, connect a multimeter across the resistor to measure the RMS voltage.

### Steps:

1. Initial Measurements:
   - Set the AC voltage source to 10V RMS at 50Hz.
   - Measure the voltage across the load (\( V_{load} \)) using the multimeter.
   - Observe the waveform across the resistor using the oscilloscope.

2. Experiment with Frequency:
   - Vary the frequency of the AC source (e.g., 10Hz, 50Hz, 100Hz).
   - Observe how \( V_{load} \) decreases as the frequency increases due to the rising \( X_L \).

3. Observe Phase Shift:
   - Compare the phase of the voltage across the load with the input voltage on the oscilloscope.

### Observations:

1. Voltage Drop:
   - At lower frequencies (\( f = 10Hz \)), \( X_L \) is small, allowing more voltage to reach the load.
   - At higher frequencies (\( f = 100Hz \)), \( X_L \) becomes significant, reducing \( V_{load} \).

2. Phase Shift:
   - The voltage across the load lags the source voltage due to the phase shift introduced by the inductor.

3. Frequency Dependence:
   - The decoupling effect strengthens as the frequency increases because \( X_L \propto f \).

### Insights:

1. High-Frequency Decoupling:
   - Series inductors are effective at attenuating high-frequency AC components while allowing low-frequency or DC components to pass.

2. Applications:
   - Inductive decoupling is used in power supplies and signal conditioning to filter high-frequency noise.

3. Inductor Selection:
   - Larger inductors provide stronger decoupling at lower frequencies, making them suitable for specific filtering needs.

This experiment is easily simulated in Tinkercad, allowing you to observe the decoupling effects of a series inductor on AC voltage.
