When current sources are connected in parallel, their currents add or subtract depending on their direction. This is governed by Kirchhoff’s Current Law (KCL), which states that the total current entering a node equals the total current leaving it.

1. Summing Currents:
   - When current sources are connected in parallel with the same direction, their currents add.
   \[
   I_{total} = I_1 + I_2
   \]

2. Subtracting Currents:
   - When current sources are connected in parallel but with opposite directions, their currents subtract.
   \[
   I_{total} = |I_1 - I_2|
   \]

3. Node Voltage:
   - In parallel, the node voltage is the same for all current sources.

### Circuit

#### Components:

1. Two current sources (\( I_1 = 2mA \), \( I_2 = 1mA \)).
2. Resistor to limit current (e.g., \( R = 1k\Omega \)).
3. Multimeter to measure the resulting current.
4. Breadboard.
5. Connecting wires.

### Experiment 1: Summing Currents

#### Setup:

1. Place two current sources (\( I_1 \) and \( I_2 \)) in parallel on the breadboard.
   - Connect both positive terminals to a common node.
   - Connect both negative terminals to another common node.

2. Add a resistor (\( R \)) in series with the parallel combination of current sources to ground.

3. Use a multimeter to measure the total current flowing through the resistor.

#### Steps:

1. Set \( I_1 = 2mA \) and \( I_2 = 1mA \).
2. Measure the current through the resistor.

#### Observation:

The total current is:
\[
I_{total} = I_1 + I_2 = 2mA + 1mA = 3mA
\]

### Experiment 2: Subtracting Currents

#### Setup:

1. Place the two current sources in parallel, but reverse the polarity of \( I_2 \) (positive terminal of \( I_2 \) to the common node connected to \( I_1 \)'s negative terminal).

2. Add a resistor (\( R \)) in series with the parallel combination of current sources to ground.

3. Use a multimeter to measure the total current.

#### Steps:

1. Set \( I_1 = 2mA \) and \( I_2 = 1mA \).
2. Measure the current through the resistor.

#### Observation:

The total current is:
\[
I_{total} = |I_1 - I_2| = |2mA - 1mA| = 1mA
\]

### Insights

- Replace ideal current sources with DC power supplies and adjust their voltages to control current using series resistors.
- Use the ammeter tool in Tinkercad to measure the total current in the circuit.
- Adjust source orientations for summing or subtracting current.

### Experiment 1: Summing Currents

#### Objective:

Demonstrate summing of currents by connecting two current sources in parallel with the same direction.

#### Components:

1. Two DC power supplies (\( V_1 = 10V \), \( V_2 = 10V \)).
2. Two resistors (\( R_1 = 5k\Omega \), \( R_2 = 10k\Omega \)) to act as current limiters.
3. One load resistor (\( R_L = 1k\Omega \)) to measure the total current.
4. Ammeter (or multimeter in current mode).
5. Breadboard and connecting wires.

#### Circuit

1. Use \( V_1 \) and \( V_2 \) as voltage sources to simulate current sources. Connect each through its respective series resistor \( R_1 \) and \( R_2 \).
   - \( V_1 \) and \( V_2 \) should have their positive terminals connected to a common node.
   - Their negative terminals should also connect to another common node.

2. Connect the load resistor \( R_L \) in series with the parallel combination of \( R_1 \) and \( R_2 \).

3. Place the ammeter in series with \( R_L \) to measure the total current.

#### Steps:

1. Set \( V_1 = 10V \) and \( V_2 = 10V \).
2. Calculate the individual currents using Ohm’s law:
   \[
   I_1 = \frac{V_1}{R_1} = \frac{10V}{5k\Omega} = 2mA
   \]
   \[
   I_2 = \frac{V_2}{R_2} = \frac{10V}{10k\Omega} = 1mA
   \]
3. Measure the total current through \( R_L \).

#### Observation:

The total current is the sum:
\[
I_{total} = I_1 + I_2 = 2mA + 1mA = 3mA
\]

### Experiment 2: Subtracting Currents

#### Objective:

Demonstrate subtracting of currents by connecting two current sources in parallel with opposing directions.

#### Components:

1. Two DC power supplies (\( V_1 = 10V \), \( V_2 = 10V \)).
2. Two resistors (\( R_1 = 5k\Omega \), \( R_2 = 10k\Omega \)) to act as current limiters.
3. One load resistor (\( R_L = 1k\Omega \)).
4. Ammeter (or multimeter in current mode).
5. Breadboard and connecting wires.

#### Setup:

1. Use \( V_1 \) and \( V_2 \) as voltage sources to simulate current sources. Connect each through its respective series resistor \( R_1 \) and \( R_2 \).

2. Reverse the polarity of \( V_2 \):
   - Connect \( V_2 \)'s negative terminal to the common positive node of \( V_1 \) and \( R_1 \).
   - Connect \( V_2 \)'s positive terminal to the common negative node of \( V_1 \) and \( R_1 \).

3. Connect the load resistor \( R_L \) in series with the parallel combination of \( R_1 \) and \( R_2 \).

4. Place the ammeter in series with \( R_L \) to measure the total current.

#### Steps:

1. Set \( V_1 = 10V \) and \( V_2 = 10V \).
2. Calculate the individual currents as before:
   \[
   I_1 = \frac{V_1}{R_1} = 2mA
   \]
   \[
   I_2 = \frac{V_2}{R_2} = 1mA
   \]
3. Measure the total current through \( R_L \).

#### Observation:

The total current is the difference:
\[
I_{total} = |I_1 - I_2| = |2mA - 1mA| = 1mA
\]

### Notes

- Use DC voltage sources to simulate current sources with series resistors.
- Place an ammeter in the circuit to measure total current.
- Adjust the resistors and polarities to switch between summing and subtracting scenarios.

Yes, modifications are needed for Tinkercad:

1. Simulate Current Sources: Use DC voltage sources with series resistors to mimic current sources.
2. Polarity Control: Reverse the orientation of one voltage source for the subtraction experiment.
3. Measure Current: Use Tinkercad's ammeter tool to measure the current through the load resistor instead of directly summing currents.
4. No Ideal Current Source: Use proper resistor values to control current through the simulated sources.

These changes adapt the experiments to Tinkercad's simulation constraints.
