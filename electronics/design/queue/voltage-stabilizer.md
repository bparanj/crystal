PENDING

Not able to see the noise in the oscilloscope. Move to out of scope

What should be the value of the time per division in the oscilloscope to see the noise in the output when capacitor is not yet connected? The frequency is set to 1 Hz.

### Setting the Time Per Division

To observe the noise at 1 Hz, the oscilloscope’s time per division should be chosen based on the signal's frequency and waveform period:

1. Signal Period:
   - The frequency of the noise is 1 Hz, so the period is:
     \[
     T = \frac{1}{f} = \frac{1}{1} = 1 \, \text{second}
     \]

2. Optimal Time Per Division:
   - A good practice is to set the time per division to capture at least one full cycle across 8–10 divisions of the oscilloscope display.
   - For a 1-second period, set the time per division to approximately:
     \[
     0.1 \, \text{seconds/division}
     \]

3. Adjustment Range:
   - Start with 0.1 s/div to view the overall waveform, and adjust up or down (e.g., 0.2 s/div or 50 ms/div) to see specific details of the fluctuations.

### Observing Noise Without the Capacitor

- At 0.1 s/div, you should clearly see the square wave fluctuations introduced by the function generator on the oscilloscope.

### Observing With the Capacitor

- After connecting the capacitor, the square wave fluctuations will smooth out, resulting in a more stable DC voltage line with reduced noise amplitude.

This experiment demonstrates the capacitor's role as a decoupling element, effectively filtering out low-frequency noise on a power supply.

To demonstrate the concept of a capacitor smoothing voltage fluctuations as a decoupling or bypass capacitor in Tinkercad, follow this experiment setup:

### Objective

Show how a capacitor can smooth out voltage fluctuations by acting as a decoupling capacitor across a power supply, helping to filter out noise and stabilize the voltage.

### Components

1. Capacitor (C) - 100 µF (electrolytic capacitor, polarized)
2. DC Power Supply - 9V
3. Resistor (R) - 1 kΩ (optional, to simulate load on the power supply)
4. Oscilloscope - To observe voltage fluctuations with and without the capacitor
5. Function Generator - To add noise to the power supply, simulating voltage fluctuations
6. Breadboard - For component connections

### Setup

1. Connect the 9V DC power supply across the breadboard's power and ground rails.
2. Connect the resistor from the positive power rail to ground. This will act as a load on the power supply.
3. Function Generator (Noise Source):
   - Set the function generator to produce a low-frequency square wave (e.g., 1 Hz) with a small amplitude (e.g., 1V peak-to-peak) to simulate power supply noise.
   - Connect the function generator's output to the positive rail to introduce fluctuating noise on the power supply.
4. Place the capacitor across the power supply rails (positive leg to the positive rail and negative leg to ground). This will act as a decoupling capacitor, helping to smooth out the fluctuations.
5. Connect the oscilloscope probes across the capacitor to observe the voltage on the positive rail.

### Procedure

1. Observe Without Capacitor:
   - Run the simulation with the capacitor removed from the circuit.
   - Observe the oscilloscope to see the fluctuating voltage (noise) caused by the function generator on the power supply rail.

2. Observe With Capacitor:
   - Now place the capacitor across the power and ground rails as described.
   - Run the simulation again and observe the oscilloscope. The fluctuations should be reduced as the capacitor smooths out the voltage by temporarily storing charge and releasing it when needed.

### Results

- Without Capacitor: The oscilloscope should show noticeable voltage fluctuations, corresponding to the noise introduced by the function generator.
- With Capacitor: The voltage fluctuations should reduce significantly, showing a more stable DC voltage as the capacitor acts to filter out noise.

This experiment demonstrates the role of a capacitor as a decoupling or bypass capacitor, smoothing out voltage fluctuations and stabilizing the power supply voltage by filtering out high-frequency noise.
