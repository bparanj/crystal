
PENDING

This is the same as 34.md. Merge and delete this document.

Checkout https://www.falstad.com/circuit/e-index.html   

Calculate the Cutoff Frequency:
   - The cutoff frequency \( f_c \) of an RC high-pass filter is given by:
     \[
     f_c = \frac{1}{2\pi RC}
     \]
   - For a 1 kΩ resistor and a 0.1 µF capacitor, the cutoff frequency is approximately 1.59 kHz. Above this frequency, signals pass through with minimal attenuation; below this frequency, signals are attenuated.

Test at the Cutoff Frequency:
   - Set the AC source frequency near the cutoff frequency (around 1.6 kHz).
   - Expected Outcome: At the cutoff frequency, the output signal amplitude should be approximately 70% of the input signal amplitude, indicating the point where the filter begins to pass higher frequencies more effectively.

High-Pass Filter Behavior:

This RC circuit acts as a high-pass filter because the capacitor blocks low frequencies by having high impedance at low frequencies, while allowing high frequencies to pass with less impedance.

Cutoff Frequency:

The cutoff frequency is where the filter transitions between attenuating low frequencies and allowing high frequencies. Frequencies above this point pass with minimal attenuation, while frequencies below are increasingly blocked.

This experiment demonstrates how an RC high-pass filter allows higher frequencies while attenuating lower ones, which is useful in applications like audio signal processing and removing unwanted low-frequency noise from signals.

Create a simple RC (Resistor-Capacitor) high-pass filter to observe how it allows high-frequency signals to pass while attenuating lower frequencies.


3. Increase Frequency: Gradually increase the frequency (e.g., 100 Hz, 500 Hz, 1 kHz, 10 kHz, etc.).
4. Record Observations: Note how the amplitude of the output signal changes relative to the input as the frequency increases.

- At low frequencies, the output signal's amplitude should be much lower than the input amplitude, indicating attenuation.
- As the frequency increases, the output amplitude should rise, approaching the input amplitude, demonstrating the high-pass filter effect.

This experiment demonstrates that an RC high-pass filter allows high-frequency signals to pass while attenuating low frequencies, illustrating the behavior of a basic high-pass filter.
