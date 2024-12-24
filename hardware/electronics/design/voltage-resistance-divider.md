### Voltage-into-Resistance Divider

A Voltage-into-Resistance Divider (commonly called a Voltage Divider) is a simple circuit that divides an input voltage into smaller fractions based on the ratio of two or more resistors connected in series.

### Concepts

1. Voltage Division Rule:
   - The output voltage across one of the resistors is proportional to its resistance relative to the total resistance:
     \[
     V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}
     \]
     - \( V_{in} \): Input voltage.
     - \( V_{out} \): Output voltage across \( R_2 \).
     - \( R_1, R_2 \): Resistors in the divider.

2. Applications:
   - Scaling voltages for sensors or ADC inputs.
   - Biasing transistors.
   - Reducing high voltages for safe measurement.

### Experiment

#### Objective

Demonstrate the operation of a Voltage Divider circuit and observe the output voltage as a function of resistance.

#### Components

1. DC Voltage Source (\( V_{in} = 10V \)).
2. Two Resistors (\( R_1 = 1k\Omega, R_2 = 2k\Omega \)).
3. Multimeter (to measure output voltage).
4. Breadboard and wires.

### Circuit

1. Resistor Connection:
   - Connect \( R_1 \) and \( R_2 \) in series.
   - Connect the free terminal of \( R_1 \) to the positive terminal of the DC voltage source (\( V_{in} \)).
   - Connect the free terminal of \( R_2 \) to the ground terminal of \( V_{in} \).

2. Output Voltage:
   - Connect a multimeter across \( R_2 \) to measure \( V_{out} \).

### Steps

1. Set Input Voltage:
   - Set \( V_{in} = 10V \) on the DC voltage source.

2. Measure Output Voltage:
   - Use the multimeter to measure \( V_{out} \) across \( R_2 \).
   - Expected:
     \[
     V_{out} = 10V \cdot \frac{2k\Omega}{1k\Omega + 2k\Omega} = 10V \cdot \frac{2}{3} = 6.67V
     \]

3. Experiment with Different Resistor Values:
   - Change \( R_2 \) to \( 1k\Omega \), \( 3k\Omega \), and \( 5k\Omega \), and observe how \( V_{out} \) changes.
   - Note the proportional relationship.

4. Test Load Effect:
   - Add a parallel load resistor (\( R_L \)) across \( R_2 \) and observe the impact on \( V_{out} \).

### Results

1. Voltage Division:
   - \( V_{out} \) decreases as \( R_2 \) decreases or \( R_1 \) increases.

2. Load Effect:
   - Adding a load resistor changes the effective resistance across \( R_2 \), altering the output voltage:
     \[
     R_{eff} = \frac{R_2 \cdot R_L}{R_2 + R_L}
     \]

### Insights

1. Scaling Voltage:
   - Voltage dividers are a simple way to produce a reduced voltage.

2. Load Sensitivity:
   - Ensure the load impedance is significantly larger than \( R_2 \) to minimize output voltage change.

3. Applications:
   - Used in circuits where precise voltage division is required, such as in biasing or interfacing.

You can change resistor values dynamically and observe how the output voltage behaves in a Voltage Divider circuit.
