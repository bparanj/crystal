### **Inductor as a Current Source**

An **inductor** can act as a current source because of its ability to resist changes in current due to its property of inductance. When connected to a voltage source, an inductor generates a gradually changing current, making it behave like a current source under specific conditions.

---

### Concepts

1. **Inductor Behavior**:
   - The voltage across an inductor is proportional to the rate of change of current:
     \[
     V_L = L \cdot \frac{dI}{dt}
     \]
   - An inductor resists sudden changes in current, causing the current through it to change gradually.

2. **Inductor as a Current Source**:
   - When a charged inductor is disconnected from the voltage source and connected to a load, it maintains the current flow temporarily, acting like a current source.

3. **Time Constant**:
   - The rate at which current changes is determined by the time constant in an RL circuit:
     \[
     \tau = \frac{L}{R}
     \]
   - Larger \( L \) or smaller \( R \) makes the current decay more slowly, resembling a stable current source.

---

### **Applications**:
1. **Current Stabilization**:
   - Used in applications requiring steady current for a short duration.
2. **Energy Storage**:
   - Supplies current during brief interruptions in power (e.g., in switching circuits).
3. **Filters**:
   - Used in LC filters to provide smooth current flow.

---

### Experiment

#### Objective
To demonstrate how an inductor behaves like a current source when connected to a load.

#### Components
1. **Inductor** (\( L = 10mH \)).
2. **DC Voltage Source** (\( V_{supply} = 10V \)).
3. **Switch** (SPST).
4. **Resistor** (\( R = 100\Omega \)) as the load.
5. **Multimeter** (to measure current).
6. **Oscilloscope** (to observe current decay).
7. **Breadboard** and wires.

---

### Circuit

1. **Charging Phase**:
   - Connect the inductor (\( L \)) in series with the voltage source (\( V_{supply} \)).
   - Place a switch between the voltage source and inductor.

2. **Discharging Phase**:
   - Connect the free terminal of the inductor to the load resistor (\( R \)).
   - Disconnect the voltage source using the switch to observe current behavior.

3. **Current Measurement**:
   - Place a multimeter in series with \( R \) to measure current.
   - Alternatively, use an oscilloscope across \( R \) to observe voltage (proportional to current).

---

### Steps

1. **Charging the Inductor**:
   - Close the switch to connect \( V_{supply} \) to the inductor.
   - Allow the current to build up through \( L \).

2. **Discharging Through the Load**:
   - Open the switch to disconnect \( V_{supply} \).
   - Connect \( L \) to the load resistor (\( R \)) and observe current flow through \( R \).

3. **Observe Current Decay**:
   - Use the multimeter or oscilloscope to observe the current decrease gradually over time.

4. **Experiment with \( L \) and \( R \)**:
   - Replace \( L \) with different inductances (\( 5mH, 20mH \)).
   - Change \( R \) to see how the current decay rate changes.

---

### Results

1. **Charging Phase**:
   - Current through \( L \) increases linearly with time until it stabilizes:
     \[
     I_L(t) = \frac{V_{supply}}{R} \cdot \left(1 - e^{-\frac{t}{\tau}}\right)
     \]

2. **Discharging Phase**:
   - The inductor maintains current through the load after disconnecting the voltage source.
   - Current decays exponentially:
     \[
     I_L(t) = I_0 \cdot e^{-\frac{t}{\tau}}
     \]
     Where \( I_0 \) is the initial current through \( L \).

3. **Effect of Time Constant**:
   - Larger \( L \) or smaller \( R \) results in slower current decay, making the inductor resemble a steady current source for longer.

---

### Insights

1. **Current Source Behavior**:
   - An inductor maintains current flow temporarily, effectively acting as a short-term current source.

2. **Time Constant Importance**:
   - The time constant \( \tau = L/R \) determines how long the inductor behaves as a current source.

3. **Applications**:
   - Useful in circuits requiring stable current during brief disruptions, such as in power supplies and filters.

---

This experiment can be implemented in **Tinkercad** to observe how an inductor behaves like a current source by maintaining current flow through a load after disconnection from the voltage source.
