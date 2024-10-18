Progmatic Electronics

Foundations through Experimentation

The basic principles from physics is explained in a simple language to provider a deeper understanding of the electronics. The basics of innovation is also discussed in the context of electronics.

Experiments Sequence

1. Short Circuit
		Demonstrate what happens to the voltage between the power source when there is a short circuit.
2. LED damage
		Demonstrate what happens to an electronic component when the current is not controlled.
3. LED Circuit (Resistor + LED)
		Demonstrate how controlling the current through an electronic component can protect it from damage.
4. Push Button
		Demonstrate the use of pushbutton to control the flow of current through a circuit.
5. Slide Switch
		Demonstrate the use of slide switch to control the flow of current through a circuit.
6. Potentiometer
		Demonstrate the use of variable resistor to control the flow of current through a circuit.
7. Capacitor
		Demonstrate the basic function of a capacitor in a circuit.
8. Missing Capacitor Experiment
		Demonstrate what happens to an electronic circuit when capacitor is not used.
9. Diode
		Demonstrate the basic function of a diode in a circuit.
10. Transistor
		Demonstrate the use of transistor in a circuit.

Create Simulation

Refer the links. Run simulation. Take screenshots of every step in the simulation

10. Inductor (Demo: https://www.tinkercad.com/things/jw2rfdSUsWg-inductordemonstration)
11. Variable Capacitor (LC Tuning Circuit) (LC - Inductor-Capacitor) https://www.tinkercad.com/things/bNBojeH8c6s-frequency-generator
		This should go after experiment #8.
12. Polarized Capacitor (see components/polarized-capacitor) https://www.tinkercad.com/things/6Z4EWNufnXG-polarized-capacitor

Experiment #1:

A **capacitor** is an electronic component that can become a **short-circuit** when it fails.

In a normal state, a capacitor blocks DC current after charging and allows AC to pass, acting as an insulator for direct current. However, when a capacitor fails, particularly through **dielectric breakdown**, it can lose its insulating property and create a low-resistance path between its terminals. This failure effectively **short-circuits** the capacitor, allowing current to flow freely where it should be blocked, potentially damaging other components in the circuit.

Other components, such as **transistors** and **diodes**, can also fail as a short-circuit in certain conditions, but capacitors are commonly known for this type of failure mode.

A **resistor** commonly becomes an **open-circuit** when it fails.

In normal operation, a resistor provides a specific resistance to limit current flow. However, due to factors like excessive heat or mechanical stress, the resistor can break or **burn out**, creating an open circuit. When this happens, it stops conducting entirely, and current can no longer flow through it.

Other components, such as **fuses**, **inductors**, and certain **semiconductors** (e.g., transistors), can also fail as open circuits under specific conditions. However, resistors are frequently associated with open-circuit failures in electronics.

## Missing Capacitor Experiment

A simple experiment to demonstrate the problem caused by not using a **capacitor** involves using an **LED** with a **switch** connected to a DC power supply. This setup shows how **capacitors help stabilize voltage** and prevent flickering or noise in circuits.

### Materials:
- **LED**
- **Resistor** (e.g., 220Ω to protect the LED)
- **Switch** (push button or slide switch)
- **Power supply** (e.g., 5V battery or DC source)
- **Capacitor** (e.g., 100 µF electrolytic capacitor)
- Connecting wires

### Steps:

1. **Build the Circuit Without a Capacitor**:
   - Connect the LED in series with the resistor and switch to the power supply.
   - The circuit should be: **Power supply -> Resistor -> LED -> Switch -> Power supply**.

2. **Operate the Switch**:
   - Toggle the switch on and off quickly. Observe the LED as you repeatedly switch the power.

3. **Observe Flickering**:
   - Without a capacitor, the LED may flicker or blink slightly as you toggle the switch. This happens because there is no smoothing component to stabilize the voltage fluctuations.

4. **Add a Capacitor and Repeat**:
   - Connect the capacitor in parallel with the LED and resistor (positive side to positive supply, negative side to ground).
   - Toggle the switch on and off as before, but now observe how the LED behaves with the capacitor in place.

5. **Observe the Stabilizing Effect**:
   - With the capacitor, the LED will remain stable, and any flickering or noise will be reduced. The capacitor smooths out the fluctuations by temporarily storing and releasing energy as needed.

### Explanation:
Without a capacitor, quick voltage changes can cause flickering, especially in circuits with sensitive components. Adding a capacitor acts as a **voltage stabilizer**, storing charge to maintain a steady output, which prevents flickering and ensures smooth operation. This experiment demonstrates the capacitor's role in **smoothing out voltage fluctuations** in circuits.
