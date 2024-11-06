To design a band-pass filter experiment using Tinkercad, you can create a simple RC-RC band-pass filter. This filter allows a specific range of frequencies to pass while attenuating frequencies outside this range.

### Objective

Create an RC-RC band-pass filter to observe how it selectively allows a certain frequency range to pass and attenuates frequencies above and below this range.

### Components

1. Resistors (R1 and R2) - 10 kΩ each (or suitable values to set the desired frequency range)
2. Capacitors (C1 and C2) - 0.1 µF each
3. Signal Generator - To provide variable frequency signals (use the Function Generator in Tinkercad)
4. Oscilloscope - To observe the input and output signals
5. Breadboard - For connecting components

### Setup

1. Connect the First RC High-Pass Stage:
   - Connect the capacitor \( C1 \) in series with the signal generator's output.
   - Connect the resistor \( R1 \) from the other side of \( C1 \) to ground. This creates a high-pass filter with a cutoff frequency defined by \( f_{c1} = \frac{1}{2\pi R_1 C_1} \).

2. Connect the Second RC Low-Pass Stage:
   - Place another resistor \( R2 \) after the first stage (at the junction after \( C1 \) and \( R1 \)).
   - Connect the second capacitor \( C2 \) from the other end of \( R2 \) to ground. This creates a low-pass filter with a cutoff frequency defined by \( f_{c2} = \frac{1}{2\pi R_2 C_2} \).

3. Connect Oscilloscope Probes:
   - Place the oscilloscope probe at the input (signal generator output before the first capacitor) to monitor the input signal.
   - Place another oscilloscope probe at the output (junction between \( R2 \) and \( C2 \)) to monitor the output signal.

### Procedure

1. Set Signal Generator: Start with a low-frequency signal (e.g., 10 Hz) and a small amplitude (e.g., 5V peak).
2. Observe Input and Output Signals: Check both signals on the oscilloscope.
3. Increase Frequency: Gradually increase the frequency (e.g., 100 Hz, 1 kHz, 5 kHz, 10 kHz, etc.).
4. Record Observations: Note how the amplitude of the output signal changes compared to the input as the frequency increases.

### Expected Results

- At frequencies below the high-pass cutoff frequency \( f_{c1} \), the output signal should be attenuated.
- As you approach the passband (between \( f_{c1} \) and \( f_{c2} \)), the output signal should have a higher amplitude.
- At frequencies above the low-pass cutoff frequency \( f_{c2} \), the output signal should again be attenuated.

This experiment demonstrates that an RC-RC band-pass filter allows only a specific range of frequencies to pass, attenuating signals outside this range.
