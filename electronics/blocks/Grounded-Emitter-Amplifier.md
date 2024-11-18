### **Transistor Circuit: Grounded-Emitter Amplifier**

The **Grounded-Emitter Amplifier**, also known as the **Common Emitter Amplifier**, is a basic transistor amplifier configuration. It provides **voltage gain** and is widely used in audio amplification and signal processing. The "grounded-emitter" designation means the emitter is connected to ground, often through a small resistor, to provide bias stability.

---

### **Key Concepts**:

1. **Voltage Gain**:
   - The grounded-emitter amplifier offers significant voltage gain.
   - Gain is determined by the ratio of the collector resistor (\( R_C \)) to the emitter resistor (\( R_E \)).

2. **Input and Output Impedance**:
   - Moderate input impedance, primarily determined by the base resistor.
   - Low output impedance, suitable for driving loads.

3. **Phase Inversion**:
   - The output voltage is inverted relative to the input voltage.

4. **Applications**:
   - Signal amplification.
   - Audio and radio frequency circuits.

---

### **Experiment Design for Tinkercad**:

#### **Objective**:
To design and simulate a **Grounded-Emitter Amplifier** using a transistor and observe its voltage gain and phase inversion.

---

#### **Components**:
1. **NPN Transistor** (e.g., 2N2222).
2. **Resistors**:
   - \( R_B = 100k\Omega \) (base resistor for biasing).
   - \( R_C = 1k\Omega \) (collector resistor).
   - \( R_E = 470\Omega \) (emitter resistor).
3. **Capacitors**:
   - \( C_{in} = 10\mu F \) (input coupling capacitor).
   - \( C_{out} = 10\mu F \) (output coupling capacitor).
4. **DC Voltage Source** (\( V_{CC} = 12V \)).
5. **AC Voltage Source** (\( V_{in} = 10mV_{peak}, 1kHz \)).
6. **Oscilloscope** (to observe input and output waveforms).
7. **Breadboard** and wires.

---

### **Circuit Connections**:

1. **Power Supply**:
   - Connect the positive terminal of \( V_{CC} \) to one end of \( R_C \).
   - Connect the other end of \( R_C \) to the transistor's collector.

2. **Transistor Configuration**:
   - Connect the transistor’s emitter to ground through \( R_E \).

3. **Input Signal**:
   - Connect \( V_{in} \) to \( C_{in} \).
   - Connect the other end of \( C_{in} \) to the base of the transistor through \( R_B \).

4. **Output Signal**:
   - Connect \( C_{out} \) to the transistor’s collector to couple the amplified signal.
   - Connect the other end of \( C_{out} \) to the oscilloscope for output waveform observation.

5. **Oscilloscope**:
   - Channel 1: Connect to the input signal (\( V_{in} \)).
   - Channel 2: Connect to the output signal (\( V_{out} \)).

---

### **Steps to Perform**:

#### **1. Apply Input Signal**:
1. Set \( V_{in} = 10mV_{peak}, 1kHz \) using the AC voltage source.
2. Observe:
   - Channel 1 displays the input signal.
   - Channel 2 displays the amplified and inverted output signal.

#### **2. Measure Voltage Gain**:
1. Measure the peak-to-peak voltages of the input (\( V_{in(pp)} \)) and output (\( V_{out(pp)} \)) signals.
2. Calculate the voltage gain (\( A_v \)):
   \[
   A_v = \frac{V_{out(pp)}}{V_{in(pp)}}
   \]

#### **3. Observe Phase Inversion**:
1. Compare the input and output waveforms.
2. Confirm that the output is inverted (180° out of phase) relative to the input.

#### **4. Experiment with Component Values**:
1. Vary \( R_C \) and \( R_E \) to observe their impact on gain.
2. Increase or decrease \( C_{in} \) and \( C_{out} \) to analyze coupling effects.

---

### **Expected Results**:

1. **Voltage Gain**:
   - The output signal is amplified relative to the input, with gain approximately:
     \[
     A_v \approx \frac{R_C}{R_E}
     \]

2. **Phase Inversion**:
   - The output signal is 180° out of phase with the input signal.

3. **Effect of Components**:
   - Increasing \( R_C \) increases gain.
   - Increasing \( R_E \) decreases gain but improves bias stability.

---

### **Key Insights**:

1. **Voltage Amplification**:
   - The grounded-emitter amplifier efficiently amplifies small AC signals.

2. **Phase Inversion**:
   - The output signal is inverted due to the transistor's operation.

3. **Applications**:
   - Used in preamplifiers and signal processing circuits.

---

### **Tinkercad Simulation**:
In **Tinkercad**, you can:
1. Build the described circuit using the components.
2. Use the oscilloscope to monitor the input and output signals.
3. Adjust component values (\( R_C \), \( R_E \), \( C_{in} \), \( C_{out} \)) to study their impact on gain and performance.
4. Confirm the amplifier’s gain and phase inversion through measurements and waveform analysis.

This experiment demonstrates the principles of amplification and phase inversion in a grounded-emitter configuration.
