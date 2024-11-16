A simple experiment in Tinkercad to demonstrate the behavior of two inductors connected in series.

### Objective

To observe how connecting two inductors in series affects the total inductance and how it influences the current in an AC circuit.

### Components

1. Breadboard
2. AC Power Supply (e.g., 5V AC, 60 Hz)
3. Two inductors (e.g., 100 mH each)
4. Resistor (100 Ω) to control current flow
5. Ammeter or Multimeter to measure current
6. Wires for connections

### Steps

1. Set Up the Breadboard and AC Power Supply:
   - Place the 5V AC power supply on the breadboard.
   - Connect the positive terminal of the AC source to a row on the breadboard for connecting components.
   - Connect the negative terminal to the ground rail of the breadboard.

2. Connect Two Inductors in Series:
   - Place the first inductor on the breadboard, connecting one terminal to the positive rail where the AC power supply is connected.
   - Connect the other terminal of the first inductor to a new row on the breadboard.
   - Place the second inductor on the breadboard, connecting one terminal to the first inductor’s open terminal.
   - Connect the remaining terminal of the second inductor to a new row on the breadboard, creating a series connection between the two inductors.

3. Add a Resistor in Series:
   - Place a 100 Ω resistor in series with the inductors. Connect one terminal of the resistor to the open terminal of the second inductor.
   - Connect the other terminal of the resistor to the negative terminal of the AC source. This resistor will limit the current and help measure the effect of the inductors on the current flow.

4. Attach an Ammeter to Measure Current:
   - Place an ammeter in series with the inductors and resistor to measure the current through the entire circuit.

5. Run the Simulation:
   - Start the simulation in Tinkercad.
   - Observe the current reading on the ammeter.
   - Note that the current is lower than it would be with a single inductor because the total inductance increases in series.

6. Explanation of the Effect of Inductors in Series:
   - When inductors are connected in series, their total inductance is the sum of their individual inductances:
     \[
     L_{\text{total}} = L_1 + L_2
     \]
   - In this case, with two 100 mH inductors, the total inductance is 200 mH. This higher inductance increases the inductive reactance \(X_L = 2 \pi f L\), which opposes the flow of AC current more strongly, resulting in a lower current reading than with one inductor.

### Observations

- Increased Inductance in Series: The two inductors in series increase the total inductance, leading to greater opposition to AC current (higher reactance).
- Reduced Current: The current in the circuit decreases due to the higher inductive reactance from the combined inductance.

This experiment demonstrates that connecting inductors in series adds their inductances together, increasing the total inductance, which decreases the current in an AC circuit due to higher reactance.
