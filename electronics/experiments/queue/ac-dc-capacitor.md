To demonstrate how a capacitor blocks DC current but allows AC to pass, you can set up a simple experiment in Tinkercad with a few basic components:

### Components:

1. Power Source: Use a DC source and an AC source (Tinkercad allows you to toggle between AC and DC power supplies).
2. Capacitor: 10 µF capacitor (or any small value capacitor).
3. Resistor: 1 kΩ resistor.
4. LED: To visualize current flow.
5. Switch: To alternate between DC and AC sources.
6. Multimeter: To measure voltage across the capacitor.

### Setup:

1. Connect the Power Source:
   - Connect one side of the capacitor to the positive terminal of the power source.
   - Connect the other side of the capacitor to one terminal of the resistor.

2. Add the LED and Resistor:
   - Connect the LED in series with the resistor. Place the LED’s positive terminal (anode) after the capacitor, and connect the negative terminal (cathode) to ground.

3. Insert a Switch to Alternate Between DC and AC:
   - Connect a switch to toggle between the DC and AC power sources. This will let you easily switch between the two types of current.

4. Place a Multimeter Across the Capacitor:
   - Connect the multimeter in parallel with the capacitor to observe the voltage across it during both AC and DC operation.

### Steps:

1. DC Mode (Switch to DC):
   - Set the power supply to 5V DC.
   - Observe the LED and the multimeter reading.
   - Expected Outcome: The LED will remain off, and the multimeter will show a voltage across the capacitor initially as it charges. Once fully charged, no current flows through the LED, demonstrating that DC current is blocked after the capacitor charges.

2. AC Mode (Switch to AC):
   - Switch the power source to 5V AC at a frequency (e.g., 50 Hz or 60 Hz).
   - Observe the LED and the multimeter reading again.
   - Expected Outcome: The LED will start to blink or stay on dimly, depending on the frequency of the AC signal. The multimeter will show alternating voltage across the capacitor, demonstrating that AC is passing through and causing a fluctuating current, which lights up the LED.

In DC Mode, the capacitor charges up and then blocks further current flow, as the current has no path through a fully charged capacitor. In AC Mode, the alternating current constantly changes direction, which allows the capacitor to continuously charge and discharge, enabling current flow through the circuit. This is why the LED lights up in AC mode but remains off in DC mode.

This setup will show how a capacitor blocks DC current after charging but allows AC current to pass through due to its continuous reversal of direction.
