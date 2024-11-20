experiment for audio coupling circuit:

### Circuit:

The coupling capacitor allows the AC audio signal from the function generator to pass to the transistor's base while blocking any DC components. This ensures the transistor base is biased correctly without interference from the audio signal's DC offset.

### Steps

#### 1. Components Setup:

- Power Supply:
  - Use a 9V battery for the circuit's DC bias.

- Biasing Resistor:
  - Connect a 10kΩ resistor from the positive terminal of the battery to the transistor's base.

- Transistor:
  - Use a 2N2222 transistor:
    - Collector: Connected to \( 9V \) through a 1kΩ resistor.
    - Emitter: Connected to ground.

- Load:
  - Use a 100Ω resistor in series with the small speaker or piezo at the collector.

- Coupling Capacitor:
  - Place a 1µF capacitor between the function generator and the transistor base.

- Function Generator:
  - Set to generate a 1kHz sine wave, 1V peak-to-peak.

### Circuit

1. Transistor Base Bias:
   - Connect the 10kΩ resistor between the base of the 2N2222 and the positive terminal of the 9V battery.

2. Coupling Capacitor:
   - Place the 1µF capacitor between the function generator output and the base of the transistor.

3. Collector Circuit:
   - Connect the collector of the transistor to the positive terminal of the battery via a 1kΩ resistor.
   - Connect a 100Ω resistor in series with the small speaker or piezo, and attach this network to the collector.

4. Emitter:
   - Connect the emitter of the transistor to ground.

5. Function Generator:
   - Connect the output of the function generator to the free terminal of the coupling capacitor.
   - Connect the ground of the function generator to the circuit ground.

### Steps:

#### Without the Coupling Capacitor:

1. Remove the coupling capacitor.
2. Connect the function generator output directly to the transistor's base.
3. Measure:
   - DC Voltage at Input (Function Generator): ~0V.
   - DC Voltage at Base (Transistor): \( ~9V \).

#### With the Coupling Capacitor:

1. Reintroduce the coupling capacitor between the function generator and transistor base.
2. Observe:
   - The AC audio signal passes through the capacitor to the transistor base.
   - The DC component of the signal is blocked.
   - The base remains correctly biased.

3. Use an oscilloscope to:
   - Measure the input signal (before the capacitor).
   - Measure the output signal across the speaker or piezo.
   - Confirm that the AC signal is coupled, and the transistor base DC bias is maintained.

### Observations:

1. Without Coupling Capacitor:
   - The transistor base is directly connected to the function generator's DC level.
   - The base is not properly biased, leading to improper transistor operation.

2. With Coupling Capacitor:
   - The coupling capacitor blocks DC from the function generator.
   - The AC signal is passed to the transistor base, maintaining proper DC bias for amplification.
   - The output across the speaker matches the amplified input signal, demonstrating coupling.

### Insights:

- The coupling capacitor ensures the AC audio signal is passed while maintaining the transistor's DC operating point.
- This setup demonstrates how coupling capacitors are used in amplifiers and audio circuits to isolate DC and pass AC signals.

This experiment is feasible in Tinkercad, and you can observe the described behavior by using its built-in oscilloscopes and function generators to measure signal waveforms and voltage levels.

PENDING

An audio coupling circuit demonstration that shows how a coupling capacitor passes audio signals while blocking DC.

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
