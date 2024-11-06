A negative clamper circuit shifts the entire AC waveform downward, "clamping" the highest point of the signal to a lower voltage level, typically near zero or a set negative voltage. This experiment in Tinkercad will help you understand how a negative clamper works.

### Components:

1. AC Voltage Source: To provide an AC signal.
2. Diode: Standard diode (e.g., 1N4148 or 1N4007).
3. Capacitor: 10 µF capacitor (or any small value capacitor).
4. Resistor: 1 kΩ resistor.
5. Oscilloscope: To observe the input and output waveforms.
6. DC Power Supply (optional): To set a specific clamping voltage.

### Circuit Setup:

1. Connect the AC Source:
   - Connect one terminal of the AC source to the input of the circuit.
   - Connect the other terminal of the AC source to ground.

2. Add the Diode and Capacitor for Clamping:
   - Place the diode in series with the AC source, with the cathode connected to the AC source and the anode connected to the capacitor.
   - Connect the other end of the capacitor to ground.
   - This orientation allows the diode to conduct during the positive half of the AC cycle, charging the capacitor and clamping the signal.

3. Add the Resistor for Load:
   - Connect a 1 kΩ resistor in parallel with the capacitor. This resistor provides a discharge path for the capacitor, stabilizing the output.

4. Set Up the Oscilloscope:
   - Connect the oscilloscope probes to observe the input and output voltages.
   - Place one probe at the input (before the diode) and the other probe at the output (across the capacitor and resistor).

### Optional: Adding a DC Power Supply for Specific Clamping Level

If you want to clamp the signal at a set negative voltage (e.g., -5V), add a small DC power supply in series with the diode, with the positive terminal connected to the anode of the diode and the negative terminal to ground.

### Steps:

1. Run the Simulation:
   - Start the simulation in Tinkercad.
   - Set the AC source to a small amplitude, like 5V peak-to-peak, with a moderate frequency (e.g., 50 Hz) to easily observe the waveform.

2. Observe the Oscilloscope Readings:
   - Observe the input waveform on one channel of the oscilloscope and the output waveform on the other.
   - Expected Outcome: On the output waveform, you should see the entire AC signal shifted downward, with the highest point clamped near 0V (or the set negative DC level, if added). The waveform will be centered around a negative voltage, rather than oscillating symmetrically around 0V.

3. Adjusting Clamping Level (Optional):
   - If you included the optional DC power supply, adjust the voltage to change the clamping level. Increasing the DC voltage will clamp the signal at a lower (more negative) level.

Diode Action:

During the positive half of the AC cycle, the diode becomes forward-biased and conducts, allowing the capacitor to charge. During the negative half, the diode is reverse-biased, and the capacitor holds its charge, effectively shifting the waveform downward.

Clamping Effect:

The circuit "clamps" the maximum voltage of the AC waveform to approximately 0V (or a set negative voltage), shifting the entire signal down.

This experiment demonstrates how a negative clamper shifts an AC signal to create a negative offset, useful in applications like signal level adjustment and DC restoration.
