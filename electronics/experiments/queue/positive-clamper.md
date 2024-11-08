A positive clamper circuit shifts the entire waveform of an AC signal upward, clamping the lowest point of the signal to a higher voltage level (usually near zero or a set positive voltage).

This experiment in Tinkercad demonstrates how a positive clamper works.

### Components:

1. AC Voltage Source: To provide an AC signal.
2. Diode: Standard diode (e.g., 1N4148 or 1N4007).
3. Capacitor: 10 µF capacitor (or any small value capacitor).
4. Resistor: 1 kΩ resistor.
5. Oscilloscope: To observe the input and output waveforms.
6. DC Power Supply (optional): To set a specific clamping voltage.

### Setup:

1. Connect the AC Source:
   - Connect one terminal of the AC source to the input point of the circuit.
   - Connect the other terminal of the AC source to ground.

2. Add the Diode and Capacitor for Clamping:
   - Connect the diode in series with the AC source, with the anode connected to the AC source and the cathode connected to the capacitor.
   - Place the capacitor in parallel with the resistor. The other end of the capacitor should be connected to ground.
   - This configuration allows the circuit to clamp the waveform to a positive voltage.

3. Add the Resistor for Load:
   - Connect a 1 kΩ resistor in parallel with the capacitor. This resistor creates a discharge path for the capacitor and stabilizes the output.

4. Set Up the Oscilloscope:
   - Connect the oscilloscope probes to observe the input and output voltages.
   - Place one probe at the input (before the diode) and the other probe at the output (across the capacitor and resistor).

### Optional: Adding a DC Power Supply for Specific Clamping Level

If you want to clamp the signal at a set positive voltage (e.g., +5V), add a small DC power supply in series with the diode, between the anode of the diode and the AC source.

### Steps:

1. Run the Simulation:
   - Start the simulation in Tinkercad.
   - Set the AC source to a small amplitude, like 5V peak-to-peak, with a moderate frequency (e.g., 50 Hz) for easy observation.

2. Observe the Oscilloscope Readings:
   - Observe the input waveform on one channel of the oscilloscope and the output waveform on the other.
   - Expected Outcome: You should see the entire AC waveform shifted upward on the output, with the lowest point clamped near 0V (or the positive DC offset level if added). The waveform will no longer be centered around 0V but instead around a positive voltage.

3. Adjusting Clamping Level (Optional):
   - If you added a DC power supply in series with the diode, adjust the voltage to change the clamping level. Increasing the DC voltage will shift the waveform even higher on the output.

Diode Action:

During the positive half-cycle of the AC signal, the diode becomes reverse-biased, preventing current flow and allowing the capacitor to charge up. During the negative half-cycle, the diode conducts, allowing the capacitor to maintain its charge, effectively shifting the waveform up.

Clamping Effect:

The circuit "clamps" the minimum voltage of the AC waveform to approximately 0V (or the DC offset level), shifting the entire signal upward.

This experiment demonstrates how a positive clamper shifts an AC signal to create a positive offset, useful in applications like DC restoration and signal level adjustment.
