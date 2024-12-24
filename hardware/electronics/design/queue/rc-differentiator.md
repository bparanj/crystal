PENDING

Run the experiment

experiment to create and observe an RC Differentiator Circuit. This circuit will produce a voltage output that represents the rate of change of the input signal, effectively differentiating it.

### Components

1. Resistor: 1 kΩ
2. Capacitor: 100 nF
3. Function Generator: To provide an AC square wave signal (simulated using Tinkercad’s voltage source)
4. Oscilloscope: To observe the input and output waveforms (Tinkercad's multimeter can measure voltages, but you can simulate observing the waveforms by using Tinkercad's time-based voltage display)

### Steps

   - Place a resistor (1 kΩ) and a capacitor (100 nF) on the breadboard to form an RC series circuit.

   - Connect one end of the resistor to the positive terminal of the function generator (voltage source).
   - Connect the other end of the resistor to the positive end of the capacitor.
   - Connect the other end of the capacitor to the ground (negative terminal) of the function generator. This arrangement places the resistor in series with the input signal, with the capacitor connected to ground.

   - Place a probe (or connect a multimeter in Tinkercad) across the resistor to observe the differentiated output.

   - Set the function generator to produce a square wave with a low frequency, such as 100 Hz, and a peak voltage of 5V.
   - The square wave will serve as the input signal for the differentiator.

   - Start the simulation in Tinkercad.
   - Observe the voltage across the resistor. You should see sharp voltage spikes at the transitions of the square wave input (when it changes from low to high and high to low).
   - These spikes are the result of the differentiator circuit, showing the changes in the input signal’s slope.

### Results

The output across the resistor will show spikes whenever the input square wave transitions. These spikes represent the differentiation of the input signal, as the circuit responds to rapid changes in the input voltage.

When the input is steady (at the high or low level of the square wave), the output will remain close to zero, as there is no change in the input signal at those points.

An RC Differentiator circuit generates an output signal that highlights changes in the input signal.
In this setup, the differentiator circuit produces voltage spikes in response to the edges of the square wave, demonstrating its ability to differentiate a signal.

This experiment demonstrates how RC differentiator circuits respond to changing input signals, emphasizing their use in edge detection and pulse generation.
