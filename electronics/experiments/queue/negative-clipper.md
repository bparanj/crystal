A negative clipper circuit removes the negative portion of an AC signal, allowing only the positive portion to pass through. This simple experiment in Tinkercad demonstrates how a negative clipper works.

### Components:

1. AC Voltage Source: To provide an AC signal.
2. Diode: Standard diode (e.g., 1N4148 or 1N4007).
3. Resistor: 1 kΩ resistor.
4. Oscilloscope: To observe the input and output waveforms.
5. DC Power Supply (optional): To set a specific clipping level if desired.

### Setup:

1. Connect the AC Source:
   - Connect one terminal of the AC source to the resistor (1 kΩ).
   - Connect the other terminal of the AC source to ground.

2. Add the Diode for Clipping:
   - Place the diode in parallel with the AC source but with the opposite orientation of a positive clipper. Connect the anode of the diode to ground and the cathode to the input signal (after the resistor).
   - This orientation allows the diode to conduct only during the negative half of the AC cycle, clipping the negative portion of the waveform.

3. Set Up the Oscilloscope:
   - Connect the oscilloscope probes to observe the input and output voltages.
   - Place the first probe at the input (before the resistor) and the second probe at the output (after the diode).

### Optional: Adding a DC Power Supply for Custom Clipping Voltage

If you want to set the clipping level at a specific voltage, you can add a DC power supply in series with the diode (between the anode of the diode and ground). This will clip the signal at the DC voltage level.

### Steps:

1. Run the Simulation:
   - Start the simulation in Tinkercad.
   - Set the AC source to a small amplitude, like 5V peak-to-peak, and a moderate frequency (e.g., 50 Hz) to easily observe the waveform.

2. Observe the Oscilloscope Readings:
   - Observe the input waveform on one channel of the oscilloscope and the output waveform on the other.
   - Expected Outcome: On the output waveform, you should see the negative portion of the AC signal clipped at approximately 0V (or the level of the DC offset if added). The positive portion of the AC signal should pass through unaffected.

3. Adjusting Clipping Level (Optional):
   - If you added a DC power supply in series with the diode, adjust the voltage to see how the clipping level changes. Increasing the DC voltage will clip the signal at a lower negative level.

Diode Action:

The diode conducts during the negative half-cycle of the AC signal, grounding the negative voltage and effectively “clipping” it to 0V (or the DC offset level).

Clipping Effect:

The negative portion of the AC signal is clipped off, while the positive portion remains unaffected.

This experiment demonstrates how a negative clipper circuit limits the negative voltage of an AC signal, useful in applications where only the positive half of a signal is needed or to protect circuits from negative voltages.
