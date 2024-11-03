A low-pass filter allows lower frequencies to pass through while attenuating higher frequencies. You can design a simple RC low-pass filter in Tinkercad to observe how it filters out high frequencies and allows low frequencies to pass.

### Components:

1. AC Voltage Source: Set to generate various frequencies (e.g., a sine wave).
2. Resistor: 1 kΩ.
3. Capacitor: 0.1 µF.
4. Oscilloscope: To observe the input and output waveforms.

### Circuit Setup:

1. Create the RC Low-Pass Filter:
   - Connect one terminal of the AC source to the resistor.
   - Connect the other end of the resistor to one terminal of the capacitor.
   - Connect the other terminal of the capacitor to ground.

2. Output Point:
   - The output is taken across the capacitor. Connect the oscilloscope probe here to observe the output signal.
   - Also, place another oscilloscope probe across the AC source to observe the input signal for comparison.

3. Set Up the Oscilloscope:
   - Connect the first oscilloscope probe to the input (AC source) and the second probe to the output (across the capacitor).
   - This setup allows you to observe how the input and output signals compare at different frequencies.

### Experiment Steps:

1. Run the Simulation:
   - Start the Tinkercad simulation.
   - Set the AC source to a high frequency, such as 10 kHz, to observe how the circuit behaves at higher frequencies.

2. Observing High-Frequency Response:
   - With a high-frequency input, check the oscilloscope to see the output across the capacitor.
   - Expected Outcome: At high frequencies, the output signal will be much weaker or nearly zero. This is because the capacitor’s impedance is low at high frequencies, causing most of the signal to bypass the output and go to ground.

3. Decrease the Frequency:
   - Gradually decrease the frequency of the AC source to around 1 kHz and then lower (e.g., 10 Hz).
   - Expected Outcome: As the frequency decreases, the output signal amplitude should increase. This is because the capacitor’s impedance increases at lower frequencies, allowing more of the input signal to pass through to the output.

4. Calculate the Cutoff Frequency:
   - The cutoff frequency \( f_c \) of an RC low-pass filter is given by:
     \[
     f_c = \frac{1}{2\pi RC}
     \]
   - For a 1 kΩ resistor and a 0.1 µF capacitor, the cutoff frequency is approximately 1.59 kHz. Below this frequency, signals pass through with minimal attenuation; above this frequency, signals are increasingly attenuated.

5. Test at the Cutoff Frequency:
   - Set the AC source frequency near the cutoff frequency (around 1.6 kHz).
   - Expected Outcome: At the cutoff frequency, the output signal amplitude should be approximately 70% of the input signal amplitude, indicating the point where the filter begins to attenuate higher frequencies.

Low-Pass Filter Behavior: This RC circuit acts as a low-pass filter because the capacitor allows low frequencies to pass while presenting low impedance to high frequencies, which causes them to be filtered out.

Cutoff Frequency: The cutoff frequency is the point where the filter transitions from passing low frequencies to attenuating high frequencies. Frequencies below this point pass with minimal attenuation, while frequencies above are increasingly blocked.

This experiment demonstrates how an RC low-pass filter selectively allows lower frequencies while attenuating higher ones, which is useful in applications like audio signal processing, smoothing DC signals, and removing high-frequency noise.
