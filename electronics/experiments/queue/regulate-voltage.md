Regulating voltage with resistance involves controlling the voltage at a specific point in a circuit by using a resistor. This is commonly done in two main configurations:

### 1. Voltage Divider

A voltage divider is a circuit consisting of two resistors connected in series, with the output voltage taken from the junction between them.

#### Formula:

\[
V_{\text{out}} = V_{\text{in}} \times \frac{R_2}{R_1 + R_2}
\]

Where:
- \( V_{\text{in}} \): Input voltage
- \( R_1, R_2 \): Resistors
- \( V_{\text{out}} \): Output voltage

#### Example:

If \( V_{\text{in}} = 10 \, \text{V} \), \( R_1 = 2 \, \Omega \), and \( R_2 = 3 \, \Omega \), the output voltage is:
\[
V_{\text{out}} = 10 \times \frac{3}{2+3} = 6 \, \text{V}
\]

### 2. Current-Limiting and Load Voltage Regulation

Using a single resistor to regulate voltage involves connecting a load in parallel or series, with the resistor adjusting the voltage supplied to the load.

The resistor's value determines the voltage drop, which impacts the voltage available for the load. This approach is common in simple circuits like LED setups.

#### Example:

- An LED needs 2V, and the source is 5V. Adding a resistor drops the excess voltage:
  \[
  R = \frac{V_{\text{drop}}}{I} = \frac{5 - 2}{0.02} = 150 \, \Omega
  \]

### Applications:

1. Voltage Dividers: Used for biasing transistors, scaling signals, or providing reference voltages.
2. LEDs: A resistor ensures the correct operating voltage and current.
3. Adjustable Voltage: Using a variable resistor (potentiometer) allows dynamic voltage control.

- The load connected to the circuit impacts the voltage regulation. For precise regulation, additional components like voltage regulators or Zener diodes are often used.
- Voltage regulation with resistance alone is less efficient in high-power circuits due to energy loss as heat in the resistor.
