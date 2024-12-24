A experiment to demonstrate phase shift in a capacitor.

To observe the phase shift between voltage across a capacitor and the input signal from an AC source, highlighting the concept of a capacitor’s phase behavior in an AC circuit.

### Components

- AC Voltage Source (simulated using Tinkercad’s function generator)
- Capacitor (e.g., 10 µF non-polarized)
- Resistor (e.g., 1 kΩ)
- Oscilloscope

### Setup

   - Place the resistor and capacitor in series on the breadboard.
   - Connect the function generator to one end of the resistor (input side).
   - Connect the other end of the resistor to the capacitor.
   - Connect the other end of the capacitor to the ground terminal of the function generator.

   - Connect an oscilloscope probe across the resistor (this will show the input voltage waveform).
   - Connect a second oscilloscope probe across the capacitor (this will show the output waveform, which should have a phase shift relative to the input).

   - Set the function generator to output a sine wave with a frequency of around 1 kHz and an amplitude of 5V peak-to-peak.

   - Run the simulation and observe both waveforms on the oscilloscope:
     - The voltage across the resistor (input) shows the current through the circuit.
     - The voltage across the capacitor (output) shows the capacitor’s voltage response.

   - Compare the two waveforms on the oscilloscope.
   - You should observe that the voltage across the capacitor lags the voltage across the resistor (input signal) by up to 90° depending on the frequency.
   - This lag demonstrates the phase shift caused by the capacitor, which results from the capacitor's delay in charging and discharging relative to the changing AC signal.

### Explanation of Phase Shift

In an RC circuit:

- The current (and voltage across the resistor) is in phase with the input signal.
- The voltage across the capacitor lags the current, creating a phase difference. This occurs because the capacitor takes time to charge and discharge, introducing a delay.

This experiment demonstrates the phase shift in an RC circuit using minimal components, with the capacitor creating a lagging phase shift in response to an AC signal. Adjusting the frequency of the AC source in Tinkercad allows you to see how the phase shift changes, illustrating the frequency-dependent nature of capacitive phase shifts.