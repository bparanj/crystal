Difficult with Tinkercad. Skip it.

PENDING

Move to out of scope folder

Here is the step-by-step setup for your RC circuit with clear terminal connections:

### Step 1: Connect the Resistor to the AC Power Source

- Take the AC power source and identify its positive terminal (P) and negative terminal (N).
- Connect one terminal of the resistor (R) (e.g., terminal R1) to the positive terminal (P) of the AC power source.

### Step 2: Connect the Resistor to the Capacitor

- Connect the other terminal of the resistor (R) (e.g., terminal R2) to one terminal of the capacitor (C) (e.g., terminal C1).

### Step 3: Complete the RC Circuit

- Connect the other terminal of the capacitor (C) (e.g., terminal C2) to the negative terminal (N) of the AC power source.

### Step 4: Add the First LED (Across the Resistor)

- Take an LED (LED1):
  - Connect the anode (A1) of LED1 to R1 (resistor terminal connected to the positive terminal of the AC power source).
  - Connect the cathode (K1) of LED1 to R2 (resistor terminal connected to the capacitor).


### Step 5: Add the Second LED (Across the Capacitor)

- Take another LED (LED2):
  - Connect the anode (A2) of LED2 to C1 (capacitor terminal connected to the resistor).
  - Connect the cathode (K2) of LED2 to C2 (capacitor terminal connected to the negative terminal of the AC power source).

### Summary of Connections

1. Resistor (R): \( R1 \to P \) and \( R2 \to C1 \).
2. Capacitor (C): \( C1 \to R2 \) and \( C2 \to N \).
3. LED1 (Across Resistor): \( A1 \to R1 \), \( K1 \to R2 \).
4. LED2 (Across Capacitor): \( A2 \to C1 \), \( K2 \to C2 \).

With this setup, the LEDs will indicate the voltage across the resistor (LED1, proportional to current) and the capacitor (LED2, showing voltage across it).

To demonstrate the voltage-current phase shift using an RC (Resistor-Capacitor) circuit in Tinkercad, you can set up a simple AC circuit. While Tinkercad doesn’t directly show phase shift with oscilloscopes, you can observe the effect by using LEDs to show the charging and discharging behavior.

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

PENDING

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

