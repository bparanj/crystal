### Transistor Circuit: Common-Emitter Amplifier

The Common-Emitter Amplifier is a widely used transistor amplifier configuration. It provides voltage gain, current gain, and phase inversion of the input signal. The configuration is ideal for signal amplification in audio, RF, and general-purpose applications.

### Concepts:

1. Voltage Gain:
   - The circuit provides significant voltage gain, controlled by the collector (\( R_C \)) and emitter (\( R_E \)) resistors.

2. Phase Inversion:
   - The output signal is inverted (180° out of phase) relative to the input signal.

3. Input and Output Impedance:
   - Moderate input impedance and low output impedance make the circuit useful for driving loads.

4. Applications:
   - Signal amplification.
   - Audio systems and RF circuits.

### Experiment:

To design and simulate a Common-Emitter Amplifier using an NPN transistor and observe its voltage gain and phase inversion.

#### Components:

1. NPN Transistor (e.g., 2N2222 or BC547).
2. Resistors:
   - \( R_B1 = 100k\Omega \) (base biasing resistor).
   - \( R_B2 = 10k\Omega \) (voltage divider for base biasing).
   - \( R_C = 2.2k\Omega \) (collector resistor).
   - \( R_E = 470\Omega \) (emitter resistor).
3. Capacitors:
   - \( C_{in} = 10\mu F \) (input coupling capacitor).
   - \( C_{out} = 10\mu F \) (output coupling capacitor).
   - \( C_E = 100\mu F \) (bypass capacitor for emitter resistor).
4. DC Voltage Source (\( V_{CC} = 12V \)).
5. AC Voltage Source (\( V_{in} = 10mV_{peak}, 1kHz \)).
6. Oscilloscope (to observe input and output waveforms).
7. Breadboard and wires.

### Circuit

1. Biasing Network:
   - Connect \( R_B1 \) between \( V_{CC} \) and the transistor’s base.
   - Connect \( R_B2 \) between the base and ground to create a voltage divider for biasing.

2. Collector Circuit:
   - Connect \( R_C \) between the collector and \( V_{CC} \).

3. Emitter Circuit:
   - Connect \( R_E \) between the emitter and ground.
   - Place \( C_E \) in parallel with \( R_E \) to stabilize gain for AC signals.

4. Input Signal:
   - Connect \( V_{in} \) through \( C_{in} \) to the base of the transistor.

5. Output Signal:
   - Connect \( C_{out} \) to the transistor’s collector to couple the amplified signal to the output.

6. Oscilloscope:
   - Channel 1: Connect to \( V_{in} \) to monitor the input signal.
   - Channel 2: Connect to the output after \( C_{out} \).

### Steps

#### 1. Apply Input Signal:

1. Set \( V_{in} = 10mV_{peak}, 1kHz \) using the AC voltage source.
2. Observe the input waveform on Channel 1 and the output waveform on Channel 2 of the oscilloscope.

#### 2. Measure Voltage Gain:

1. Measure the peak-to-peak voltage of the input signal (\( V_{in(pp)} \)).
2. Measure the peak-to-peak voltage of the output signal (\( V_{out(pp)} \)).
3. Calculate the voltage gain (\( A_v \)) as:
   \[
   A_v = \frac{V_{out(pp)}}{V_{in(pp)}}
   \]

#### 3. Observe Phase Inversion:

1. Compare the input and output waveforms.
2. Confirm that the output signal is inverted (180° phase shift).

#### 4. Experiment with Component Values:

1. Vary \( R_C \) to observe its impact on voltage gain.
2. Remove \( C_E \) and note the reduction in gain due to emitter degeneration.
3. Adjust \( R_E \) to observe changes in bias stability and gain.

### Results:

1. Voltage Gain:
   - The circuit amplifies the input signal, with gain approximately:
     \[
     A_v = \frac{R_C}{R_E}
     \]
     (with \( C_E \) bypassed).

2. Phase Inversion:
   - The output signal is inverted relative to the input signal.

3. Effect of Components:
   - Increasing \( R_C \) increases gain.
   - Increasing \( R_E \) reduces gain but improves bias stability.

### Insights

1. Signal Amplification:
   - The common-emitter amplifier provides high voltage gain, making it ideal for amplifying weak signals.

2. Phase Inversion:
   - The circuit inverts the signal, which can be important in signal processing applications.

3. Stability and Gain:
   - The emitter resistor (\( R_E \)) stabilizes the operating point but reduces gain. Adding \( C_E \) bypasses \( R_E \) for AC signals, restoring gain.

4. Applications:
   - Used in audio amplifiers, RF amplifiers, and other signal amplification circuits.

In Tinkercad, you can:

1. Build the described circuit using the provided components.
2. Use the oscilloscope to monitor and compare the input and output waveforms.
3. Adjust component values (\( R_C \), \( R_E \), \( C_E \)) to study their effects on gain and stability.
4. Confirm the amplifier’s gain and phase inversion through waveform measurements and analysis.

This experiment demonstrates the amplification and phase inversion properties of a common-emitter amplifier and its practical applications in signal processing.
