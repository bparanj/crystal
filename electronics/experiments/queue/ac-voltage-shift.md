### AC Voltage Shifting Using a Series Capacitor

Connecting a capacitor in series with an AC voltage source shifts the voltage across a load due to the capacitor’s reactance (\(X_C\)), which depends on the frequency of the AC signal and the capacitor's value. This property can cause a phase shift between the current and voltage, and the voltage across the load will no longer align perfectly with the source voltage.

### Concepts:

1. Capacitive Reactance (\(X_C\)):
   - The capacitor introduces impedance that depends on the frequency (\(f\)) of the AC signal:
     \[
     X_C = \frac{1}{2 \pi f C}
     \]
   - At lower frequencies, \(X_C\) is higher, reducing the voltage across the load.
   - At higher frequencies, \(X_C\) is lower, allowing more voltage to pass to the load.

2. Voltage Division:
   - The voltage is divided between the capacitor and the load according to their impedance. The voltage across the load depends on the load impedance (\(Z_{load}\)) and \(X_C\).

3. Phase Shift:
   - A capacitor causes a phase shift of 90° between current and voltage, with current leading voltage.

### Experiment

#### Components:

1. AC Voltage Source (\( V_{rms} = 10V, f = 50Hz \)).
2. Resistor (Load) (\( R = 1k\Omega \)).
3. Capacitor (\( C = 10\mu F \)).
4. Oscilloscope (to observe phase shift and voltage drop).
5. Multimeter (to measure RMS voltage across the load).
6. Breadboard and connecting wires.

### Setup:

1. Connect the AC voltage source to the breadboard.
2. Insert the capacitor (\( C \)) in series with the AC voltage source.
3. Connect a resistor (\( R \)) as the load in series with the capacitor.
4. Attach the oscilloscope probes:
   - Across the AC source to observe input voltage.
   - Across the resistor to observe the output voltage.
5. Optionally, connect a multimeter across the resistor to measure the RMS voltage.


### Steps:

1. Initial Measurements:
   - Set the AC voltage source to 10V RMS at 50Hz.
   - Measure the voltage across the load (\( V_{load} \)) using the multimeter.
   - Observe the waveform across the resistor using the oscilloscope.

2. Experiment with Frequency:
   - Vary the frequency of the AC source (e.g., 10Hz, 50Hz, 100Hz).
   - Observe how \( V_{load} \) changes due to the capacitive reactance (\(X_C\)).

3. Observe Phase Shift:
   - Compare the phase of the voltage across the load with the input voltage on the oscilloscope.

### Observations:

1. Voltage Drop:
   - At lower frequencies (\( f = 10Hz \)), the capacitive reactance is higher, causing a greater voltage drop across the capacitor and reducing \( V_{load} \).
   - At higher frequencies (\( f = 100Hz \)), the capacitive reactance decreases, allowing more voltage to pass to the load.

2. Phase Shift:
   - The voltage across the load will lag the source voltage due to the phase shift introduced by the capacitor.

3. Voltage Division:
   - The load voltage is determined by the voltage division between the capacitor and resistor:
     \[
     V_{load} = V_{source} \cdot \frac{Z_{load}}{\sqrt{X_C^2 + Z_{load}^2}}
     \]

### Insights:

1. AC Coupling:
   - Series capacitors are often used in audio and signal circuits for AC coupling to block DC components while passing AC signals.

2. Frequency Sensitivity:
   - The shifting effect is frequency-dependent, making this configuration useful for filtering or tuning applications.

3. Capacitor Selection:
   - The capacitor value (\(C\)) determines the cutoff frequency and degree of voltage shifting.

This experiment is easily implementable in Tinkercad and provides a clear understanding of how series capacitors affect AC voltages.
