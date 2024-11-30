a simple experiment to demonstrate a **Voltage-Controlled Current Source (VCCS)** using basic analog components like a transistor.

### **Objective**
To build and observe the behavior of a Voltage-Controlled Current Source (VCCS), where the output current is proportional to the input voltage.

### **Components Needed**
1. **BJT Transistor** (e.g., 2N3904 or BC547, NPN type)
2. **Resistors**:
   - \( R_1 = 10 \, \text{k}\Omega \) (base bias resistor)
   - \( R_2 = 1 \, \text{k}\Omega \) (load resistor)
3. **Voltage Input Source** (\( V_{\text{in}} \)) – range: 0–5V.
4. **Power Supply** (\( V_{\text{CC}} \)) – +12V DC.
5. **Multimeter** – to measure the output current (\( I_{\text{out}} \)).
6. Breadboard and connecting wires.

### **Circuit Design**
1. The transistor operates in the **active region**, where the base-emitter junction is forward-biased, and the collector-emitter junction is reverse-biased.
2. The input voltage (\( V_{\text{in}} \)) applied to the base through \( R_1 \) controls the current flowing into the base.
3. The output current (\( I_{\text{out}} \)) is measured through the collector terminal, and its value is determined by the input voltage.

### **Circuit Diagram**
```
         V_CC (+12V)
             |
             |
             R2
             |
             +---------> I_out (Output Current)
             |
            C
           Q1 (NPN)
            E
             |
            R1
             |
          V_in (Input Voltage)
             |
            GND
```

### **Working Principle**
1. **Input Voltage (\( V_{\text{in}} \))**:
   - The base-emitter voltage (\( V_{\text{BE}} \)) controls the base current (\( I_B \)).
2. **Transistor Action**:
   - The collector current (\( I_C \)) is proportional to the base current (\( I_B \)), as \( I_C = \beta I_B \), where \( \beta \) is the current gain of the transistor.
3. **Output Current**:
   - The load resistor (\( R_2 \)) is connected to the collector, and the output current (\( I_{\text{out}} \)) flows through it.
   - By controlling \( V_{\text{in}} \), you control \( I_B \), and thus \( I_{\text{out}} \).

### **Theoretical Analysis**
1. The base current (\( I_B \)) is related to the input voltage:
   \[
   I_B = \frac{V_{\text{in}} - V_{\text{BE}}}{R_1}
   \]
   - \( V_{\text{BE}} \) is typically 0.7V for silicon BJTs.

2. The collector current (\( I_C \)) is:
   \[
   I_C = \beta I_B
   \]

3. Therefore, the output current (\( I_{\text{out}} \)) is:
   \[
   I_{\text{out}} = \beta \cdot \frac{V_{\text{in}} - V_{\text{BE}}}{R_1}
   \]

### **Steps to Perform the Experiment**
1. Assemble the circuit on a breadboard as per the diagram.
2. Connect the power supply (\( V_{\text{CC}} \)) to +12V.
3. Vary the input voltage (\( V_{\text{in}} \)) in steps (e.g., 0V, 1V, 2V, up to 5V).
4. Measure the output current (\( I_{\text{out}} \)) using a multimeter placed in series with the load resistor \( R_2 \).
5. Record the relationship between \( V_{\text{in}} \) and \( I_{\text{out}} \).

### **Expected Results**
- As \( V_{\text{in}} \) increases, the output current \( I_{\text{out}} \) will increase linearly within the active region of the transistor.
- The relationship between \( I_{\text{out}} \) and \( V_{\text{in}} \) is governed by the proportionality factor \( \beta / R_1 \).

### **Applications**
1. Demonstrating the behavior of a VCCS.
2. Practical implementation of current sources in circuits like LED drivers.
3. Modeling controlled sources in analog circuits.

### **Advantages**
- Simple to implement with basic analog components.
- Provides a hands-on understanding of controlled current sources.

This experiment effectively demonstrates how a VCCS works using a transistor as the primary control element, linking the input voltage to the output current in a predictable manner.
