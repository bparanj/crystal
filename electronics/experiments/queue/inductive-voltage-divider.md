An equivalent experiment for demonstrating voltage division with inductors can be done using an inductive voltage divider circuit, similar in concept to resistive and capacitive voltage dividers. In an AC circuit, the voltage divides across inductors in series according to their inductances, with higher inductance resulting in a larger voltage drop.

To demonstrate that in a series circuit, voltage divides across inductors in proportion to their inductance values, with higher inductance causing a larger voltage drop.

### Components:

- 1 AC Power Source (e.g., 5V AC source)
- 2 Inductors with different values (e.g., 10 mH and 100 mH)
- Multimeter (to measure the voltage across each inductor)
- Breadboard and Wires

### Steps:

   - Connect the AC source’s positive terminal to the positive rail of the breadboard.
   - Connect the negative terminal of the AC source to the ground rail.

   - Connect the 10 mH inductor in series with the 100 mH inductor.
   - Connect one end of the 10 mH inductor to the positive rail.
   - Connect the other end of the 100 mH inductor to the ground rail.

   - Use the multimeter in Tinkercad to measure the AC voltage drop across each inductor.
   - You should observe that the 100 mH inductor has a higher voltage drop compared to the 10 mH inductor.
   - This is because inductive reactance (\( X_L = 2 \pi f L \)) is proportional to the inductance, so the larger inductance will have a higher impedance, leading to a larger share of the voltage in the series circuit.

In an AC series circuit, voltage divides across inductors in proportion to their inductance values. The larger the inductance, the more it impedes the AC current, which leads to a higher voltage drop across it. This is similar to how higher resistance in a resistor divider takes more voltage, but here it’s based on inductive reactance.

The voltage across each inductor can be calculated with:

\[
V_L = V_{in} \times \frac{L}{L_{total}}
\]

where:
- \( V_{in} \) is the total input voltage,
- \( L \) is the inductance of the inductor of interest,
- \( L_{total} \) is the sum of inductances in the series.
