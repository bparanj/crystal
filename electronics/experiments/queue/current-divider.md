PENDING

This is already complete. Merge with the experiment.

A current divider circuit allows the input current to be split between two or more parallel branches based on their resistances (or impedances in AC circuits).

### How a Current Divider Works

In a current divider, the total current \( I_{\text{total}} \) entering the parallel branches splits among the branches, with the amount of current in each branch inversely proportional to the resistance of that branch.

For two resistors \( R_1 \) and \( R_2 \) in parallel, the current through each resistor can be calculated as:

- Current through \( R_1 \):
  \[
  I_1 = I_{\text{total}} \cdot \frac{R_2}{R_1 + R_2}
  \]

- Current through \( R_2 \):
  \[
  I_2 = I_{\text{total}} \cdot \frac{R_1}{R_1 + R_2}
  \]

### Simple Current Divider Circuit

Here’s a basic current divider circuit using two resistors in parallel.

#### Components:

1. DC Power Source: e.g., 9V battery or DC supply.
2. Resistor \( R_1 \): e.g., 1 kΩ.
3. Resistor \( R_2 \): e.g., 2 kΩ.
4. Ammeter or Multimeter: To measure the current through each branch.

#### Setup:

1. Power Supply Connection:
   - Connect the positive terminal of the DC power source to one end of both \( R_1 \) and \( R_2 \) resistors.

2. Parallel Branches:
   - Connect the other end of \( R_1 \) and \( R_2 \) to the negative terminal of the power supply (forming a parallel circuit).

3. Measurement:
   - Place an ammeter in each branch or use a multimeter to measure the current through \( R_1 \) and \( R_2 \).
   - Alternatively, you could calculate the expected currents using the formulas above.

The current through each resistor depends on its resistance. For example, if \( R_1 = 1 \, \text{kΩ} \) and \( R_2 = 2 \, \text{kΩ} \) with a total current \( I_{\text{total}} \), more current will flow through \( R_1 \) (lower resistance) than through \( R_2 \).

This simple circuit shows how current divides between parallel branches based on resistance, following the principle of a current divider.
