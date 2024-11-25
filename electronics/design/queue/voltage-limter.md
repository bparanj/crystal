### Voltage Limiting Using a Series Diode

A series diode can limit voltage in a circuit by exploiting its forward voltage drop (\(V_f\)) and conducting only when the input voltage exceeds this threshold. This behavior is commonly used to protect sensitive components from overvoltage.

### Concepts:

1. Forward Voltage Drop (\(V_f\)):
   - A silicon diode typically has a \(V_f \approx 0.7V\).
   - A Schottky diode has a lower \(V_f \approx 0.3V\).

2. Voltage Clipping:
   - The series diode limits the voltage to \( V_{out} = V_{in} - V_f \) when forward-biased.
   - If the input voltage is below \(V_f\), the diode blocks current flow, and the output voltage remains 0V.

3. Applications:
   - Protecting circuits from voltage spikes.
   - Ensuring voltage does not exceed a safe level for sensitive components.

### Experiment

#### Components:

1. AC voltage source (\( V_{peak} = 5V, f = 50Hz \)).
2. Diode (e.g., 1N4148 or Schottky diode).
3. Resistor (Load) (\( R = 1k\Omega \)).
4. Oscilloscope (to observe the waveform).
5. Breadboard and wires.

### Circuit

1. Series Diode:
   - Connect the anode of the diode to the AC voltage source's positive terminal.
   - Connect the cathode to one end of the resistor (\( R \)).
   - Connect the other end of the resistor to the AC source ground.

2. Oscilloscope Connections:
   - Channel 1: Across the AC voltage source to observe the input waveform.
   - Channel 2: Across the resistor to observe the output waveform.

### Steps

1. Set Input Signal:
   - Configure the AC voltage source to produce a sine wave:
     - Peak voltage: \( 5V \)
     - Frequency: \( 50Hz \).

2. Observe Input Waveform:
   - Monitor the input sine wave on Channel 1 of the oscilloscope.

3. Observe Output Waveform:
   - Monitor the voltage across the resistor on Channel 2 of the oscilloscope.

4. Experiment with Diode Types:
   - Replace the diode with a Schottky diode and observe the effect on the output waveform.

### Observations:

1. Forward Limiting:
   - During the positive half-cycle of the input, the diode conducts once the voltage exceeds \( V_f \), limiting the output to:
     \[
     V_{out} = V_{in} - V_f
     \]

2. Blocking Negative Cycle:
   - During the negative half-cycle, the diode is reverse-biased, and no current flows, resulting in \( V_{out} = 0V \).

3. Diode Type Effect:
   - A Schottky diode reduces the voltage drop to \( \approx 0.3V \), limiting the output less compared to a silicon diode.

### Insights:

1. Voltage Protection:
   - Series diodes are commonly used to protect circuits by limiting voltage spikes.

2. Fine-Tuning:
   - Multiple diodes in series can increase the limiting voltage (\( V_{total} = n \cdot V_f \)).

3. Applications:
   - Overvoltage protection in power supplies and signal conditioning.

This experiment can be simulated in Tinkercad, where you can visualize how the diode limits the voltage and experiment with different diodes to observe their effects on the output waveform.
