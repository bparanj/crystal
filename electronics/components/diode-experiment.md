PENDING

Is this already in existing experiment?
Move this to experiments folder. Or merge it to any existing experiment.

A simple experiment to demonstrate the problem caused by not using a diode involves a DC motor connected to a power supply without a flyback diode. This setup shows how voltage spikes from the motor can damage other components when the diode is missing.

### Materials:

- Small DC motor (e.g., a 5V or 9V motor)
- Power supply (matching the motor's voltage rating)
- LED (to act as a sensitive component that could be damaged)
- Resistor (appropriate for the LED, e.g., 220Ω)
- Connecting wires
- (Optional) Multimeter to measure voltage spikes

### Steps:

1. Connect the Circuit Without a Diode:

   - Connect the DC motor in series with an LED and resistor to the power supply.
   - The circuit should be: Power supply -> Motor -> Resistor -> LED -> Power supply.

2. Run the Motor:

   - Turn on the power supply so the motor starts running, which causes current to flow through the LED.

3. Disconnect the Power Suddenly:

   - While the motor is running, suddenly disconnect the power supply by opening the circuit.

4. Observe the LED:

   - The motor, when disconnected, produces a voltage spike (back EMF) because it acts as a generator for a moment. This spike can cause the LED to flash or even burn out, depending on its intensity.

5. Add a Flyback Diode and Repeat:

   - Connect a diode in parallel with the motor, with the diode’s cathode to the positive motor terminal and anode to the negative.
   - Run the motor again, then disconnect the power as before.
   - Observe that the LED no longer flashes or is at less risk of damage.

Without the diode, the motor generates a reverse voltage spike that passes through the LED, potentially damaging it. With the diode in place, the spike is absorbed by the diode, protecting the LED. This experiment demonstrates the importance of using a diode for voltage spike protection in circuits with inductive loads.
