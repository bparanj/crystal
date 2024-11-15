When two voltage sources are connected in series, their voltages either add or subtract depending on their polarity alignment. Here's how it works:

---

### Key Concepts:
1. Summing Voltages:
   - When two voltage sources are connected in series with their polarities aligned (positive terminal of one connected to the negative terminal of the other), their voltages add:
   \[
   V_{total} = V_1 + V_2
   \]

2. Subtracting Voltages:
   - When two voltage sources are connected in series but with opposing polarities (positive to positive or negative to negative), their voltages subtract:
   \[
   V_{total} = |V_1 - V_2|
   \]

---

### Circuit Design in Tinkercad:

#### Components:
1. Two DC Voltage Sources (e.g., \( V_1 = 5V \), \( V_2 = 3V \))
2. Multimeter (to measure the total voltage)
3. Breadboard
4. Connecting Wires

---

#### Experiment Steps:

1. Summing Voltages:
   - Connect the negative terminal of the first voltage source (\( V_1 \)) to the positive terminal of the second voltage source (\( V_2 \)).
   - Use a multimeter to measure the voltage across the remaining free terminals (positive of \( V_1 \) and negative of \( V_2 \)).
   - Expected reading: \( V_{total} = 5V + 3V = 8V \).

2. Subtracting Voltages:
   - Connect the positive terminal of the first voltage source (\( V_1 \)) to the positive terminal of the second voltage source (\( V_2 \)).
   - Use a multimeter to measure the voltage across the remaining free terminals (negative of \( V_1 \) and negative of \( V_2 \)).
   - Expected reading: \( V_{total} = |5V - 3V| = 2V \).

---

#### Observations:
- Voltage sources in series sum when their polarities are aligned.
- Opposing polarities result in subtraction of voltages.
- This principle is useful in signal conditioning and power supplies where specific voltage levels are needed.

#### Additional Insight:
You can extend this principle to multiple voltage sources in series. The resulting voltage is the algebraic sum of all individual voltages, considering their polarities.

### Experiment 1: Summing Voltages

#### Objective:
Demonstrate how to sum voltages by connecting two DC voltage sources in series.

---

#### Components:
1. Two DC voltage sources (\( V_1 = 5V \), \( V_2 = 3V \)).
2. Multimeter to measure the combined voltage.
3. Breadboard.
4. Connecting wires.


#### Circuit Setup:
1. Place two DC voltage sources on the breadboard.
   - Label their terminals as follows:
     - \( V_1 \): Positive (1a) and Negative (1b).
     - \( V_2 \): Positive (2a) and Negative (2b).

2. Connect the negative terminal of \( V_1 \) (1b) to the positive terminal of \( V_2 \) (2a).

3. Use a multimeter to measure the voltage across:
   - Positive terminal of \( V_1 \) (1a) and Negative terminal of \( V_2 \) (2b).


#### Steps:
1. Set \( V_1 = 5V \) and \( V_2 = 3V \).
2. Measure the voltage across 1a and 2b.
3. Record the result.

---

#### Expected Observation:
The measured voltage is:
\[
V_{total} = V_1 + V_2 = 5V + 3V = 8V
\]

---

---

### Experiment 2: Subtracting Voltages

#### Objective:
Demonstrate how to subtract voltages by connecting two DC voltage sources in series with opposing polarities.

---

#### Components:
1. Two DC voltage sources (\( V_1 = 5V \), \( V_2 = 3V \)).
2. Multimeter to measure the resultant voltage.
3. Breadboard.
4. Connecting wires.

---

#### Circuit Setup:
1. Place the two DC voltage sources on the breadboard.
   - Label their terminals as follows:
     - \( V_1 \): Positive (1a) and Negative (1b).
     - \( V_2 \): Positive (2a) and Negative (2b).

2. Connect the positive terminal of \( V_1 \) (1a) to the positive terminal of \( V_2 \) (2a).

3. Use a multimeter to measure the voltage across:
   - Negative terminal of \( V_1 \) (1b) and Negative terminal of \( V_2 \) (2b).

---

#### Steps:
1. Set \( V_1 = 5V \) and \( V_2 = 3V \).
2. Measure the voltage across 1b and 2b.
3. Record the result.

---

#### Expected Observation:
The measured voltage is:
\[
V_{total} = |V_1 - V_2| = |5V - 3V| = 2V
\]

---

### Insights:
- Summing voltages demonstrates how voltages add when polarities are aligned.
- Subtracting voltages shows how opposing polarities result in a voltage difference.
- These experiments can be used in Tinkercad or on a physical breadboard for hands-on understanding.

Yes, slight modifications are required for Tinkercad:

1. Voltage Sources: Use two batteries or two DC power supplies in Tinkercad to simulate the voltage sources.
2. Connections: Ensure proper polarity by adjusting battery orientations in the schematic.
3. Multimeter: Use Tinkercad's built-in multimeter to measure the voltage across the specified points.
4. Breadboard: Place batteries directly in the simulation workspace instead of relying on physical terminal labels. Connect wires appropriately.

No major changes to the experiment steps are needed; just adapt the physical wiring to Tinkercad's interface.
