an experiment in Tinkercad to demonstrate the behavior of two inductors connected in parallel.

To observe how connecting two inductors in parallel affects the total inductance and the current in an AC circuit.

### Components

1. Breadboard
2. AC Power Supply (e.g., 5V AC, 60 Hz)
3. Two inductors (e.g., 100 mH each)
4. Resistor (100 Ω) for current control
5. Ammeter or Multimeter to measure current
6. Connecting wires

### Steps

   - Place the 5V AC power supply on the breadboard.
   - Connect the positive terminal of the AC source to a row on the breadboard, which will serve as the main current source point.
   - Connect the negative terminal of the AC source to the ground rail of the breadboard.

   - Place the two inductors on the breadboard.
   - Connect one terminal of each inductor to the positive rail of the AC source.
   - Connect the other terminal of each inductor to the same row on the breadboard, creating a parallel connection between the inductors.

   - Connect a 100 Ω resistor in series with the parallel inductors.
   - Connect one terminal of the resistor to the parallel junction where both inductors connect to the AC power supply.
   - Connect the other terminal of the resistor to the negative rail of the AC power supply.

   - Place an ammeter in series with the inductors and resistor to measure the total current flowing through the circuit.

   - Start the simulation in Tinkercad.
   - Observe the current reading on the ammeter.
   - Note that the current may be higher than if only one inductor were present, due to the reduced total inductance in parallel.

6. Explanation of Inductors in Parallel:
   - When inductors are connected in parallel, the total inductance is lower than that of a single inductor. The formula for calculating total inductance \( L_{\text{total}} \) for two inductors \( L_1 \) and \( L_2 \) in parallel is:
     \[
     \frac{1}{L_{\text{total}}} = \frac{1}{L_1} + \frac{1}{L_2}
     \]
   - For two 100 mH inductors in parallel, the total inductance is:
     \[
     L_{\text{total}} = \frac{L_1 \times L_2}{L_1 + L_2} = \frac{100 \, \text{mH} \times 100 \, \text{mH}}{100 \, \text{mH} + 100 \, \text{mH}} = 50 \, \text{mH}
     \]
   - This lower total inductance reduces the inductive reactance (\(X_L = 2 \pi f L\)), allowing more AC current to flow through the circuit.

### Observations

Reduced Inductance in Parallel:

The two inductors in parallel result in a total inductance that is lower than each individual inductor, leading to less opposition to AC current.

Increased Current:

With reduced total inductance, the circuit’s overall inductive reactance is lower, allowing more current to flow through the circuit, which is shown by a higher reading on the ammeter.

This experiment demonstrates that connecting inductors in parallel reduces the total inductance, decreasing the circuit’s inductive reactance and allowing more current to flow in an AC circuit.
