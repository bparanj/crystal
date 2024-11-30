To demonstrate the behavior of a **Current-Controlled Voltage Source (CCVS)** using analog components, we can design a simple circuit based on a **transistor** and resistors.

### **Objective**
Build and observe a circuit where the output voltage depends linearly on an input current, demonstrating the functionality of a Current-Controlled Voltage Source (CCVS).

### **Components**
1. **BJT Transistor** (e.g., 2N3904 or BC547, NPN type).
2. **Resistors**:
   - \( R_1 = 10 \, \text{k}\Omega \) (base resistor for current control).
   - \( R_2 = 1 \, \text{k}\Omega \) (collector resistor to generate output voltage).
3. **Voltage Source** (\( V_{\text{CC}} \)) – +12V DC.
4. **Current Source** (\( I_{\text{in}} \)) – a variable current source (can be simulated using a DC voltage source and a series resistor).
5. **Multimeter** – to measure the output voltage (\( V_{\text{out}} \)).
6. Breadboard and connecting wires.

### **Circuit Design**
1. **Current Control**:
   - The base current (\( I_B \)) of the transistor is set by the input current (\( I_{\text{in}} \)).
   - The input current is fed into the base of the transistor through \( R_1 \).
2. **Voltage Output**:
   - The output voltage is taken from the collector of the transistor and is proportional to the collector current (\( I_C \)).

### **Circuit Diagram**
```
          V_CC (+12V)
             |
             R2
             |
             +---------> V_out (Output Voltage)
             |
            C
           Q1 (NPN)
            E
             |
             R1
             |
         I_in (Input Current)
             |
            GND
```

### **Working Principle**
1. **Current Control**:
   - The input current (\( I_{\text{in}} \)) is applied to the base of the transistor via \( R_1 \).
   - The base-emitter voltage (\( V_{\text{BE}} \)) ensures the transistor operates in the active region.

2. **Voltage Generation**:
   - The transistor amplifies the base current (\( I_B \)) to produce a collector current (\( I_C \)).
   - The voltage drop across the collector resistor (\( R_2 \)) is proportional to \( I_C \):
     \[
     V_{\text{out}} = I_C \cdot R_2
     \]

3. **Relationship Between \( V_{\text{out}} \) and \( I_{\text{in}} \)**:
   - Using the transistor's current gain (\( \beta \)):
     \[
     I_C = \beta \cdot I_B
     \]
     Since \( I_B \approx I_{\text{in}} \) (neglecting base-emitter leakage current):
     \[
     V_{\text{out}} = \beta \cdot I_{\text{in}} \cdot R_2
     \]

### **Steps to Perform the Experiment**
1. **Assemble the Circuit**:
   - Connect the components on a breadboard as per the circuit diagram.
   - Ensure the transistor’s base is connected to \( I_{\text{in}} \) via \( R_1 \).

2. **Apply Input Current (\( I_{\text{in}} \))**:
   - Generate a controlled input current using a voltage source in series with a resistor, or a dedicated current source.

3. **Measure Output Voltage (\( V_{\text{out}} \))**:
   - Use a multimeter to measure the output voltage at the collector with respect to ground.

4. **Vary \( I_{\text{in}} \)**:
   - Adjust the input current in steps (e.g., 0.1mA, 0.2mA, up to 1mA).
   - Record the corresponding \( V_{\text{out}} \) values.

### **Expected Results**
- The output voltage (\( V_{\text{out}} \)) will increase linearly with the input current (\( I_{\text{in}} \)).
- For example, if \( \beta = 100 \), \( R_2 = 1 \, \text{k}\Omega \):
  \[
  V_{\text{out}} = 100 \cdot I_{\text{in}} \cdot 1 \, \text{k}\Omega = 100 \cdot I_{\text{in}} \, \text{V/mA}.
  \]
  - When \( I_{\text{in}} = 0.1 \, \text{mA} \), \( V_{\text{out}} = 10 \, \text{V} \).
  - When \( I_{\text{in}} = 0.2 \, \text{mA} \), \( V_{\text{out}} = 20 \, \text{V} \), and so on.

### **Applications**
1. Demonstrates the principle of a Current-Controlled Voltage Source.
2. Useful for understanding transistor operation and current-to-voltage conversion.
3. Foundational for analog circuits like current amplifiers and feedback systems.

### **Advantages**
- Uses simple, readily available analog components.
- Provides hands-on experience with current-controlled sources.

This experiment shows how a CCVS works and how input current can control the output voltage in a predictable manner.
