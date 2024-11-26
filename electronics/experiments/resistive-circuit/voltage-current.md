PENDING

See Resistor V-I Curve in personal account. 

### **Voltage and Current in Phase in a Resistor Circuit**

In a resistive circuit, the voltage and current are in phase. The voltage and current waveforms reach their peaks and zero crossings simultaneously. This can be demonstrated using an AC voltage source and an oscilloscope.

To show that the voltage and current are in phase in a resistor-only AC circuit.

### **Components**:

1. **Resistor** (\( R = 1k\Omega \)).
2. **AC Voltage Source** (\( V_{AC} = 10V_{rms}, 1kHz \)).
3. **Oscilloscope** (dual-channel).
4. **Breadboard** and wires.
5. **Current Probe** or a voltage measurement across a small shunt resistor to infer current.

### **Circuit**:

   - Connect the AC voltage source (\( V_{AC} \)) across the resistor.

   - Connect **Channel 1** across the resistor to measure the voltage (\( V_R \)).
   - Connect **Channel 2** across a small shunt resistor (\( R_s = 1\Omega \)) in series with \( R \), or use a current probe to measure current.

### **Steps**:

   - Set the AC voltage source to \( 10V_{rms}, 1kHz \).

   - Use Channel 1 to observe the voltage across \( R \).
   - Use Channel 2 to observe the current through \( R \) (proportional to voltage across \( R_s \) if using a shunt resistor).

   - Check the waveforms on the oscilloscope.
   - Note that the peaks and zero crossings of voltage and current waveforms occur simultaneously.

   - Use the oscilloscope’s measurement function to confirm that the phase difference between the voltage and current waveforms is \( 0^\circ \).

### ** Results**:

- The voltage and current waveforms will align perfectly, confirming that they are in phase.
- The phase difference displayed on the oscilloscope will be \( 0^\circ \).

- In a resistive circuit, the voltage and current are in phase because the resistor does not store energy but dissipates it as heat.
- This behavior contrasts with inductors and capacitors, which introduce phase shifts due to energy storage.

This simple experiment effectively demonstrates the in-phase relationship between voltage and current in a resistor-only circuit.

To demonstrate that voltage and current are in phase in Tinkercad, follow these **modifications** since Tinkercad doesn’t support direct current measurement or phase analysis natively:

### **Modified Steps**:

1. **Use a Shunt Resistor for Current Measurement**:
   - Place a small shunt resistor (\( R_s = 1\Omega \)) in series with the main resistor (\( R \)).
   - The voltage across \( R_s \) will be proportional to the current (\( I = \frac{V_{R_s}}{R_s} \)).

2. **Oscilloscope Setup**:
   - Connect **Channel 1** across the main resistor (\( R \)) to measure voltage.
   - Connect **Channel 2** across the shunt resistor (\( R_s \)) to measure the voltage proportional to the current.

3. **Set Up the AC Source**:
   - Use an AC voltage source (\( V_{AC} \)) with a sinusoidal waveform (e.g., \( 10V_{rms}, 1kHz \)).

4. **Visualize Waveforms**:
   - Observe the waveforms for \( V_R \) (Channel 1) and \( V_{R_s} \) (Channel 2).
   - Note that the two waveforms will align perfectly, showing no phase difference.

5. **Verify Phase Relationship**:
   - Ensure the peaks and zero crossings of both waveforms occur simultaneously, demonstrating that voltage and current are in phase.

### **Additional Tips**:

- Tinkercad doesn’t have direct phase measurement tools, so the alignment of waveforms serves as the visual evidence for the in-phase relationship.
- Use appropriate oscilloscope time and voltage settings to clearly observe the sinusoidal waveforms.

This modification allows Tinkercad to simulate the in-phase behavior of voltage and current in a resistive circuit.
