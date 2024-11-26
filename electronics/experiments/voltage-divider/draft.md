
### Voltage Divider Circuit

The circuit consists of two resistors connected in series across a voltage source (e.g., a 9V battery). The resistors create a division of the total voltage, with each resistor receiving a share proportional to its resistance. The voltage at the midpoint between the two resistors, relative to the ground, is the circuit's output voltage.

- When current flows through the resistors, each experiences a voltage drop proportional to its resistance value.
- The total voltage drop across all components equals the supply voltage, illustrating Kirchhoff's Voltage Law.
- The midpoint voltage (output voltage) can be calculated using the formula:
  \[
  V_{\text{out}} = V_{\text{in}} \left( \frac{R_2}{R_1 + R_2} \right)
  \]


- The larger resistor (3 kΩ) experiences a higher voltage drop than the smaller resistor (1 kΩ).
- Voltage divides proportionally:
  - \( V_{1k} \approx 2.25V \)
  - \( V_{3k} \approx 6.75V \)

This proportional division demonstrates how the resistor values dictate the voltage drop, validating the voltage divider formula.

Altering the resistor values changes the distribution of voltage:

- **Higher Resistance:** Increases the voltage drop across that resistor.
- **Lower Resistance:** Reduces the voltage drop.

This shows the importance of selecting appropriate resistor values when designing circuits to achieve specific output voltages.

### Forward Voltage Drop in LEDs

Adding LEDs to the circuit introduces another layer of understanding. LEDs require a specific forward voltage (e.g., 1.87V in this case) to conduct. This behavior demonstrates that components in a circuit impose distinct voltage requirements, further reinforcing the concept of voltage drops.

### Applications of Voltage Divider Circuits

Voltage dividers have practical purposes, such as:

1. **Reducing Voltage:** Adjusting voltage levels for sensors and low-voltage components.
2. **Reference Voltages:** Providing stable voltage points in circuits.
3. **Level Shifting:** Adapting signal levels for compatibility between components.
4. **Biasing Circuits:** Setting operating points in amplifiers and other active components.

This experiment illustrates:

1. **Voltage Division:** Voltage is distributed in proportion to resistance in a series circuit.
2. **Voltage Drops:** The sum of individual voltage drops equals the total supply voltage.
3. **Design Flexibility:** By changing resistor values, we can control output voltage to meet specific needs.

The voltage divider is used to meet different voltage requirements in circuits.
