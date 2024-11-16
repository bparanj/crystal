### **Inductive Voltage-to-Current (V-to-I) Integrator**

An **Inductive Voltage-to-Current (V-to-I) Integrator** is a circuit that converts an input voltage signal into a current proportional to the **integral** of the voltage. This is achieved using an inductor, which inherently integrates the input voltage over time due to its relationship with current:

\[
V_L = L \cdot \frac{dI}{dt} \implies I(t) = \frac{1}{L} \int V_{in} \, dt
\]

---

### **Key Concepts**:

1. **Inductive Behavior**:
   - The current through an inductor is proportional to the integral of the voltage applied across it.
   - Slowly varying or constant input voltages result in a gradual increase in current.

2. **Output Current**:
   - The current through the inductor is given by:
     \[
     I(t) = \frac{1}{L} \int V_{in}(t) \, dt
     \]
     Where:
     - \(L\): Inductance in henries.
     - \(V_{in}(t)\): Input voltage as a function of time.

3. **Applications**:
   - Waveform shaping (e.g., converting step signals into ramp signals).
   - Signal integration in processing circuits.

---

### **Experiment Design for Tinkercad**:

#### **Objective**:
To demonstrate the behavior of an **Inductive V-to-I Integrator** and observe the current response to a time-varying voltage input.

#### **Components**:
1. **AC Voltage Source** (\( V_{in} = 5V_{peak}, f = 1kHz \)).
2. **Inductor** (\( L = 10mH \)).
3. **Resistor** (\( R = 1k\Omega \)) for measuring current as voltage.
4. **Oscilloscope** (to observe input voltage and output current waveform).
5. **Breadboard** and wires.

---

### **Circuit Configuration**:

1. **Input Voltage**:
   - Connect the AC voltage source (\( V_{in} \)) to one terminal of the inductor (\( L \)).

2. **Current Measurement**:
   - Connect the other terminal of the inductor to a series resistor (\( R \)).

3. **Load Resistor**:
   - Use \( R \) to convert the current into a proportional voltage (\( V_R = I \cdot R \)) for observation.

4. **Oscilloscope Connections**:
   - Channel 1: Monitor the input voltage (\( V_{in} \)).
   - Channel 2: Monitor the voltage across \( R \), which represents the output current.

---

### **Steps to Perform**:

1. **Set Input Signal**:
   - Configure the AC voltage source to generate a sine wave:
     - Amplitude: \( 5V_{peak} \).
     - Frequency: \( 1kHz \).

2. **Measure Output Current**:
   - Observe the current waveform (\( V_R = I \cdot R \)) on Channel 2 of the oscilloscope.

3. **Change Input Frequency**:
   - Increase the frequency of \( V_{in} \) (e.g., \( 2kHz, 5kHz \)) and observe how the output current waveform changes.

4. **Change Inductance**:
   - Replace \( L \) with \( 5mH, 20mH \) inductors and observe how the integration effect varies.

---

### **Expected Results**:

1. **Current Proportional to Integral**:
   - The current waveform (\( I(t) \)) will lag the input voltage (\( V_{in} \)) by 90°, representing the integration.

2. **Frequency Dependence**:
   - At lower frequencies, the output current changes more slowly due to slower voltage variations.
   - At higher frequencies, the current responds more rapidly to the changing voltage.

3. **Inductance Effect**:
   - Larger inductors reduce the rate of current change (\( \Delta I \)) for the same input voltage.

---

### **Key Insights**:

1. **Integration Behavior**:
   - The circuit demonstrates how inductors naturally integrate input voltages over time, converting them into proportional currents.

2. **Applications**:
   - Useful in waveform generation, energy storage, and signal processing where integration is required.

3. **Impedance Matching**:
   - Ensure that the resistor \( R \) does not significantly affect the circuit’s behavior or loading.

---

This experiment can be implemented in **Tinkercad**, where you can observe the current waveform corresponding to the integrated voltage using the oscilloscope and verify the effects of input frequency and inductance value.
