4. How do inductors behave as passive components?

Inductors store energy in a magnetic field created by current flow through a coil of wire. They resist changes in current flow, allowing DC to pass while impeding AC. Their inductance is measured in henries (H).

An inductor acts like a heavy water wheel in a stream. It resists sudden changes in water flow (current) due to its inertia, smoothing out flow variations.

To demonstrate an inductor's effect:

a) Set up an AC circuit with a function generator, a 100mH inductor, and an oscilloscope.
b) Generate a square wave signal at 1kHz.
c) Observe the square wave on the oscilloscope without the inductor.
d) Insert the inductor in series and observe how it rounds the square wave edges.
e) This shows how the inductor resists rapid current changes, smoothing the signal.

1.  What is inductance, and how does an inductor create it?

Inductance refers to the property of an electrical conductor to oppose changes in the current flowing through it. An inductor creates inductance through its coiled structure, which generates a magnetic field when current flows, opposing changes in that current.

Inductance resembles the momentum of a heavy flywheel. Just as a spinning flywheel resists changes to its rotational speed due to its momentum, an inductor resists changes to the current flowing through it due to its inductance.

11. Inductor (Demo: https://www.tinkercad.com/things/jw2rfdSUsWg-inductordemonstration)

Inductors store energy in the form of a magnetic field when current flows through them and oppose changes in current.

PENDING

Use multimeter and show the current in the circuit without inductor when the switch is closed
Do the same with inductor added to that circuit. Compare and summarize the experiment results
Use multimeter to verify whether a inductor can drive LED in a closed circuit

The power supply can be used to provide a steady or varying voltage to the circuit, driving current through the inductor. This helps in showing how the inductor reacts to changes in the applied voltage.

4. Amperage Multimeter (Meter2):

The multimeter can be used to measure the current flowing through the inductor. This allows observation of the delayed current response due to the inductor's opposition to changes in current (known as inductive reactance).

Explanation of Tinekrcad simulation:

The demonstration involves two circuits with an inductor and a light bulb, but they behave very differently due to the varying parameters of voltage, current, and frequency.

An inductor can cause an LED to glow dimly and gradually turn off even in an open circuit due to its ability to store energy in its magnetic field. Here's how this works:

Energy Storage in Inductors:

When current flows through an inductor, it stores energy in its magnetic field. If the circuit is suddenly opened, the inductor resists the abrupt change in current by releasing its stored energy. This released energy can power components like LEDs momentarily.

LED Behavior:

Upon opening the circuit, the inductor's stored energy discharges through the LED, causing it to emit light briefly. As the energy depletes, the LED's brightness diminishes gradually until it turns off completely.

- Inductor's Role: Acts as an energy reservoir, releasing stored energy when the circuit opens.
- LED Response: Utilizes the inductor's discharged energy, resulting in a temporary, fading glow.
- Circuit This phenomenon occurs even if the circuit is open after the inductor has been energized.

This behavior is a fundamental characteristic of inductors in electrical circuits, demonstrating their ability to oppose sudden changes in current by releasing stored energy.

### Circuit 1:

Components:

- Sine function generator
- inductor (L1 or L3)
- bulb (L2 or L4).

Function Generator Output:

2000 Hz, 10 V, sine wave.

Observed Current:

71 µA (microamperes).

1. High Frequency from Function Generator:

The sine function generator outputs a 2000 Hz signal. At high frequencies, the inductive reactance (\(X_L = 2\pi f L\)) of the inductor increases.

Inductive reactance depends on frequency (\(f\)) and inductance (\(L\)). As frequency rises, the inductor opposes the current more strongly.

This explains why the current is very low (71 µA). The high reactance limits the current flowing through the circuit, which also affects the brightness of the bulb (likely very dim or off).

2. Bulb Behavior:

The light bulb in this circuit likely stays off or is barely glowing because the low current (71 µA) is insufficient to heat the filament and produce visible light.

### Circuit 2:

Components:

Power supply, inductor (L1 or L3), and bulb (L2 or L4).

- Power Supply Output: 10 V.
- Observed Current: 187 mA (milliamperes).
- Bulb Status: On.

DC Power Supply:

The power supply provides constant DC voltage (10 V). Unlike AC signals, DC voltage doesn't change over time, so there is no frequency-dependent reactance here. The only opposition to current flow is the resistance of the bulb and the initial opposition from the inductor (as it builds its magnetic field).

After the inductor builds its magnetic field, it behaves like a short circuit in DC, meaning the current flows more easily.

2. Higher Current:

The observed current (187 mA) is much higher because there’s no significant reactance limiting it like in the first circuit. The inductor only briefly resists changes in current when the circuit is first powered on.

Since there is sufficient current, the bulb lights up fully.

- Circuit 1 (with the function generator): The high-frequency AC signal increases the inductor’s reactance, reducing current (71 µA), which keeps the bulb off or dim.
- Circuit 2 (with the power supply): The DC signal causes a steady current (187 mA) to flow after the inductor initially resists the current change, allowing the bulb to light up fully.

This demonstration highlights how inductors behave differently in AC (especially at high frequencies) and DC circuits. In AC, inductors resist current more strongly at higher frequencies, while in DC, once the current stabilizes, inductors allow full current flow.


CONTINUE WITH STEP BY STEP SCREEN CAPTURE FOR THE EXPERIMENT

No, a sine wave generator is not typically considered a power source for an electronic circuit. Instead, it is used to provide an alternating signal, often for testing, signal processing, or as an input to a circuit. A power source, on the other hand, supplies the energy needed to operate the circuit, typically in the form of a constant voltage or current, like a battery or power supply.

The sine wave generator can drive certain parts of the circuit, but it's not meant to power the entire system.

Yes, a sine wave generator can be used with an inductor and a bulb to demonstrate how an inductor behaves in an AC circuit. Here’s how:

1. AC Source:

The sine wave generator provides an alternating current (AC) signal to the circuit.

2. Inductor Behavior:

In an AC circuit, an inductor resists changes in current. As the frequency of the sine wave increases, the inductive reactance increases, reducing the current flow through the circuit.

3. Bulb:

The brightness of the bulb will change depending on the current through it. At low frequencies, the current will be higher, and the bulb will be brighter. At higher frequencies, the inductor’s reactance will limit the current, dimming the bulb.

This setup can effectively demonstrate the frequency-dependent behavior of inductors in AC circuits.

An AC source, like a sine wave generator, is not typically considered a general-purpose power source because it is designed to provide a varying signal rather than constant energy supply. While it generates alternating voltage and current, it is often used for signal generation and testing rather than providing the stable, continuous power needed to run most electronic circuits.

In contrast, a power source (like a battery or DC power supply) provides a steady voltage or current to power the components continuously. AC sources can power circuits but are usually intended for specific functions like driving motors or transformers, not powering entire electronic systems directly.
