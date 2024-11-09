A simple experiment in Tinkercad to demonstrate a relay-driven LED circuit:

https://www.tinkercad.com/things/4m6CB0ucXPe/editel?returnTo=%2Fdashboard%2Fdesigns%2Fcircuits

### Components

- Breadboard
- Relay (e.g., a 5V relay)
- LED
- Resistor (220Ω for the LED)
- NPN transistor (e.g., 2N2222 or similar)
- Power supply (5V DC)
- Switch (optional, to control the relay circuit)
- Diode (e.g., 1N4007 to protect against back EMF)
- Connecting wires

### Steps

1. Set Up the Power Supply:

Connect the positive and ground lines of the 5V power supply to the breadboard’s power and ground rails.

2. Connect the Relay and Transistor:
   - Place the relay on the breadboard.
   - Connect the collector of the NPN transistor to one side of the relay coil.
   - Connect the other side of the relay coil to the 5V power rail.
   - Connect the emitter of the transistor to the ground rail of the breadboard.

3. Add a Diode for Protection:
   - Connect the diode (1N4007) across the relay coil, with the cathode (the end with the line) connected to the 5V rail side and the anode to the transistor's collector side. This diode protects the transistor from voltage spikes when the relay switches.

4. Control the Transistor Base:
   - Connect a 1kΩ resistor between the base of the transistor and the positive rail (or a switch, if using, to control the relay with the switch).
   - This resistor limits the current flowing to the transistor’s base.

5. Connect the LED:
   - Connect the common (COM) terminal of the relay to the ground rail.
   - Connect the normally open (NO) terminal of the relay to the negative side of the LED.
   - Connect the positive side of the LED to the 5V power rail through a 220Ω resistor.

6. Operation:
   - When you power the circuit, the transistor will activate the relay by energizing the coil when a small current flows into the transistor's base.
   - The relay will switch, closing the circuit between the NO terminal and COM, allowing current to flow through the LED and light it up.

The transistor acts as a switch that controls the relay. When a signal is sent to the transistor’s base, it completes the circuit for the relay coil, energizing the relay. This energization switches the relay’s NO terminal to COM, turning on the LED by allowing current to flow through it.

This experiment demonstrates how a relay can be controlled with a low-power signal (from the transistor) to switch a higher-power device (the LED) and is a fundamental principle in relay-driven circuits.
