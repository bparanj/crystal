A first-order circuit typically includes a resistor and either a capacitor (RC circuit) or an inductor (RL circuit). These circuits are useful for understanding concepts like charging/discharging in RC circuits and current buildup/decay in RL circuits. Here, we’ll design an RC circuit experiment in Tinkercad to observe how a capacitor charges and discharges.

### Components:

1. DC Power Source: 5V DC source.
2. Resistor: 1 kΩ resistor.
3. Capacitor: 10 µF capacitor.
4. Switch: To control when the capacitor starts charging or discharging.
5. Oscilloscope: To observe the voltage across the capacitor.

### Setup:

1. Connect the Resistor and Capacitor in Series:
   - Connect one terminal of the resistor to the positive terminal of the 5V DC power source.
   - Connect the other terminal of the resistor to one terminal of the capacitor.

2. Complete the Circuit with the Switch:
   - Connect the other terminal of the capacitor to ground.
   - Place a switch in parallel with the capacitor. This switch will allow you to toggle between charging and discharging the capacitor.

3. Set Up the Oscilloscope:
   - Connect the oscilloscope probes across the capacitor (one probe on each terminal) to monitor the voltage across it as it charges and discharges.

### Steps:

1. Charging the Capacitor:
   - Close the switch to start the experiment. When the switch is closed, the DC voltage source is connected directly to the resistor-capacitor combination.
   - Observe the voltage across the capacitor on the oscilloscope.
   - Expected Outcome: The voltage across the capacitor will gradually increase from 0V to 5V following an exponential curve. This increase follows the formula \( V(t) = V_{source} \times (1 - e^{-\frac{t}{RC}}) \), where \( R \) is the resistance and \( C \) is the capacitance.

2. Discharging the Capacitor:
   - Once the capacitor is fully charged (reaches close to 5V), open the switch to disconnect the power source and allow the capacitor to discharge through the resistor.
   - Observe the voltage across the capacitor as it discharges.
   - Expected Outcome: The voltage across the capacitor will gradually decrease from 5V to 0V, following an exponential decay curve. This discharge follows the formula \( V(t) = V_{initial} \times e^{-\frac{t}{RC}} \).


Charging Phase:

When the switch is closed, the capacitor starts charging through the resistor. The rate of charging is governed by the time constant \( \tau = RC \), which determines how quickly the voltage across the capacitor approaches the supply voltage.

Discharging Phase:

When the switch is opened, the capacitor discharges through the resistor. The discharge rate also follows the time constant \( RC \), dictating how quickly the voltage across the capacitor drops to zero.

### Observing the Time Constant (τ):

The time constant \( \tau = RC \) is the time it takes for the capacitor to charge up to approximately 63% of the supply voltage or discharge to about 37% of its initial voltage.
By observing the charging and discharging curves on the oscilloscope, you can estimate \( \tau \) and see the exponential nature of the process.

This experiment in Tinkercad demonstrates a first-order RC circuit, allowing you to visualize the charging and discharging behavior of a capacitor and understand the time constant's effect on circuit response. This experiment is foundational for understanding timing, filtering, and transient response in electronics.
