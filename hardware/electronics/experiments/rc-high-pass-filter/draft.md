
PENDING

Checkout https://www.falstad.com/circuit/e-index.html   
Calculate cutoff frequency for 10 k ohm resistor and 0.1 micro farad capacitor.
Test at the Cutoff Frequency.

The RC high-pass filter uses a capacitor to block low-frequency signals and a resistor to allow high-frequency signals to pass. At low frequencies, the capacitor has a high impedance, reducing current flow. At high frequencies, the capacitor's impedance decreases, allowing signals to pass through the resistor with minimal attenuation.

We analyze the attenuation of low-frequency signals and the near-identical input and output signals at high frequencies, confirming the filter's operation.

For a 10 kΩ resistor and a 0.1 µF capacitor, the cutoff frequency is approximately 1.59 kHz. Above this frequency, signals pass through with minimal attenuation; below this frequency, signals are attenuated.

Test at the Cutoff Frequency:

- Set the AC source frequency near the cutoff frequency (around 1.6 kHz).
- Expected Outcome: At the cutoff frequency, the output signal amplitude should be approximately 70% of the input signal amplitude, indicating the point where the filter begins to pass higher frequencies more effectively.

High-Pass Filter Behavior:

This RC circuit acts as a high-pass filter because the capacitor blocks low frequencies by having high impedance at low frequencies, while allowing high frequencies to pass with less impedance.

Cutoff Frequency:

The cutoff frequency is where the filter transitions between attenuating low frequencies and allowing high frequencies. Frequencies above this point pass with minimal attenuation, while frequencies below are increasingly blocked.

This experiment demonstrates how an RC high-pass filter allows higher frequencies while attenuating lower ones, which is useful in applications like audio signal processing and removing unwanted low-frequency noise from signals.

Create a simple RC (Resistor-Capacitor) high-pass filter to observe how it allows high-frequency signals to pass while attenuating lower frequencies.

Increase Frequency: 

Gradually increase the frequency (e.g., 100 Hz, 500 Hz, 1 kHz, 10 kHz, etc.).

Record Observations: 

Note how the amplitude of the output signal changes relative to the input as the frequency increases.

At low frequencies, the output signal's amplitude should be much lower than the input amplitude, indicating attenuation.

As the frequency increases, the output amplitude should rise, approaching the input amplitude, demonstrating the high-pass filter effect.

This experiment demonstrates that an RC high-pass filter allows high-frequency signals to pass while attenuating low frequencies, illustrating the behavior of a basic high-pass filter.

### **Troubleshooting and Adjustments**

1. **Flat Output Signal:**
   - If the output appears as a flat line, check:
     - Frequency: Ensure the input signal frequency is above \(f_c\).
     - Connections: Verify proper series configuration of the capacitor and resistor.
     - Oscilloscope Settings: Adjust voltage and time scales to detect small signals.

2. **Signal Alignment:**
   - If the output is not attenuated as expected at low frequencies, confirm the resistor and capacitor values.

This experiment demonstrates the fundamental operation of an RC high-pass filter:

- Low-frequency signals (\(f < f_c\)) are attenuated due to the high impedance of the capacitor.
- High-frequency signals (\(f > f_c\)) pass through with minimal attenuation, as the capacitor's impedance decreases.

High-pass filters are essential in applications like audio processing, signal conditioning, and communication systems. By understanding their behavior, we can effectively manipulate signals to meet specific requirements. This demonstration reinforces the importance of frequency-dependent filtering in circuit design.

### Observations

1. Input Signal:
   - The input oscilloscope shows a 10 V scale sine wave, which means the input signal has a peak-to-peak amplitude of 10 V.

2. Output Signal:
   - The output oscilloscope shows a 4 V scale sine wave, meaning the output signal has been attenuated to 4 V peak-to-peak.

3. Attenuation Below Cutoff Frequency:
   - At 100 Hz, which is below the cutoff frequency of \(f_c = 159 \, \text{Hz}\) (calculated earlier for \(R = 10 \, \text{k}\Omega\) and \(C = 0.1 \, \mu\text{F}\)), the high-pass filter attenuates lower frequencies. The observed reduction in output voltage aligns with this behavior.

### What This Means

- The RC high-pass filter is performing as expected:
  - Low Frequencies (\(f < f_c\)): Signals are attenuated.
  - High Frequencies (\(f > f_c\)): Signals pass with minimal attenuation.

At 100 Hz:

- The output amplitude is lower because the signal frequency is below the cutoff, where the capacitor offers higher impedance, limiting current flow through the resistor and reducing the voltage across it.

The observed output signal at 4 V peak-to-peak confirms that the filter is attenuating low-frequency components as designed. If you increase the input frequency closer to or above \(f_c = 159 \, \text{Hz}\), the output signal amplitude will increase and eventually match the input signal at higher frequencies.

At 1 kHz, the input and output waveforms being the same and on the same scale indicates that the signal frequency is well above the cutoff frequency (\(f_c = 159 \, \text{Hz}\)). The high-pass filter allows high-frequency signals to pass with minimal attenuation, showing the filter's expected behavior.

### **Observations**

#### At 100 Hz (Low Frequency)

1. **Input Signal:**
   - The input oscilloscope displays a 5 V peak-to-peak sine wave.
2. **Output Signal:**
   - The output oscilloscope shows an attenuated signal (e.g., 4 V peak-to-peak).
   - This attenuation demonstrates that frequencies below \(f_c\) are partially blocked by the capacitor, which has high impedance at low frequencies.

#### At 1 kHz (High Frequency)

1. **Input Signal:**
   - The input remains a 5 V peak-to-peak sine wave.
2. **Output Signal:**
   - The output matches the input in amplitude and shape.
   - At frequencies above \(f_c\), the capacitor's impedance decreases, allowing high-frequency signals to pass with minimal attenuation.

### **Expected Behavior**

1. **Below Cutoff Frequency (\(f < f_c\)):**
   - The capacitor blocks most of the signal, resulting in low output amplitude.
2. **At Cutoff Frequency (\(f = f_c\)):**
   - The signal is attenuated by approximately 70% (\(-3 \, \text{dB}\)), marking the transition between blocking and passing.
3. **Above Cutoff Frequency (\(f > f_c\)):**
   - Signals pass through with minimal attenuation.

For \(R = 10 \, \text{k}\Omega\) and \(C = 0.1 \, \mu\text{F}\), the cutoff frequency is:
\[
f_c = \frac{1}{2 \pi R C} \approx 159 \, \text{Hz}
\]

- Below 159 Hz: Output appears flat (no voltage across the resistor).
- Around 159 Hz: Output voltage starts increasing, with some attenuation and phase shift.
- Above 159 Hz: Output closely follows the input sine wave.

The difference in the scales of the input and output signals indicates that the RC high-pass filter is attenuating the input signal at 100 Hz, which is below the filter's cutoff frequency (\(f_c\)).
