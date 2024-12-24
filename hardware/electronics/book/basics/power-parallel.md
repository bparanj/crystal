### Power in a Parallel Circuit

Power in a parallel circuit refers to the rate at which electrical energy is consumed by the components. The total power is the sum of the power consumed by each branch.

### Reasoning

1. **Independent Power Consumption**:
   - In a parallel circuit, each branch operates independently, with the same voltage across all branches. The power consumed by each branch depends on its resistance and the common voltage.

2. **Power Formula**:
   The power consumed by a branch is given by:
   \[
   P = V \cdot I
   \]
   Substituting \(I = V / R\) from Ohm’s Law:
   \[
   P = \frac{V^2}{R}
   \]

3. **Total Power**:
   - Since branches are independent, the total power is the sum of the power in each branch:
     \[
     P_T = P_1 + P_2 + \dots + P_n
     \]

### Formulas for Power in a Parallel Circuit

1. **Power in Each Branch**:
   For a branch with resistance \(R_k\) and voltage \(V\):
   \[
   P_k = \frac{V^2}{R_k}
   \]

2. **Total Power**:
   If \(V\) is the voltage across all branches:
   \[
   P_T = \sum_{k=1}^{n} \frac{V^2}{R_k}
   \]

   Alternatively, using total current:
   \[
   P_T = V \cdot I_T
   \]

### Example

Given:
- \(V = 12 \, \text{V}\),
- \(R_1 = 4 \, \Omega\), \(R_2 = 6 \, \Omega\).

1. **Power in Each Branch**:
   \[
   P_1 = \frac{V^2}{R_1} = \frac{12^2}{4} = 36 \, \text{W}
   \]
   \[
   P_2 = \frac{V^2}{R_2} = \frac{12^2}{6} = 24 \, \text{W}
   \]

2. **Total Power**:
   \[
   P_T = P_1 + P_2 = 36 + 24 = 60 \, \text{W}
   \]

This shows how power is calculated and distributed in parallel circuits. Each branch contributes independently to the total power.
