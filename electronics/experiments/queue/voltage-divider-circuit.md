PENDING

Check the voltage divider experiment and extract anything from this to that document.

A basic voltage divider consists of two resistors connected in series across a voltage source, with the output voltage taken from the connection point between the two resistors.

A voltage divider resembles a water pipe with two constrictions in series. Just as the water pressure decreases after each constriction, the voltage drops across each resistor in the divider.

1) Get two resistors (e.g., 1kΩ and 2kΩ) and a 9V battery.
2) Connect the resistors in series:
 			attach one end of the 1kΩ resistor to the positive terminal of the battery.
3) Connect the other end of the 1kΩ resistor to one end of the 2kΩ resistor.
4) Connect the free end of the 2kΩ resistor to the negative terminal of the battery.
5) The voltage divider output is the point between the two resistors. Measure the voltage at this point with respect to the negative battery terminal.

You should observe a voltage of approximately 6V, which is 2/3 of the input voltage, as the 2kΩ resistor is 2/3 of the total resistance.

## Voltage division

A simple voltage division circuit is a fundamental electronic circuit that uses two resistors to create a lower voltage from a higher voltage source.

 Components:

 1. Two resistors (R1 and R2)
 2. Input voltage source (Vin)
 3. Output voltage (Vout)

 Circuit layout:

 1. R1 and R2 are connected in series
 2. Vin is applied across both resistors
 3. Vout is measured across R2

 ```
      Vin
       |
       R1
       |
 Vout ---|
       |
       R2
       |
      GND
 ```

How it works:

 1. The input voltage (Vin) is split across the two resistors
 2. The output voltage (Vout) is taken from the midpoint between R1 and R2
 3. Vout is always less than or equal to Vin

The relationship between Vin and Vout is given by the formula:

Vout = Vin * (R2 / (R1 + R2))

 1. The ratio of R1 to R2 determines the output voltage
 2. Changing the resistor values changes the output voltage
 3. The total current through both resistors remains constant
 4. This circuit is most effective when the load impedance is much higher than R2

Applications:

 1. Reducing voltage for sensors or low-voltage components
 2. Creating reference voltages
 3. Level shifting in signal processing
 4. Biasing in amplifier circuits

 This simple circuit is the basis for many more complex voltage division applications in electronics.

A simple experiment to illustrate the concept of voltage drop:

PENDING

This is the same as resistor in series experiment. See the voltage-divider-cirucit.md

### Objective:

To demonstrate how voltage decreases across components in a series circuit, illustrating the concept of voltage drop.

### Materials:

- A 9V battery or a DC power supply
- Two resistors of different values (e.g., 100 ohms and 200 ohms)
- A breadboard
- A multimeter to measure voltage
- Connecting wires

### Procedure:

1. Set Up the Circuit:

   - Connect the 9V battery to the breadboard.
   - Place the two resistors in series on the breadboard. Connect one end of the first resistor to the positive terminal of the battery.
   - Connect the free end of the first resistor to one end of the second resistor. Connect the free end of the second resistor to the negative terminal of the battery.

2. Measure the Total Voltage:

   - Use the multimeter to measure the total voltage across the two resistors. Place the multimeter probes across the positive terminal of the battery and the connection point between the second resistor and the negative terminal. Record this voltage, which should be approximately 9V.

3. Measure the Voltage Drop Across Each Resistor:

   - Measure the voltage drop across the first resistor (100 ohms). Place one probe of the multimeter on the positive terminal of the battery and the other probe on the junction between the two resistors. Record the voltage drop.
   - Measure the voltage drop across the second resistor (200 ohms). Place one probe on the junction between the two resistors and the other probe on the negative terminal of the battery. Record this voltage drop.

4. Compare the Voltage Drops:

   - Observe how the voltage drops across each resistor add up to the total voltage of the battery. Notice that the voltage drop across the 200-ohm resistor is higher than the voltage drop across the 100-ohm resistor. This demonstrates that the voltage drop is proportional to the resistance in a series circuit.

This experiment illustrates the concept of voltage drop in a simple series circuit. When resistors are connected in series, the total voltage supplied by the battery is divided among the resistors. The voltage drop across each resistor depends on its resistance, following Ohm’s Law (\( V = IR \)). The resistor with higher resistance (200 ohms) has a greater voltage drop compared to the resistor with lower resistance (100 ohms). This shows how voltage is used up as current flows through resistive elements in a circuit. The total voltage drop across all components in a series circuit will always equal the supply voltage.

Observations:

| Component           | Resistance (Ω) | Multimeter Lead Placement                                          | Measured Voltage Drop (V) |
|-------------------------|--------------------|------------------------------------------------------------------------|-------------------------------|
| Resistor 1 (R1)         | 100                | Place the red lead on the positive terminal of the battery; black lead on the junction between R1 and R2. |                               |
| Resistor 2 (R2)         | 200                | Place the red lead on the junction between R1 and R2; black lead on the negative terminal of the battery. |                               |
| Total (across R1 + R2)  | N/A                | Place the red lead on the positive terminal of the battery; black lead on the negative terminal of the battery. |                               |

Resistance (Ω):

Enter the resistance values for each resistor. In this experiment, Resistor 1 (R1) is 100 ohms, and Resistor 2 (R2) is 200 ohms.

Multimeter Lead Placement:

Position the red (positive) and black (negative) multimeter leads to measure the voltage drop across each component.

Measured Voltage Drop (V):

Measure and record the voltage drop across each component using the multimeter.
