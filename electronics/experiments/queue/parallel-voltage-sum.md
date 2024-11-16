To sum or subtract voltages by preconverting them into currents, you can use resistors to convert the input voltages into currents, then process the currents in parallel (summing/subtracting) and reconvert the result back into a voltage using a load resistor.

### Concepts:

1. Voltage-to-Current Conversion:
   - By Ohm’s Law, a voltage source \( V \) across a resistor \( R \) generates a current:
     \[
     I = \frac{V}{R}
     \]

2. Summing/Subtracting Currents:
   - When these currents are combined in parallel, they sum or subtract based on their direction (polarity).

3. Current-to-Voltage Conversion:
   - The total current is passed through a load resistor to convert the combined current back into a voltage:
     \[
     V_{out} = I_{total} \cdot R_L
     \]

### Experiment

#### Components:
1. Two DC voltage sources (e.g., \( V_1 = 5V \), \( V_2 = 3V \)).
2. Two resistors (\( R_1 \), \( R_2 \)) for voltage-to-current conversion.
3. One load resistor (\( R_L \)) for current-to-voltage conversion.
4. Multimeter to measure the output voltage.
5. Breadboard and wires.

### Experiment 1: Summing Voltages

#### Circuit Setup:
1. Connect \( V_1 \) across \( R_1 \) and \( V_2 \) across \( R_2 \) separately.
2. Connect the free ends of \( R_1 \) and \( R_2 \) to a common node.
3. Connect the common node to \( R_L \), and then connect \( R_L \) to ground.
4. Measure the output voltage across \( R_L \).

#### Steps:
1. Set \( V_1 = 5V \), \( V_2 = 3V \), \( R_1 = 1k\Omega \), \( R_2 = 1k\Omega \), and \( R_L = 1k\Omega \).
2. Calculate the individual currents:
   \[
   I_1 = \frac{V_1}{R_1} = \frac{5V}{1k\Omega} = 5mA
   \]
   \[
   I_2 = \frac{V_2}{R_2} = \frac{3V}{1k\Omega} = 3mA
   \]
3. The total current is:
   \[
   I_{total} = I_1 + I_2 = 5mA + 3mA = 8mA
   \]
4. The output voltage is:
   \[
   V_{out} = I_{total} \cdot R_L = 8mA \cdot 1k\Omega = 8V
   \]

### Experiment 2: Subtracting Voltages

#### Circuit Setup:
1. Connect \( V_1 \) across \( R_1 \) and reverse the polarity of \( V_2 \) across \( R_2 \).
2. Connect the free ends of \( R_1 \) and \( R_2 \) to a common node.
3. Connect the common node to \( R_L \), and then connect \( R_L \) to ground.
4. Measure the output voltage across \( R_L \).

#### Steps:
1. Set \( V_1 = 5V \), \( V_2 = 3V \), \( R_1 = 1k\Omega \), \( R_2 = 1k\Omega \), and \( R_L = 1k\Omega \).
2. Calculate the individual currents:
   \[
   I_1 = \frac{V_1}{R_1} = 5mA, \quad I_2 = \frac{V_2}{R_2} = 3mA
   \]
3. The total current is:
   \[
   I_{total} = I_1 - I_2 = 5mA - 3mA = 2mA
   \]
4. The output voltage is:
   \[
   V_{out} = I_{total} \cdot R_L = 2mA \cdot 1k\Omega = 2V
   \]

### Notes
- Replace ideal current sources with DC voltage sources and resistors for conversion.
- Ensure polarity alignment for summing or subtraction.
- Use the ammeter to measure total current at the node if needed.
- Place a multimeter across the load resistor to measure the final voltage.
