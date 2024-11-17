### Decoupling Inductor

A decoupling inductor is used in circuits to block or filter high-frequency noise while allowing low-frequency signals or DC to pass through. It works as a low-pass filter, ensuring that unwanted high-frequency interference does not propagate through power or signal lines.

### Concepts

1. Inductive Reactance:
   - The impedance of an inductor increases with frequency:
     \[
     X_L = 2\pi f L
     \]
     - At low frequencies (or DC), \( X_L \) is small, allowing current to pass.
     - At high frequencies, \( X_L \) becomes large, blocking high-frequency noise.

2. Decoupling Behavior:
   - The inductor blocks high-frequency noise from power supply lines or signal paths.
   - Often paired with a capacitor to form a pi-filter or LC filter.

3. Applications:
   - Power supply noise suppression.
   - Signal integrity improvement in high-speed digital and RF circuits.

### Experiment

#### Objective

To demonstrate how a decoupling inductor blocks high-frequency signals while allowing low-frequency signals or DC to pass.

#### Components

1. AC Voltage Source (\( V_{AC} = 5V_{peak}, f = 1kHz - 100kHz \)).
2. DC Voltage Source (\( V_{DC} = 5V \)).
3. Inductor (\( L = 10mH \)).
4. Resistor (\( R = 1k\Omega \)) as a load.
5. Capacitor (\( C = 10\mu F \)) for optional LC filtering.
6. Oscilloscope (to observe signals).
7. Breadboard and wires.

### Circuit

1. Voltage Source:
   - Combine the DC voltage source and AC voltage source to simulate a power line with superimposed noise.
   - Connect the combined source to one terminal of the inductor.

2. Decoupling Inductor:
   - Place the inductor (\( L \)) in series with the load resistor.

3. Load Resistor:
   - Connect one terminal of the load resistor (\( R \)) to the other end of the inductor.
   - Connect the other terminal of \( R \) to ground.

4. Oscilloscope Connections:
   - Channel 1: Monitor the input signal (combined AC + DC voltage).
   - Channel 2: Monitor the output signal across the load resistor.

### Steps

1. Set Input Signal:
   - Configure the AC voltage source to simulate noise with frequencies \( 1kHz, 10kHz, 50kHz, 100kHz \).
   - Combine it with the DC voltage source (\( V_{DC} = 5V \)).

2. Observe Input Signal:
   - Use Channel 1 of the oscilloscope to verify the combined signal with both AC and DC components.

3. Observe Output Signal:
   - Use Channel 2 to observe the signal across the load resistor.

4. Experiment with Frequencies:
   - Gradually increase the frequency of the AC source and note how the inductor blocks higher frequencies while allowing DC and low-frequency signals to pass.

5. Optional LC Filter:
   - Add a capacitor in parallel with the load resistor and observe enhanced filtering of high-frequency noise.

### Results

1. Low-Frequency Signals:
   - At \( f = 1kHz \), the output signal includes both DC and AC components with minimal attenuation.

2. High-Frequency Signals:
   - As \( f \) increases (e.g., \( 50kHz \), \( 100kHz \)), the output AC signal is significantly attenuated due to the inductor's high reactance.

3. Improved Filtering with LC:
   - Adding a capacitor in parallel with \( R \) forms an LC filter, further reducing high-frequency noise.

### Insights

1. Decoupling Performance:
   - The inductor effectively blocks high-frequency noise, ensuring clean DC power or low-frequency signal transmission.

2. Applications:
   - Widely used in power supply circuits to filter switching noise and in signal paths to suppress electromagnetic interference (EMI).

3. Design Considerations:
   - Choose \( L \) based on the required cutoff frequency (\( f_c \)) for effective decoupling:
     \[
     f_c = \frac{R}{2\pi L}
     \]

This experiment can be implemented in Tinkercad, allowing you to visualize the inductor's frequency-dependent behavior in suppressing high-frequency signals while passing low-frequency signals or DC components.
