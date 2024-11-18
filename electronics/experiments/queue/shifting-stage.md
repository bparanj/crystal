
To observe how a resistor in series with a DC voltage source causes a voltage shift when supplied with a constant current from a current source.

### Components

1. DC Voltage Source (e.g., 5V)
2. Resistor (e.g., 1 kΩ)
3. Constant Current Source (simulate with a current-controlled source or an adjustable power supply with current-limiting capability)
4. Multimeter (to measure output voltage)
5. Breadboard
6. Connecting wires

### Circuit

1. Set Up the DC Voltage Source:
   - Place a 5V DC voltage source on the breadboard.
   - Label its terminals as 1a (positive) and 1b (negative).

2. Add the Resistor:
   - Connect one end of the resistor to 1a.
   - Label the resistor's other terminal as 2a.

3. Connect the Current Source:
   - Connect the positive terminal of the current source to 2a (resistor's free terminal).
   - Connect the negative terminal of the current source to 1b (negative of the voltage source).

4. Add a Multimeter:
   - Place a multimeter across 2a and 1b to measure the output voltage.

### Steps:

   - Set the DC voltage source to 5V.
   - Set the current source to supply a constant current, e.g., 1 mA.

   - Observe the multimeter reading to measure the combined voltage.

   - Change the resistor value (e.g., to 2 kΩ or 500 Ω) or adjust the current (e.g., 2 mA) in the current source.
   - Observe how the voltage across the resistor shifts the output voltage.

### Observations:

1. Voltage Shift:
   - When the current increases, the voltage across the resistor (\( V_R = I \cdot R \)) increases, causing the output voltage to increase (if in series with the positive terminal).

2. Adjustable Behavior:
   - Changing the resistor value or current demonstrates how the output voltage can be tuned.

### Insights:

- This setup demonstrates how a resistor and current source influence a DC voltage.
- Use Tinkercad's simulation tools to observe voltage changes dynamically as you adjust values.

In a circuit with a voltage source (Vin), resistor (R), and current source (I) in series:

1. The current source forces a constant current (I) through the circuit
2. By Ohm's Law, the voltage across the resistor (VR) is:
   VR = I × R

3. The output voltage (Vout) will be:
   Vout = Vin - VR = Vin - (I × R)

This configuration effectively "shifts" or "moves" the input voltage down by I×R volts. The current source maintains constant current regardless of voltage changes, making this useful for level shifting and biasing applications.

Steps to recreate in Tinkercad:

1. Add 5V DC source
2. Connect 1kΩ resistor in series
3. Add 2mA current source
4. Add multimeter to measure:
   - Input voltage (5V)
   - Voltage across resistor (2V)
   - Output voltage (3V)
5. Expected measurements verify V = IR: 2mA × 1kΩ = 2V drop

When a DC voltage source is connected in series with a resistor, and a current source is supplying current, the voltage across the resistor will shift or "move" the original voltage according to Ohm's Law:

\[ V_R = I \cdot R \]

### Concepts:

1. Voltage across the resistor (V_R):
   The current supplied by the current source (\(I\)) flows through the resistor (\(R\)), creating a voltage drop.

2. Resultant voltage:
   The new voltage at the terminal connected to the resistor depends on whether the resistor is connected to the positive or negative terminal of the DC voltage source:

   - Positive terminal side:
     The output voltage increases if the current flows from the DC source's positive terminal, as:
     \[ V_{out} = V_{source} + V_R \]

   - Negative terminal side:
     The output voltage decreases if the current flows towards the DC source's negative terminal, as:
     \[ V_{out} = V_{source} - V_R \]

3. Current source role:
   The current source ensures a constant current (\(I\)) through the resistor, making the voltage shift predictable based on the resistor's value.

### Application:

This setup is often used in circuits for biasing or offsetting a signal, where the resistor transforms the input voltage by an amount proportional to the current supplied by the current source.

