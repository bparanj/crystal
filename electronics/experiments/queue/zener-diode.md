A simple circuit in Tinkercad to demonstrate the use of a Zener diode as a reference voltage.

### Components

- Breadboard
- Zener diode (e.g., 5.1V or 6.2V Zener diode)
- Resistor (appropriate value based on your input voltage, e.g., 330Ω or 470Ω)
- Power source (DC power supply or a 9V battery)
- Multimeter (to measure the reference voltage)

### Steps

1. Setup Power Supply:

Connect the positive terminal of your power supply to the breadboard’s positive rail, and the ground to the negative rail.

2. Zener Diode Connection:
   - Place the Zener diode on the breadboard.
   - Connect the cathode (end with the line) of the Zener diode to the power supply’s ground (negative rail).
   - Connect the anode to the resistor.

3. Resistor:
   - Connect the other end of the resistor to the positive rail (power supply’s positive).
   - This resistor limits the current flowing through the Zener diode, which is necessary for proper operation.

4. Measurement with Multimeter:
   - Place the multimeter across the Zener diode.
   - Set the power supply to a higher voltage than the Zener diode’s breakdown voltage (e.g., if using a 5.1V Zener, set around 9V).

5. Observe the Reference Voltage:
   - As the input voltage is higher than the Zener breakdown voltage, the diode will conduct and "clamp" the voltage at its breakdown level (e.g., 5.1V).
   - The multimeter should show a stable voltage close to the Zener's breakdown voltage, demonstrating the Zener diode’s function as a reference voltage.

The Zener diode maintains a constant voltage across it once the input voltage surpasses its breakdown voltage. This property is useful for creating a stable reference voltage in circuits, even when the input voltage fluctuates.

This setup can help visualize how a Zener diode operates as a voltage reference, a common use in voltage regulators and reference circuits.