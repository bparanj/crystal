A high-pass filter allows higher frequencies to pass through while attenuating lower frequencies. You can design a simple RC high-pass filter in Tinkercad to demonstrate this concept by observing how it blocks low frequencies and allows high frequencies.

### Components:

1. AC Voltage Source: Set to generate various frequencies (e.g., a sine wave).
2. Resistor: 1 kΩ.
3. Capacitor: 0.1 µF.
4. Oscilloscope: To observe the input and output waveforms.

### Circuit Setup:

1. Create the RC High-Pass Filter:
   - Connect one terminal of the AC source to the capacitor.
   - Connect the other terminal of the capacitor to the resistor.
   - Connect the other end of the resistor to ground.

2. Output Point:
   - The output is taken across the resistor. Connect the oscilloscope probe here to observe the output signal.
   - Also, place another oscilloscope probe across the AC source to observe the input signal for comparison.

3. Set Up the Oscilloscope:
   - Connect the first oscilloscope probe to the input (AC source) and the second probe to the output (across the resistor).
   - This setup allows you to observe how the input and output signals compare at different frequencies.

### Experiment Steps:

1. Run the Simulation:
   - Start the Tinkercad simulation.
   - Set the AC source to a low frequency, such as 10 Hz, to observe how the circuit behaves at lower frequencies.

2. Observing Low-Frequency Response:
   - With a low-frequency input, check the oscilloscope to see the output across the resistor.
   - Expected Outcome: At low frequencies, the output signal will be much weaker or nearly zero. This is because the capacitor’s impedance is high at low frequencies, blocking them from passing through to the resistor.

3. Increase the Frequency:
   - Gradually increase the frequency of the AC source to 1 kHz and then higher (e.g., 10 kHz).
   - Expected Outcome: As the frequency increases, the output signal amplitude should increase. This is because the capacitor’s impedance decreases at higher frequencies, allowing more of the input signal to pass through to the output.

4. Calculate the Cutoff Frequency:
   - The cutoff frequency \( f_c \) of an RC high-pass filter is given by:
     \[
     f_c = \frac{1}{2\pi RC}
     \]
   - For a 1 kΩ resistor and a 0.1 µF capacitor, the cutoff frequency is approximately 1.59 kHz. Above this frequency, signals pass through with minimal attenuation; below this frequency, signals are attenuated.

5. Test at the Cutoff Frequency:
   - Set the AC source frequency near the cutoff frequency (around 1.6 kHz).
   - Expected Outcome: At the cutoff frequency, the output signal amplitude should be approximately 70% of the input signal amplitude, indicating the point where the filter begins to pass higher frequencies more effectively.

High-Pass Filter Behavior: This RC circuit acts as a high-pass filter because the capacitor blocks low frequencies by presenting high impedance at those frequencies, while allowing high frequencies to pass with less impedance.

Cutoff Frequency: The cutoff frequency is where the filter transitions between attenuating low frequencies and allowing high frequencies. Frequencies above this point pass with minimal attenuation, while frequencies below are increasingly blocked.

This experiment demonstrates how an RC high-pass filter selectively allows higher frequencies while attenuating lower ones, which is useful in applications like audio signal processing and removing unwanted low-frequency noise from signals.
