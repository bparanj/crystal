PENDING

Can this done using Tinkercad

A simple audio coupling circuit demonstration that shows how a coupling capacitor passes audio signals while blocking DC.

Components:

1. 1µF coupling capacitor
2. 2N2222 transistor
3. 10kΩ resistor (bias)
4. 1kΩ resistor (collector)
5. 100Ω resistor (load)
6. 9V battery
7. Small speaker/piezo
8. Function generator (for input signal)

Experiment Steps:
1. Build the circuit in Tinkercad
2. Set function generator to:
   - 1kHz sine wave
   - 1V peak-to-peak

Measurements to make:
1. Without coupling capacitor:
   - Measure DC at input: ~0V
   - Measure DC at transistor base: 9V

2. With coupling capacitor:
   - Input signal passes through
   - DC voltage blocked
   - Transistor base bias maintained

Expected observations:
1. Audio signal passes through to speaker
2. DC battery voltage doesn't affect input stage
3. Using oscilloscope, you'll see:
   - Input: AC signal centered at 0V
   - Output: AC signal centered at transistor's bias point

This demonstrates how coupling capacitors:
- Pass the AC audio signal
- Block the DC bias voltage
- Allow separate stages to operate at different DC voltages
