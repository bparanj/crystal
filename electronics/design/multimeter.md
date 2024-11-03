You cannot use a multimeter in parallel with the load to measure current because a multimeter, when set to measure current (ammeter mode), has a very low internal resistance. Connecting it in parallel would cause several problems:

1. Incorrect Measurement:

   - Current Division: In parallel, the current from the power source would split between the multimeter and the load. Due to the multimeter’s low resistance, most of the current would flow through the multimeter instead of the load. This means the multimeter would not accurately measure the current flowing through the  load.

2. Potential Damage to the Multimeter:

   - Excessive Current: Because the multimeter in ammeter mode is designed to measure current flowing through it, connecting it in parallel can cause a very high current to flow through the multimeter. This can easily exceed the multimeter’s maximum current rating, potentially damaging the multimeter’s internal fuse or circuitry.

3. Circuit Alteration:

   - Disturbing the Circuit Operation: Placing a low-resistance device (the multimeter in ammeter mode) in parallel with the load effectively changes the circuit’s behavior by creating a new, unintended path for the current. This could alter the performance and functioning of the entire circuit.

### Correct Usage:

- Current Measurement: 

To correctly measure current, the multimeter should be connected in series with the load, not in parallel. This ensures that all current flowing through the load also flows through the multimeter, allowing it to accurately measure the current.

- Voltage Measurement: 

For voltage measurements, a multimeter is placed in parallel with the component or section of the circuit across which you want to measure the voltage, because it is designed to have a high internal resistance in this mode, minimizing the impact on the circuit.

TAG

voltage
current
multimeter
