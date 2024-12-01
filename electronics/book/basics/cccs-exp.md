Here’s a simple experiment to demonstrate a **Current-Controlled Current Source (CCCS)** using analog components such as transistors.

### **Objective**
To design and observe the behavior of a Current-Controlled Current Source (CCCS), where the output current depends linearly on the input current.

### **Components**
1. **BJT Transistors** (e.g., 2N3904 or BC547, NPN type) – 2 units.
2. **Resistors**:
   - \( R_1 = 1 \, \text{k}\Omega \) (base bias resistor for input transistor).
   - \( R_2 = 1 \, \text{k}\Omega \) (collector resistor for output transistor).
3. **Power Supply** (\( V_{\text{CC}} \)) – +12V DC.
4. **Current Source** (\( I_{\text{in}} \)) – a variable current source (can be simulated using a voltage source and a series resistor).
5. **Multimeter** – to measure the output current (\( I_{\text{out}} \)).
6. Breadboard and connecting wires.

### **Circuit Design**
1. Use one transistor to sense the input current (\( I_{\text{in}} \)) and generate a base current for the second transistor.
2. The second transistor acts as the output stage, replicating the input current at its collector.

### **Circuit Diagram**
```
         V_CC (+12V)
             |
             R2
             |
             +---------> I_out (Output Current)
             |
            C
           Q2 (NPN)
            E
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

1. **Input Current (\( I_{\text{in}} \))**:
   - The input current is applied to the emitter of the first transistor (\( Q_1 \)) through resistor \( R_1 \).
   - \( Q_1 \) operates in the active region, converting the emitter current into a proportional collector current.

2. **Output Current (\( I_{\text{out}} \))**:
   - The collector current of \( Q_1 \) drives the base of the second transistor (\( Q_2 \)), which amplifies the current.
   - \( Q_2 \)'s collector current (\( I_{\text{out}} \)) becomes a scaled version of \( I_{\text{in}} \).

3. **Relationship Between \( I_{\text{in}} \) and \( I_{\text{out}} \)**:
   - \( I_{\text{out}} \approx \beta_2 \cdot I_{\text{in}} \), where \( \beta_2 \) is the current gain of \( Q_2 \).

### **Steps to Perform the Experiment**
1. **Assemble the Circuit**:
   - Build the circuit on a breadboard using the diagram.
   - Ensure the transistors are oriented correctly.

2. **Apply Input Current (\( I_{\text{in}} \))**:
   - Generate a controlled input current using a voltage source and a series resistor.

3. **Measure Output Current (\( I_{\text{out}} \))**:
   - Use a multimeter to measure the output current at the collector of \( Q_2 \).

4. **Vary \( I_{\text{in}} \)**:
   - Adjust the input current in steps (e.g., 0.1mA, 0.2mA, up to 1mA).
   - Record the corresponding \( I_{\text{out}} \) values.

### **Results**
- The output current (\( I_{\text{out}} \)) will increase linearly with the input current (\( I_{\text{in}} \)).
- The relationship depends on the current gain (\( \beta \)) of the transistors:
  \[
  I_{\text{out}} \approx \beta_2 \cdot I_{\text{in}}
  \]
  For instance:
  - If \( \beta_2 = 100 \) and \( I_{\text{in}} = 0.1 \, \text{mA} \), \( I_{\text{out}} = 10 \, \text{mA} \).

### **Applications**
1. Demonstrates the principle of a Current-Controlled Current Source.
2. Useful for understanding transistor operation and current mirrors.
3. Foundational for analog circuits like current amplifiers and feedback systems.

### **Advantages**
- Uses only analog components (transistors and resistors).
- Provides hands-on experience with current-controlled sources.

This experiment models a CCCS, showing how an input current can control and replicate an output current in analog circuits.
