To demonstrate the voltage-current phase shift using an RC (Resistor-Capacitor) circuit in Tinkercad, you can set up a simple AC circuit. While Tinkercad doesn’t directly show phase shift with oscilloscopes, you can observe the effect by using LEDs to show the charging and discharging behavior.

### Objective:

To show the phase shift between voltage and current in an RC circuit.

### Components:

- 1 AC Power Source (e.g., 5V AC source)
- 1 Resistor (e.g., 1 kΩ)
- 1 Capacitor (e.g., 100 μF)
- 2 LEDs (to show charging and discharging behavior)
- Breadboard and Wires

### Steps:

1. Set Up the AC Power Source:
   - Place a 5V AC power source on the breadboard.

2. Create the RC Circuit:
   - Connect one terminal of the AC power source to one end of the 1 kΩ resistor.
   - Connect the other end of the resistor to one end of the 100 μF capacitor.
   - Connect the other end of the capacitor to the other terminal of the AC power source.

3. Add LEDs to Show Phase Behavior:
   - Place one LED in parallel with the resistor (to indicate the voltage across the resistor, which corresponds to current through the circuit).
   - Place the second LED in parallel with the capacitor (to indicate the voltage across the capacitor).

4. Observe the Phase Shift:
   - When you start the simulation, you should see the LEDs flickering with the AC source. 
   - Notice that the LED across the resistor (indicating current) lights up slightly out of sync with the LED across the capacitor (indicating voltage).
   - This phase difference demonstrates that in an RC circuit, the current and voltage are not perfectly in phase. The current through the resistor leads the voltage across the capacitor, creating a phase shift.

In an AC RC circuit, the voltage across the capacitor lags behind the current through the resistor due to the time it takes for the capacitor to charge and discharge. This lag causes a phase shift, where the current and voltage are no longer aligned in time.

In this RC phase shift experiment:

1. The Resistor (Current-Related Component):
   - The voltage across the resistor is proportional to the current flowing through the circuit, as per Ohm’s Law (\( V = IR \)). 
   - Therefore, the resistor voltage indicates the phase of the current in the circuit.
   - The LED across the resistor will light up in sync with the current, making it the current-related component in this setup.

2. The Capacitor (Voltage-Related Component):
   - The capacitor stores and releases charge, causing the voltage across it to build up and lag behind the current. 
   - The voltage across the capacitor represents the phase of the voltage in the circuit.
   - The LED across the capacitor will light up slightly out of phase with the LED across the resistor, showing the voltage behavior over time. This makes it the voltage-related component.

- Resistor: Represents the current phase.
- Capacitor: Represents the voltage phase.

This difference in the behavior of the LEDs shows the phase shift between current and voltage in the RC circuit.
