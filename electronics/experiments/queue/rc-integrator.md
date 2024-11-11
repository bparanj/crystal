You can design a simple experiment to create and observe an RC Integrator Circuit in Tinkercad. An RC Integrator circuit produces an output voltage that represents the integral of the input signal over time, effectively “smoothing” it. Here’s a step-by-step guide to build and test this in Tinkercad.

### Components

1. Resistor: 1 kΩ
2. Capacitor: 10 µF
3. Function Generator: To provide an AC square wave signal (simulated with Tinkercad’s voltage source)
4. Oscilloscope: To observe the input and output waveforms (in Tinkercad, you can view the voltages over time with the multimeter in time-based display mode)
5. Breadboard and Connecting Wires

### Steps

1. Set Up the Breadboard:
   - Place the resistor (1 kΩ) and capacitor (10 µF) on the breadboard to form an RC series circuit.

2. Create the RC Integrator:
   - Connect the resistor to the positive terminal of the function generator (or voltage source in Tinkercad).
   - Connect the other end of the resistor to the positive end of the capacitor.
   - Connect the other end of the capacitor to the ground (negative terminal) of the function generator.
   - The output will be observed across the capacitor, as it integrates the input signal.

3. Set Up the Function Generator:
   - Set the function generator to produce a square wave with a low frequency, such as 100 Hz, and a peak voltage of 5V.
   - The square wave will serve as the input signal for the integrator.

4. Connect the Measurement Tool:
   - In Tinkercad, use the multimeter (in time-based voltage display mode) to observe the output voltage across the capacitor.

5. Run the Simulation and Observe Output:
   - Start the simulation in Tinkercad.
   - Observe the voltage across the capacitor. The output will show a smoother, ramp-like waveform instead of the sharp square wave input. This is due to the integrative effect of the RC circuit, which “smooths” the input signal.

### Expected Results

- Output Waveform: The output across the capacitor will resemble a triangular waveform when the input is a square wave. The capacitor charges and discharges gradually, integrating the changes in the square wave, which leads to a smooth, sloped waveform.
- When the input square wave is high, the capacitor charges, causing the output voltage to rise linearly. When the input square wave goes low, the capacitor discharges, causing the output to fall linearly.

- An RC Integrator circuit produces a smooth, integrated output when given a square wave input, demonstrating its role in smoothing or averaging signals.
- This circuit is a foundational concept for understanding signal processing, where integrators are used to create smooth waveforms or as basic elements in filters.

This simple experiment demonstrates how RC integrator circuits respond to changing input signals, highlighting their application in signal smoothing and filtering in electronic circuits.
