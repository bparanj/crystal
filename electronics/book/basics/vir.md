### Ohm's Law for Parallel Circuits

Ohm's Law states the relationship between voltage (\(V\)), current (\(I\)), and resistance (\(R\)):
\[
V = I \cdot R
\]
In a **parallel circuit**, the total current (\(I_T\)) is divided among the branches, but the voltage (\(V\)) across all branches is the same.

### Reasoning

1. **Same Voltage Across Branches**:
   - In a parallel circuit, all branches are connected to the same two points. This ensures the voltage is equal across every branch.

2. **Current Splits Across Branches**:
   - Current takes multiple paths, dividing between branches based on their resistance (lower resistance → higher current).

3. **Effective Resistance**:
   - The total resistance of a parallel circuit (\(R_T\)) is less than the smallest branch resistance because multiple paths make it easier for current to flow.

4. **Total Current**:
   - The total current (\(I_T\)) entering the parallel network is the sum of currents through all branches (\(I_1, I_2, \dots\)).

### Formulas for Parallel Circuits

1. **Total Resistance (\(R_T\))**:
   For \(n\) resistors in parallel:
   \[
   \frac{1}{R_T} = \sum_{i=1}^{n} \frac{1}{R_i}
   \]

   For two resistors (\(R_1\) and \(R_2\)):
   \[
   R_T = \frac{R_1 \cdot R_2}{R_1 + R_2}
   \]

2. **Current Through a Branch**:
   Using Ohm's Law for any branch \(k\):
   \[
   I_k = \frac{V}{R_k}
   \]

3. **Total Current**:
   Since \(I_T = I_1 + I_2 + \dots\), we get:
   \[
   I_T = V \cdot \left( \frac{1}{R_1} + \frac{1}{R_2} + \dots + \frac{1}{R_n} \right)
   \]

### Example

Given:
- \(R_1 = 4 \, \Omega\), \(R_2 = 6 \, \Omega\),
- \(V = 12 \, \text{V}\).

1. **Total Resistance**:
   \[
   R_T = \frac{1}{\frac{1}{4} + \frac{1}{6}} = 2.4 \, \Omega
   \]

2. **Total Current**:
   \[
   I_T = \frac{V}{R_T} = \frac{12}{2.4} = 5 \, \text{A}
   \]

3. **Branch Currents**:
   \[
   I_1 = \frac{V}{R_1} = \frac{12}{4} = 3 \, \text{A}, \quad I_2 = \frac{V}{R_2} = \frac{12}{6} = 2 \, \text{A}.
   \]

This shows how voltage governs the current distribution in a parallel circuit.
