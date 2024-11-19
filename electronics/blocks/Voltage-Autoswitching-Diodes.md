### **Voltage Autoswitching Diodes**

A **Voltage Autoswitching Diode Circuit** automatically switches between two power sources based on their voltages, ensuring that the higher voltage source powers the load. This is commonly used in backup power systems where a secondary source (e.g., battery) takes over if the primary source fails or drops below a threshold.

1. **Diode Behavior**:
   - A diode allows current to flow only in one direction, ensuring the higher voltage source powers the load.
   - The source with the higher voltage forward-biases its diode, while the lower voltage source is blocked.

2. **Autoswitching**:
   - The circuit seamlessly switches between sources without manual intervention.
   - Typically used in dual power systems (e.g., mains power and battery backup).

3. **Applications**:
   - UPS systems.
   - Dual power supplies.
   - Battery-powered devices with external adapters.

### Experiment

To design and simulate a **Voltage Autoswitching Diode Circuit** to demonstrate how the load is automatically powered by the higher voltage source.

---

#### **Components**:
1. **2 Diodes** (1N4007 or similar).
2. **2 Power Supplies** (\( V_1 = 12V \), \( V_2 = 9V \)).
3. **Resistor** (\( R = 1k\Omega \), load resistor).
4. **Multimeters** (to measure current and voltage).
5. **Breadboard** and wires.

#### **Circuit Connections**:

1. **Primary Power Source** (\( V_1 \)):
   - Connect \( V_1 \) to the anode of the first diode (\( D_1 \)).
   - Connect the cathode of \( D_1 \) to one end of the load resistor (\( R \)).

2. **Backup Power Source** (\( V_2 \)):
   - Connect \( V_2 \) to the anode of the second diode (\( D_2 \)).
   - Connect the cathode of \( D_2 \) to the same end of the load resistor (\( R \)).

3. **Load Resistor**:
   - Connect the other end of the resistor to ground.

4. **Multimeters**:
   - Place one multimeter across \( R \) to measure the voltage powering the load.
   - Place another multimeter in series with \( R \) to measure the current.

### Steps

#### **1. Normal Operation (Primary Power On)**:
1. Turn on both power supplies (\( V_1 = 12V, V_2 = 9V \)).
2. Observe:
   - \( D_1 \) is forward-biased, powering the load.
   - \( D_2 \) is reverse-biased, blocking \( V_2 \).

#### **2. Simulate Primary Power Failure**:
1. Turn off \( V_1 \) (primary source).
2. Observe:
   - \( D_2 \) becomes forward-biased, powering the load from \( V_2 \).
   - The load seamlessly switches to the backup power source.

#### **3. Restore Primary Power**:
1. Turn \( V_1 \) back on.
2. Observe:
   - The circuit automatically switches back to \( V_1 \), the higher voltage source.

### Results

1. **When \( V_1 > V_2 \)**:
   - The load is powered by \( V_1 \), with \( D_1 \) conducting and \( D_2 \) blocking.

2. **When \( V_1 < V_2 \) or \( V_1 \) is off**:
   - The load is powered by \( V_2 \), with \( D_2 \) conducting and \( D_1 \) blocking.

3. **Smooth Switching**:
   - The circuit ensures uninterrupted power to the load as it switches between sources.

### Insights

1. **Diode Selection**:
   - Use low forward-voltage-drop diodes (e.g., Schottky diodes) for minimal power loss.
   - Standard diodes like 1N4007 can also work but introduce a voltage drop (~0.7V).

2. **No Overlap**:
   - Only one source powers the load at any time, preventing backfeeding.

3. **Applications**:
   - Essential in backup systems, such as powering critical equipment from batteries when mains power fails.

In **Tinkercad**, you can toggle the power supplies to simulate power switching and observe:
1. Which diode conducts.
2. The voltage across the load resistor.
3. The seamless transition between power sources without manual intervention.