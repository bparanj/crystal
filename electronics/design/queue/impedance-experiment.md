PENDING SEARCH

- Search for youtube video for this experiment

A simple experiment to illustrate the concept of impedance:

PENDING REVISION

- Review the following experiments and revise them

To demonstrate how impedance affects the flow of alternating current (AC) in a circuit containing resistive and reactive components (inductors or capacitors).

### Needed:

- A resistor (e.g., 100 ohms)
- An inductor (e.g., 10 mH) or a capacitor (e.g., 10 µF)
- A function generator or AC power source
- An oscilloscope or multimeter set to measure AC voltage
- Connecting wires
- Breadboard (optional)

### Procedure:

   - Create a simple series circuit by connecting the resistor and the inductor (or capacitor) in series. Connect this series combination to the function generator or AC power source. If using an oscilloscope, connect its probes across the resistor to measure the voltage.

   - Set the function generator to produce a sine wave at a low frequency (e.g., 100 Hz). Observe the voltage across the resistor using the oscilloscope or multimeter. Record this voltage.

   - Gradually increase the frequency of the AC signal from the function generator (e.g., up to 1 kHz or higher). Observe how the voltage across the resistor changes as the frequency increases.

   - If possible, switch the function generator to produce a DC signal and observe the voltage across the resistor again. Notice the difference in voltage behavior between DC and varying AC frequencies.

This experiment illustrates how impedance affects the current flow in an AC circuit. The resistor offers a constant resistance to the current, but the inductor or capacitor introduces reactance, which changes with frequency. As the frequency of the AC signal increases, the impedance of the inductor increases (or the impedance of the capacitor decreases), which in turn affects the voltage drop across the resistor. This change demonstrates that impedance in AC circuits is not just resistance; it also includes the frequency-dependent reactance of inductors and capacitors. This experiment provides a clear visualization of how impedance influences the behavior of AC circuits and why it is important in designing and analyzing such systems.

In Tinkercad, this exact setup to demonstrate impedance effects on AC flow is partially feasible but limited due to the platform’s lack of certain components and features.

### Steps to Approximate the Circuit in Tinkercad

   - Resistor: Use a 100-ohm resistor.
   - Capacitor: Use a 10 µF capacitor. Tinkercad doesn’t support inductors, so the demonstration will be limited to resistive-capacitive (RC) impedance effects.
   - AC Source: Tinkercad doesn’t have a true function generator, but you can use an AC power source to simulate an AC signal.
   - Multimeter: Tinkercad provides a multimeter, but it lacks an oscilloscope to visualize the waveform directly.

   - Place the 100-ohm resistor and 10 µF capacitor in series.
   - Connect this series circuit to the AC power source (found under the "Components" in Tinkercad).
   - Connect the multimeter across the resistor to measure the AC voltage.

   - Set the AC power source to a low frequency, such as 100 Hz. Observe the AC voltage across the resistor with the multimeter. This will represent the initial current flow at low frequency.
   - Increase the frequency of the AC source to simulate how a change in frequency affects the impedance and the voltage across the resistor. Note any changes in multimeter readings.
   - Tinkercad doesn’t allow switching to DC or adjusting frequencies dynamically, so observations will be limited to static frequency changes by editing the AC source properties manually.

### Limitations

- No Inductor or True Oscilloscope: Without an inductor, only capacitive impedance can be demonstrated. The lack of an oscilloscope also means the waveform shape and phase shift can’t be directly visualized.
- Frequency Adjustment Limitations: Tinkercad does not allow for real-time frequency adjustments or waveform observations, so experimentation with different frequencies is limited.

This provides a basic understanding of capacitive reactance in an AC circuit but doesn’t fully capture the impedance behavior with varying AC frequencies. A more advanced simulator would be needed for detailed exploration with inductors and an oscilloscope.

Experiment:

Materials:

- 9V battery
- Battery clip
- Breadboard
- LED
- 220-ohm resistor
- 100-ohm resistor
- 10 µF capacitor
- Jumper wires
- Multimeter (optional, for measurements)

Setup:

1. Set up three parallel circuits on the breadboard:

   a) LED with 220-ohm resistor
   b) LED with 100-ohm resistor
   c) LED with 100-ohm resistor and 10 µF capacitor in series

2. Connect the 9V battery to power all three circuits.

Procedure:

1. Observe the brightness of the LED in each circuit.
2. If using a multimeter, measure the voltage across each LED.
3. Disconnect and reconnect the battery, paying attention to how quickly each LED lights up.

Expected results:

1. Circuit (a) will have moderate LED brightness due to the higher resistance.
2. Circuit (b) will have the brightest LED due to lower resistance.
3. Circuit (c) will have an interesting behavior:
   - When first connected, the LED will be dim or off.
   - It will slowly brighten to match circuit (b)'s brightness.
   - When disconnecting and reconnecting quickly, you may notice a delay in the LED lighting up.

This experiment demonstrates different aspects of impedance:

1. Circuits (a) and (b) show how resistance affects current flow and, consequently, LED brightness.

2. Circuit (c) illustrates the effect of capacitive reactance, a component of impedance:

   - The capacitor initially acts like an open circuit, blocking current flow.
   - As it charges, it allows more current to pass, brightening the LED.
   - This time-dependent behavior is characteristic of reactive impedance.

3. The delay in circuit (c) when reconnecting demonstrates how impedance can affect the timing of electrical responses.

This experiment helps visualize how impedance is more than just resistance. It shows how reactive components (like capacitors) can create time-dependent and frequency-dependent effects in circuits, which is a key aspect of impedance in AC circuits.

To extend this experiment, use different capacitor values or add an inductor to explore inductive reactance as well. You could also use an oscilloscope to visualize the voltage changes across the capacitor over time.
