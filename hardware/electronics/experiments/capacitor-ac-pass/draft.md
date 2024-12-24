
Demonstrate how a capacitor blocks direct current (DC) but allows alternating current (AC) to pass through.

Capacitors block DC but allow AC to pass by continuously charging and discharging in response to the alternating voltage. This property demonstrates the capacitor's **reactive behavior** in AC circuits.

With AC, The LED or bulb lights up, indicating that the capacitor allows AC to pass by continuously charging and discharging with the alternating voltage.

Alternating current continuously changes direction, allowing the capacitor to charge and discharge, effectively enabling current to "pass through."

Capacitors are used in AC circuits for signal coupling, filtering, and timing applications.
The principle is applied in designing circuits like high-pass filters and AC coupling in audio and RF systems.

This experiment demonstrates capacitor's basic behavior in AC circuits.

### **Experimenting with Frequency and DC Offset**

#### Lower Frequency (e.g., 100 Hz)

- Reduce the frequency of the function generator to **100 Hz**.
- Observe the LED blinking or dimming as the capacitor charges and discharges more slowly, reducing the average current through the LED.

#### Add DC Offset

- Increase the DC offset of the function generator to **2V**.
- Observe the LED lighting more steadily because the capacitor now passes both AC and the added DC component.

#### Remove AC Component

- Set the function generator to output only DC (remove AC).
- Observe the LED turning off, as the capacitor blocks pure DC once charged.

### **Observations**

1. **Initial State:**
   - At the start, the capacitor is uncharged and acts like a short circuit for AC, allowing current to flow freely.
   - The LED lights brightly.

2. **Steady State:**
   - As the capacitor charges with the AC signal, it develops a voltage across its terminals, reducing the current flow.
   - The LED appears dimmer or blinks at the AC frequency.

3. **DC Behavior:**
   - The capacitor blocks steady DC signals after charging, preventing the LED from lighting.

This experiment demonstrates the AC-coupling property of capacitors:
- **AC Signals:** Capacitors continuously charge and discharge with alternating voltage, allowing AC signals to pass through.
- **DC Signals:** Capacitors block steady DC after charging, highlighting their role in filtering.

Capacitors are used in circuits where AC signals need to pass while DC components are filtered out, such as in audio systems, signal processing, and power supplies. The experiment provides a demonstration of this behavior, with the LED as a visual indicator.

Capacitors block DC after they charge, as no steady current flows through it. However, in AC circuits, the changing voltage continuously charges and discharges the capacitor, allowing current to flow.

The capacitor allows AC signals to pass, lighting the LED. Reducing the frequency shows how slower charging and discharging cycles impact the LED's behavior. The capacitor’s role in filtering DC signals becomes clear when the DC offset is added or removed.

### Demonstrate Capacitor Passing AC Signal

This experiment shows how a capacitor allows AC signals to pass through the circuit but blocks DC signals.

1. Function Generator
2. LED
3. Capacitor: 100 µF (non-polarized is ideal, but polarized can be used with correct polarity)
4. Resistor: 330 Ω (to protect the LED)

   - Connect the other terminal of the resistor to the anode (long leg) of the LED.
   - Connect the cathode (short leg) of the LED to the negative rail of the breadboard.

   - The function generator acts as the signal source, so no external DC power supply is needed.

1. Set the function generator to:
   - Waveform: Sine wave.
   - Frequency: 1 kHz (or a similar low frequency for easier observation).
   - Amplitude: 5V peak-to-peak.
   - DC Offset: 0V (pure AC signal).

### Procedure

   - Run the simulation in Tinkercad.
   - The LED will blink rapidly or appear dim, as the AC signal passes through the capacitor.

2. Experiment with DC Offset:
   - Change the DC offset of the function generator to a positive value (e.g., 2V).
   - Observe how the LED lights up continuously because the capacitor now passes the AC signal combined with the DC offset.

3. Remove the AC Component:
   - Set the function generator to output only DC (remove the AC component).
   - Observe that the LED turns off, showing that the capacitor blocks pure DC signals.


- The capacitor blocks DC and allows AC to pass by continuously charging and discharging in response to the alternating voltage. The LED lights up when the capacitor passes the AC signal but remains off for pure DC.

This experiment demonstrates the AC-coupling property of a capacitor.

The LED is bright initially and then becomes dim because the capacitor charges over time, reducing the current flow through the circuit. Here’s why this happens:

1. Initial State:
   - When the circuit starts, the capacitor is uncharged, and it acts like a short circuit for the AC signal.
   - A high current flows through the circuit, lighting the LED brightly.

2. Charging Phase:
   - As the capacitor charges, it develops a voltage across its plates, opposing the flow of current.
   - Over time, the capacitor reaches a steady-state charge for the applied signal, reducing the effective current passing through the LED.

3. Steady State:
   - Once the capacitor is fully charged for DC components (or at equilibrium for AC signals), it blocks further DC current while allowing only the AC component of the signal to pass.
   - The reduced current through the LED makes it appear dimmer.

### Factors

- Capacitor Size: Larger capacitance takes longer to charge but can smooth out the signal more effectively.
- Frequency of Signal: At lower frequencies, the capacitor charges and discharges more slowly, affecting the LED's brightness.

### How to Observe Pure AC Behavior

To keep the LED brightness consistent:
- Ensure the signal is purely AC (set the function generator's DC offset to 0V).
- Use a smaller capacitor value (e.g., 10 µF) to reduce the charging time and focus on the AC response.

This behavior demonstrates the charging and discharging dynamics of the capacitor and its role in filtering DC components while passing AC.
