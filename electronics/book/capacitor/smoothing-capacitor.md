Capacitor for Smoothing Pulsating DC 

Here's a simple Tinkercad experiment to demonstrate the capacitor's smoothing function:

1. Build a basic rectifier circuit:

- Connect diode to convert AC to pulsating DC
- Measure output with multimeter/oscilloscope

2. Run two scenarios:
   - Without capacitor: You'll see LED blinking/flickering
   - With capacitor (100-1000µF) parallel to LED: The light becomes steady

This demonstrates how capacitors smooth pulsating DC by storing and releasing energy during voltage peaks and dips.

Components:

1. AC Voltage Source: 9V peak, 60Hz
2. Diode: 1N4007
3. Resistor: 330Ω
4. LED: Red (standard)
5. Capacitor: 470µF electrolytic
6. Oscilloscope or Voltmeter for measurement

Circuit Connections:

1. Without Capacitor:
   - AC source positive → Diode anode
   - Diode cathode → Resistor
   - Resistor → LED anode
   - LED cathode → AC source negative

2. With Capacitor (add to above):
   - Connect capacitor positive terminal to diode cathode
   - Connect capacitor negative terminal to AC source negative

Steps:

1. Build circuit without capacitor first
2. Observe LED brightness/flicker
3. Add capacitor in parallel with LED
4. Observe difference in LED brightness
5. Use oscilloscope to see:
   - Pulsating DC without capacitor
   - Smoothed DC with capacitor

Results:

- Without capacitor: LED blinks at 60Hz
- With capacitor: LED stays steady
- Oscilloscope will show smoothed voltage with reduced ripple after adding capacitor

