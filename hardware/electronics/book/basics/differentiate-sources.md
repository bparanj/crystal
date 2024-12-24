A **voltage source** and a **current source** are two fundamental types of electrical sources, each defined by the quantity they provide and how they behave in a circuit.

### **1. Definition**

- **Voltage Source**:

  - A device that delivers a constant voltage regardless of the current drawn by the load.
  - Examples: Batteries, AC power supplies.

- **Current Source**:

  - A device that delivers a constant current regardless of the voltage across it.
  - Examples: Current regulators, transistor circuits configured as current sources.

### **2. Symbol**

- **Voltage Source**:

  - Represented in circuit diagrams as:
    - DC source: \( \bigoplus\bigominus \)
    - AC source: \( \sim \)

- **Current Source**:

  - Represented as:
    - \( \rightarrow \) (with a current arrow).

### **3. Output Behavior**

- **Voltage Source**:

  - Maintains a fixed voltage output.
  - The current varies depending on the load connected to it.

- **Current Source**:

  - Maintains a fixed current output.
  - The voltage varies depending on the load impedance.

### **4. Ideal Characteristics**

- **Voltage Source**:
  - **Ideal Voltage Source**: Has zero internal resistance.
    - Output voltage remains constant for any load current.
  - **Real Voltage Source**: Includes some internal resistance, causing the voltage to drop under high current loads.

- **Current Source**:
  - **Ideal Current Source**: Has infinite internal resistance.
    - Output current remains constant regardless of the load voltage.
  - **Real Current Source**: Includes a finite internal resistance, causing the current to vary slightly with load voltage.

### **5. Example Behavior**

- **Voltage Source**:
  - A 12V battery will maintain 12V across its terminals regardless of whether it powers a light bulb or a resistor, up to its capacity.

- **Current Source**:
  - A 2A current source will supply 2A to any load, whether it's a high-impedance circuit or a low-impedance circuit, within its voltage compliance range.

### **6. Applications**

- **Voltage Source**:

  - Commonly used to power electronic devices and circuits where a stable voltage is needed.
  - Examples: Power supplies, batteries, and AC mains.

- **Current Source**:

  - Used in applications requiring constant current, such as LED drivers, biasing transistors, and charging batteries.
  - Examples: Constant-current chargers, transistor current mirrors.

### **7. Mathematical Representation**

- **Voltage Source**:

  - Defined by:
    \[
    V = \text{constant}
    \]

- **Current Source**:

  - Defined by:
    \[
    I = \text{constant}
    \]

### **Comparison**

| **Aspect**             | **Voltage Source**                 | **Current Source**                 |
|-------------------------|-------------------------------------|-------------------------------------|
| **Primary Output**      | Constant voltage                   | Constant current                   |
| **Internal Resistance** | Ideally zero                       | Ideally infinite                   |
| **Current Behavior**    | Varies with load resistance         | Fixed, regardless of load          |
| **Voltage Behavior**    | Fixed, regardless of load           | Varies with load resistance         |
| **Symbol**              | \( \bigoplus\bigominus \), \( \sim \) | \( \rightarrow \) (current arrow)  |
| **Applications**        | Power supply for devices           | LED drivers, transistor biasing    |

a **voltage source** focuses on maintaining a steady voltage, while a **current source** ensures a steady current. Each has specific use cases based on the requirements of the circuit.
