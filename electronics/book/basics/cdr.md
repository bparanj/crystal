### Current Divider Rule (CDR) Explained

The **Current Divider Rule** explains how current splits between parallel branches in a circuit. The current through each branch depends on the resistance of that branch relative to the total resistance of the parallel network.

---

### Reasoning Behind the Rule

1. **Parallel Paths**:
   - In a parallel circuit, the voltage across all branches is the same because they share the same two nodes.
   - Current splits inversely proportional to the resistance of each branch (Ohm's Law: \(I = V / R\)).

2. **Lower Resistance → Higher Current**:
   - A branch with lower resistance allows more current to flow through it because it offers less opposition to the flow of charge.
   - Conversely, a higher-resistance branch carries less current.

3. **Proportional Distribution**:
   - Each branch's share of the total current is determined by the ratio of its resistance to the total parallel resistance.

---

### Formula for Current Divider Rule

For two parallel resistors, \(R_1\) and \(R_2\), with total current \(I_T\):

1. Current through \(R_1\):
   \[
   I_1 = I_T \cdot \frac{R_2}{R_1 + R_2}
   \]

2. Current through \(R_2\):
   \[
   I_2 = I_T \cdot \frac{R_1}{R_1 + R_2}
   \]

For \(n\) parallel resistors (\(R_1, R_2, \dots, R_n\)):
- Current through any resistor \(R_k\):
   \[
   I_k = I_T \cdot \frac{\frac{1}{R_k}}{\sum_{i=1}^{n} \frac{1}{R_i}}
   \]

---

### Example

Given \(I_T = 10 \, \text{A}\), \(R_1 = 4 \, \Omega\), and \(R_2 = 6 \, \Omega\):

1. Total resistance:
   \[
   R_T = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}} = \frac{1}{\frac{1}{4} + \frac{1}{6}} = 2.4 \, \Omega
   \]

2. Current through \(R_1\):
   \[
   I_1 = 10 \cdot \frac{6}{4 + 6} = 6 \, \text{A}
   \]

3. Current through \(R_2\):
   \[
   I_2 = 10 \cdot \frac{4}{4 + 6} = 4 \, \text{A}
   \]

This shows how \(I_T\) splits proportionally based on resistance.

The reasoning behind the **Current Divider Rule (CDR)** formulas lies in understanding how parallel circuits work and how current flows through them according to **Ohm’s Law** and the properties of parallel resistances.

---

### 1. **Constant Voltage Across Parallel Branches**
In a parallel circuit:
- The voltage across all parallel branches is the same because they are connected to the same two nodes.
- The current through each branch depends only on its resistance and the shared voltage.

From Ohm's Law:
\[
I_k = \frac{V}{R_k}
\]
Where:
- \(I_k\): Current through branch \(k\),
- \(V\): Voltage across all branches (same for all branches),
- \(R_k\): Resistance of branch \(k\).

---

### 2. **Current Splits Based on Resistance**
- A branch with **lower resistance** draws more current because it provides less opposition to the flow of charge.
- Conversely, a branch with **higher resistance** draws less current.

The current splits in proportion to the inverse of the resistance:
\[
I_k \propto \frac{1}{R_k}
\]

This relationship forms the core of the Current Divider Rule.

---

### 3. **Parallel Resistance Reduces Total Resistance**
The total current \(I_T\) entering the parallel combination is shared among the branches:
\[
I_T = I_1 + I_2 + \dots + I_n
\]

The total resistance of the parallel network (\(R_T\)) is given by:
\[
\frac{1}{R_T} = \sum_{i=1}^{n} \frac{1}{R_i}
\]
This relationship shows how resistances combine in parallel.

---

### 4. **Relating Branch Current to Total Current**
Using Ohm's Law for the total circuit:
\[
I_T = \frac{V}{R_T}
\]
The current through a specific branch \(I_k\) is related to the total current \(I_T\) by the fraction of its conductance (\(1/R_k\)) to the total conductance (\(1/R_T\)).

For \(n\) branches:
\[
I_k = I_T \cdot \frac{\frac{1}{R_k}}{\sum_{i=1}^{n} \frac{1}{R_i}}
\]

---

### 5. **Two-Branch Simplification**
For two parallel resistors, the total current \(I_T\) splits as:
- Current through \(R_1\):
  \[
  I_1 = I_T \cdot \frac{R_2}{R_1 + R_2}
  \]
  Here, \(R_2\) appears in the numerator because the current through \(R_1\) depends inversely on the resistance of \(R_1\) but directly on the relative resistance of the other branch (\(R_2\)).

- Current through \(R_2\):
  \[
  I_2 = I_T \cdot \frac{R_1}{R_1 + R_2}
  \]

This formula is derived from the proportional splitting of current:
\[
I_k = \frac{V}{R_k} \quad \text{and} \quad V = I_T \cdot R_T
\]

---

### Insights

1. **Voltage governs current**: Since voltage is constant across branches, current is solely determined by resistance.
2. **Inverse proportionality**: Lower resistance → higher current, higher resistance → lower current.
3. **Energy conservation**: Total current \(I_T\) splits among branches without being lost, adhering to Kirchhoff's Current Law (KCL).

This reasoning builds a logical foundation for the Current Divider Rule formulas.
