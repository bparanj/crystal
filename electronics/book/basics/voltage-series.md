In a **series circuit**, the total voltage from the power source is distributed across the components in proportion to their resistance.

### **1. Voltage in a Series Circuit**

- The total voltage (\(V_{\text{total}}\)) is the sum of the voltages across all individual components:
  \[
  V_{\text{total}} = V_1 + V_2 + V_3 + \dots + V_n
  \]
  Where:
  - \(V_1, V_2, \dots, V_n\): Voltages across individual components.
  - \(V_{\text{total}}\): Voltage of the power source.

### **2. Relationship Between Voltage and Resistance**

- According to **Ohm’s Law**:
  \[
  V = I \cdot R
  \]
  Where:
  - \(V\): Voltage across a component.
  - \(I\): Current through the circuit.
  - \(R\): Resistance of the component.

- In a series circuit, the current is the same through all components because there is only one path for the current to flow:
  \[
  I_{\text{total}} = I_1 = I_2 = \dots = I_n
  \]

- Thus, the voltage across each component depends on its resistance:
  \[
  V_i = I_{\text{total}} \cdot R_i
  \]

### **3. Proportional Voltage Distribution**

- The voltage across a component is proportional to its resistance:
  \[
  \frac{V_1}{R_1} = \frac{V_2}{R_2} = \dots = \frac{V_n}{R_n} = I_{\text{total}}
  \]

### **4. Total Resistance in a Series Circuit**

- The total resistance (\(R_{\text{total}}\)) is the sum of all individual resistances:
  \[
  R_{\text{total}} = R_1 + R_2 + R_3 + \dots + R_n
  \]

- The total current can then be calculated as:
  \[
  I_{\text{total}} = \frac{V_{\text{total}}}{R_{\text{total}}}
  \]

- The voltage across each component is:
  \[
  V_i = I_{\text{total}} \cdot R_i = \frac{V_{\text{total}} \cdot R_i}{R_{\text{total}}}
  \]

### **5. Example Calculation**

**Setup**:
- Power source: \( V_{\text{total}} = 12 \, \text{V} \)
- Resistors: \( R_1 = 2 \, \Omega \), \( R_2 = 4 \, \Omega \), \( R_3 = 6 \, \Omega \)

**Step 1: Total Resistance**:

\[
R_{\text{total}} = R_1 + R_2 + R_3 = 2 + 4 + 6 = 12 \, \Omega
\]

**Step 2: Total Current**:

\[
I_{\text{total}} = \frac{V_{\text{total}}}{R_{\text{total}}} = \frac{12}{12} = 1 \, \text{A}
\]

**Step 3: Voltage Across Each Resistor**:

- \( V_1 = I_{\text{total}} \cdot R_1 = 1 \cdot 2 = 2 \, \text{V} \)
- \( V_2 = I_{\text{total}} \cdot R_2 = 1 \cdot 4 = 4 \, \text{V} \)
- \( V_3 = I_{\text{total}} \cdot R_3 = 1 \cdot 6 = 6 \, \text{V} \)

**Step 4: Verify**:

\[
V_{\text{total}} = V_1 + V_2 + V_3 = 2 + 4 + 6 = 12 \, \text{V}
\]

### **Points**

1. **Voltage is Divided**:
   - The total voltage is shared among the components in proportion to their resistance.
2. **Current is Constant**:
   - The same current flows through all components in a series circuit.
3. **Higher Resistance = Higher Voltage**:
   - Components with greater resistance have a larger share of the total voltage.

### **Applications**

- Voltage dividers.
- Series lighting circuits (e.g., older Christmas lights).
- Sensors with resistive elements (e.g., potentiometers).

Understanding this distribution is useful for designing and analyzing circuits effectively.
