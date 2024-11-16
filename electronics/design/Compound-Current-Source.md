### **Compound Current Source**

A **Compound Current Source** is a circuit that combines multiple current sources (typically an active current source and a passive element) to achieve better performance, such as higher output impedance, better current stability, or improved linearity.

---

### **Key Features**:

1. **Improved Output Impedance**:
   - The circuit provides a high output impedance, making it behave like an ideal current source over a wide range of load conditions.

2. **Enhanced Stability**:
   - Compound designs compensate for variations in temperature, supply voltage, or load resistance.

3. **Better Linearity**:
   - Non-linearities in one current source can be countered by another element in the compound design.

---

### **Basic Types of Compound Current Sources**:

#### **1. Widlar Current Source**
   - Uses a resistor in the emitter leg of a transistor to produce a current that decreases exponentially with increased resistance.
   - **Applications**: Low-current applications and biasing.

#### **2. Wilson Current Source**
   - Combines three transistors to provide high output impedance and low sensitivity to supply voltage variations.
   - **Key Characteristics**:
     - Feedback improves current regulation.
     - High output impedance makes it nearly ideal.
   - **Applications**: Precision analog circuits and biasing in integrated circuits.

#### **3. Cascode Current Source**
   - Combines two transistors in a cascade configuration to achieve very high output impedance.
   - **Key Characteristics**:
     - Reduced Early effect improves current regulation.
     - Better frequency response compared to single-transistor current sources.
   - **Applications**: Analog amplifier stages and high-frequency circuits.

---

### **General Configuration of a Compound Current Source**:

#### **Components**:
1. **Reference Current Source**:
   - Provides a stable reference current.
   - Can be implemented with a simple resistor, transistor, or IC.

2. **Control Transistor(s)**:
   - Modulates the output current based on the reference current.
   - Arranged in configurations like cascode, Wilson, or Widlar for improved performance.

3. **Load**:
   - The device or circuit consuming the output current.

---

### **Advantages**:

1. **High Output Impedance**:
   - Reduces the impact of load resistance variations.

2. **Stable Current**:
   - Less sensitive to changes in supply voltage or temperature.

3. **Versatile**:
   - Suitable for applications ranging from analog signal processing to biasing.

---

### **Applications**:

1. **Biasing Circuits**:
   - Provides stable current for transistors in amplifiers.

2. **Analog Integrated Circuits**:
   - Precision current references and current mirrors.

3. **Power Regulation**:
   - Supplies constant current for LED drivers and other devices.

4. **Measurement Systems**:
   - Provides a stable reference current for precise sensor readings.

---

### **Key Insights**:
- Compound current sources are essential in **precision analog circuits** and **signal processing** where stable and accurate current sources are required.
- Designs like the **Wilson** and **Cascode** current sources are optimized for different performance criteria, such as high output impedance or low voltage sensitivity.


### **Experiment: Compound Current Source**

#### **Objective**:
To design and simulate a **compound current source** using a **cascode configuration** and demonstrate its high output impedance and stable current behavior.

---

### **Circuit Design: Cascode Current Source**

#### **Components**:
1. **DC Power Supply** (\( V_{supply} = 12V \))
2. **Two NPN Transistors** (e.g., 2N2222)
3. **Resistor** (\( R_{ref} = 1k\Omega \))
4. **Load Resistor** (\( R_{load} = 1k\Omega \))
5. **Multimeter** (to measure output current)
6. **Breadboard** and wires

---

### **Circuit Configuration**:

1. **Reference Current**:
   - Use the first transistor (Q1) and resistor (\( R_{ref} \)) to set a reference current:
     \[
     I_{ref} = \frac{V_{supply} - V_{BE}}{R_{ref}}
     \]
     Where \( V_{BE} \approx 0.7V \).

2. **Cascode Stage**:
   - Use the second transistor (Q2) as the cascode stage to enhance output impedance:
     - Connect the collector of Q1 to the emitter of Q2.
     - Connect the collector of Q2 to \( V_{supply} \).

3. **Load Resistor**:
   - Place \( R_{load} \) between the emitter of Q1 and ground to simulate the circuit's load.

4. **Current Measurement**:
   - Place a multimeter in series with \( R_{load} \) to measure the output current.

---

### **Steps to Perform**:

1. **Set Up the Circuit**:
   - Build the circuit in Tinkercad as described above.
   - Ensure proper connections for Q1 and Q2, and verify \( R_{ref} = 1k\Omega \).

2. **Measure the Output Current**:
   - Run the simulation and measure the current through \( R_{load} \) using the multimeter.

3. **Vary the Load Resistance**:
   - Replace \( R_{load} \) with different resistances (\( 500\Omega, 1k\Omega, 2k\Omega \)).
   - Observe how the current remains stable despite changes in the load resistance.

4. **Test Voltage Sensitivity**:
   - Change the supply voltage (\( V_{supply} \)) from \( 10V \) to \( 15V \) and observe the output current.

---

### **Expected Results**:

1. **Stable Output Current**:
   - The current through \( R_{load} \) remains nearly constant regardless of variations in load resistance, demonstrating high output impedance.

2. **Voltage Independence**:
   - The output current does not vary significantly with changes in the supply voltage, showing improved stability.

3. **Cascode Effect**:
   - The cascode configuration minimizes the Early effect, enhancing current regulation.

---

### **Key Insights**:

- **Compound Current Source**:
  - The use of a cascode stage results in higher output impedance compared to a simple current source, making the circuit behave closer to an ideal current source.

- **Practical Applications**:
  - This experiment showcases how compound current sources are used in analog circuits for precise and stable current control.

---

This experiment is straightforward to implement in **Tinkercad**, and the results clearly demonstrate the advantages of a compound current source in achieving stable current output under varying conditions.
