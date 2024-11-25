A experiment to demonstrate phase shift in an inductor in Tinkercad, showing how the inductor's voltage response leads the current in an AC circuit.

To observe the phase shift between the voltage across an inductor and the current in the circuit when connected to an AC signal, highlighting the concept of inductive phase behavior.

### Components

- AC Voltage Source (simulated using Tinkercad’s function generator)
- Inductor (e.g., 10 mH)
- Resistor (e.g., 1 kΩ)
- Oscilloscope

### Setup

   - Place the resistor and inductor in series on the breadboard.
   - Connect the function generator to one end of the resistor (input side).
   - Connect the other end of the resistor to one terminal of the inductor.
   - Connect the other terminal of the inductor to the ground of the function generator.

   - Connect an oscilloscope probe across the resistor (to observe the current waveform indirectly, as current through the resistor reflects the input waveform).
   - Connect a second oscilloscope probe across the inductor (to observe the voltage across the inductor).

   - Set the function generator to output a sine wave with a frequency of around 1 kHz and an amplitude of 5V peak-to-peak.

   - Run the simulation and observe both waveforms on the oscilloscope:
     - The voltage across the resistor (input signal) represents the current through the circuit.
     - The voltage across the inductor represents the inductor’s voltage response.

   - Compare the two waveforms on the oscilloscope.
   - You should observe that the voltage across the inductor leads the voltage across the resistor (current) by up to 90°, depending on the frequency.
   - This lead in the inductor’s voltage response demonstrates the inductive phase shift in the circuit.

In an RL circuit:

- The current through the circuit (indicated by the voltage across the resistor) is in phase with the input voltage.
- The voltage across the inductor leads the current, creating a phase difference. This occurs because the inductor opposes changes in current, causing its voltage to peak before the current does.

This experiment demonstrates the phase shift in an RL circuit using minimal components, where the inductor causes the voltage to lead the current. You can adjust the AC signal frequency in Tinkercad to see how this phase shift varies, illustrating the frequency-dependent nature of inductive phase shifts.