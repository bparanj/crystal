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

1. Power Supply: Connect the 9V DC power supply across the breadboard's power and ground rails.
2. Resistor (Load): Connect the resistor from the positive power rail to ground. This will act as a load on the power supply.
3. Function Generator (Noise Source):
   - Set the function generator to produce a low-frequency square wave (e.g., 1 Hz) with a small amplitude (e.g., 1V peak-to-peak) to simulate power supply noise.
   - Connect the function generator's output to the positive rail to introduce fluctuating noise on the power supply.
4. Capacitor Placement:
   - Place the capacitor across the power supply rails (positive leg to the positive rail and negative leg to ground). This will act as a decoupling capacitor, helping to smooth out the fluctuations.
5. Oscilloscope Connections:
   - Connect the oscilloscope probes across the capacitor to observe the voltage on the positive rail.

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
