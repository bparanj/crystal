### Diode Circuit: Series Diode Limiter (Clipping Circuit)

A Series Diode Limiter, also known as a Clipping Circuit, limits the amplitude of an input signal by "clipping" portions of the waveform beyond a certain threshold. It uses diodes to restrict the voltage reaching the load, protecting sensitive components or shaping signals.

1. Clipping Operation:
   - When the input voltage exceeds the forward voltage of the diode (\( V_f \)), the diode conducts and "clips" the excess voltage.

2. Clipping Levels:
   - The clipping level can be set using the diode's forward voltage or by adding external voltage sources in series with the diode.

3. Applications:
   - Signal processing (wave shaping).
   - Protection circuits.
   - Amplitude control in audio and communication systems.

### Experiment

To design and simulate a Series Diode Limiter Circuit and observe its ability to clip the input signal at a specific threshold.

#### Components:
1. Diodes (2 × 1N4007 or similar).
2. Resistor (\( R = 1k\Omega \), load resistor).
3. AC Voltage Source (\( V_{in} = \pm 10V, 1kHz \)).
4. Oscilloscope (to visualize input and output waveforms).
5. Breadboard and wires.

### Circuit Connections:

1. AC Input Signal:
   - Connect the AC voltage source to one end of the load resistor (\( R \)).

2. Series Diodes:
   - Connect the cathode of one diode (\( D_1 \)) to the AC source.
   - Connect the anode of \( D_1 \) to the other end of \( R \).
   - Connect the anode of the second diode (\( D_2 \)) to the AC source.
   - Connect the cathode of \( D_2 \) to the other end of \( R \).

3. Output Signal:
   - Measure the voltage across \( R \) to observe the clipped waveform.

4. Oscilloscope:
   - Channel 1: Connect to the AC source to monitor the input waveform.
   - Channel 2: Connect across \( R \) to monitor the output waveform.

### Steps

#### 1. Observe Input and Output Waveforms:
1. Set the AC voltage source to \( \pm 10V, 1kHz \).
2. Use the oscilloscope to observe:
   - Channel 1: The sinusoidal input signal (\( V_{in} \)).
   - Channel 2: The output signal (\( V_{out} \)) across the load resistor.

#### 2. Analyze Clipping Behavior:
1. Note how the output signal is clipped at the forward voltage of the diodes (\( \pm 0.7V \) for silicon diodes).
2. Compare the input and output waveforms.

#### 3. Modify Clipping Levels:
1. Add small DC voltage sources (\( V_{offset} \)) in series with each diode to shift the clipping levels.
2. Observe how the output waveform changes:
   - For example, adding \( +2V \) and \( -2V \) offsets will clip the signal at \( \pm 2.7V \).

### Results

1. Without DC Offset:
   - The input signal (\( \pm 10V \)) is clipped at \( \pm 0.7V \) (the forward voltage of the diodes).
   - The output waveform is flattened at these levels.

2. With DC Offset:
   - The clipping thresholds shift by the offset voltage.
   - For \( V_{offset} = \pm 2V \), the signal is clipped at \( \pm 2.7V \).

### Insights

1. Clipping Threshold:
   - The threshold is determined by the diode's forward voltage (\( V_f \)) and any added offset voltage.

2. Waveform Shaping:
   - Series diode limiters are commonly used to shape signals for specific applications.

3. Applications:
   - Protecting circuits from overvoltage.
   - Limiting amplitude in signal processing systems.

In Tinkercad, you can:
1. Build the circuit with the diodes, resistor, and AC voltage source.
2. Use the oscilloscope to monitor the input and output waveforms.
3. Experiment with adding offset voltage sources in series with the diodes to modify the clipping levels.
4. Observe the clipping behavior and its impact on the waveform.

This experiment demonstrates the principle of using diodes for amplitude control and protection in electronic circuits.
