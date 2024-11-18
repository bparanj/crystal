### **Diode Circuit: Parallel Diode Limiter (Clipping Circuit)**

A **Parallel Diode Limiter**, or Clipping Circuit, restricts the amplitude of an input signal by "clipping" the portions of the waveform that exceed a certain threshold. The diodes are connected in parallel with the load and conduct only when the input voltage surpasses a specific level.

---

### Concepts

1. **Clipping Behavior**:
   - When the input voltage exceeds the diode's forward voltage (\( V_f \)), the diode conducts, effectively "clipping" the voltage at that threshold.

2. **Bidirectional Clipping**:
   - By using two diodes in opposite orientations, the circuit can clip both the positive and negative peaks of an input signal.

3. **Applications**:
   - Signal protection.
   - Wave shaping in communication and audio systems.
   - Preventing overvoltage in sensitive circuits.

---

### Experiment

#### **Objective**:
To design and simulate a **Parallel Diode Limiter Circuit** and observe its ability to clip the input signal at specific voltage thresholds.

---

#### **Components**:
1. **2 Diodes** (e.g., 1N4007).
2. **Resistor** (\( R = 1k\Omega \), simulating the load).
3. **AC Voltage Source** (\( V_{in} = \pm 10V, 1kHz \)).
4. **Oscilloscope** (to visualize input and output waveforms).
5. **Breadboard** and wires.

---

### **Circuit Connections**:

1. **Input Signal**:
   - Connect the AC voltage source to one end of the resistor (\( R \)).

2. **Parallel Diodes**:
   - Connect the cathode of the first diode (\( D_1 \)) to the AC source.
   - Connect the anode of the second diode (\( D_2 \)) to the AC source.
   - Connect the other ends of \( D_1 \) (anode) and \( D_2 \) (cathode) to the other end of the resistor.

3. **Output Signal**:
   - Measure the voltage across the resistor to observe the clipped waveform.

4. **Oscilloscope**:
   - Channel 1: Connect to the AC source to monitor the input waveform.
   - Channel 2: Connect across the resistor to monitor the output waveform.

---

### Steps

#### **1. Set Up the Input Signal**:
1. Configure the AC source to generate a sinusoidal waveform (\( V_{in} = \pm 10V, 1kHz \)).
2. Use the oscilloscope to monitor the input signal on Channel 1.

#### **2. Observe Clipping Behavior**:
1. Monitor the output signal (\( V_{out} \)) across the resistor using Channel 2 of the oscilloscope.
2. Note that the output voltage is clipped at \( \pm 0.7V \), corresponding to the forward voltage of the diodes.

#### **3. Adjust Clipping Levels**:
1. Add small DC voltage sources (\( V_{offset} \)) in series with each diode.
   - Connect a \( +2V \) source in series with \( D_1 \).
   - Connect a \( -2V \) source in series with \( D_2 \).
2. Observe:
   - The clipping levels shift to \( \pm 2.7V \) (diode threshold \( \pm 0.7V \) plus the offset).

---

### Results

1. **Without Offset**:
   - The input signal (\( \pm 10V \)) is clipped at \( \pm 0.7V \), the forward voltage of the diodes.
   - The output waveform shows flattened peaks.

2. **With Offset**:
   - Adding \( \pm 2V \) offsets shifts the clipping thresholds to \( \pm 2.7V \).
   - The output waveform clips at the new thresholds.

3. **Symmetric Clipping**:
   - Both positive and negative peaks of the waveform are clipped symmetrically.

---

### Insights

1. **Voltage Threshold Control**:
   - The clipping levels are determined by the diodes’ forward voltage (\( V_f \)) and any added offset voltages.

2. **Waveform Shaping**:
   - The circuit can shape or limit signal amplitude, making it useful in signal processing and protection applications.

3. **Applications**:
   - Preventing overvoltage conditions in sensitive circuits.
   - Shaping signals for communication or audio systems.

---

### Simulation
In **Tinkercad**, you can:
1. Build the circuit using the described components.
2. Use the oscilloscope to observe the input and output waveforms.
3. Experiment with adding offset voltage sources to change the clipping thresholds.
4. Compare the clipped output waveform to the unclipped input waveform, confirming the clipping behavior.

This experiment demonstrates how parallel diodes can limit the amplitude of a signal effectively and adjust the clipping thresholds as needed.
