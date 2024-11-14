A band-pass filter experiment using a simple RC-RC band-pass filter. This filter allows a specific range of frequencies to pass while attenuating frequencies outside this range.

PENDING

Find a circuit diagram online

### Objective

Create an RC-RC band-pass filter to observe how it selectively allows a certain frequency range to pass and attenuates frequencies above and below this range.

### Components

1. Resistors (R1 and R2) - 10 kΩ each (sets the desired frequency range)
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

### Results

- At frequencies below the high-pass cutoff frequency \( f_{c1} \), the output signal should be attenuated.
- As you approach the passband (between \( f_{c1} \) and \( f_{c2} \)), the output signal should have a higher amplitude.
- At frequencies above the low-pass cutoff frequency \( f_{c2} \), the output signal should again be attenuated.

This experiment demonstrates that an RC-RC band-pass filter allows only a specific range of frequencies to pass, attenuating signals outside this range.

Yes, seeing a sawtooth-like output from a square wave input suggests that your band-pass filter is working as intended. Here’s why:

1. Square Wave Composition:
   - A square wave consists of a fundamental frequency and a series of odd harmonics (higher frequencies).
   
2. Band-Pass Filtering Action:
   - The high-pass filter removes the DC component and very low frequencies, which smooths out the flat parts of the square wave.
   - The low-pass filter attenuates higher harmonics, which normally create the sharp transitions in a square wave.
   
3. Resulting Sawtooth Shape:
   - With only the mid-range harmonics passing through, the sharp edges of the square wave are softened.
   - This creates the rounded, sawtooth-like shape in the output, as the filter has smoothed out the waveform by removing extreme high and low frequencies.

This curvy sawtooth output confirms that your band-pass filter is correctly filtering out both very low and very high frequencies, leaving only the middle range, which produces the observed waveform shape.

With a square wave input and the observed curvy sawtooth output, your circuit's band-pass filter is reshaping the waveform. Here’s why this happens and how to set the oscilloscope:

### Why the Output Looks Like a Curvy Sawtooth

1. Square Wave Input:
   - A square wave is composed of a fundamental frequency plus many higher-frequency harmonics.
   
2. Band-Pass Filtering:
   - The high-pass filter stage removes lower frequencies below its cutoff, including the DC component and some lower harmonics.
   - The low-pass filter stage removes frequencies above its cutoff, reducing higher harmonics.
   - This results in a waveform that retains only the mid-range harmonics, producing a curvy sawtooth shape instead of a square shape. This is due to the filtering out of sharp transitions, leaving smoother transitions that approximate a sawtooth.

### Setting Time per Division for the Oscilloscopes

#### 1. Calculate the Input Signal Period:
   - If the input square wave frequency is, for example, 1 kHz, its period \( T \) is 1 ms.

#### 2. Oscilloscope Time per Division Setting:
   - For the input square wave, set the time per division to 500 μs or 200 μs. This setting will let you see 2–5 cycles of the square wave clearly.
   - For the output (curvy sawtooth), use the same time per division as the input, starting with 500 μs per division.
   
If you want to analyze one cycle in detail, set a longer time per division (e.g., 1 ms per division). This setup will help visualize how the filter stages are shaping each transition of the square wave into the sawtooth pattern.

To set the time per division for the input and output oscilloscopes, you should base it on the frequency of the signal and the behavior of the filter.

### Step-by-Step Guide for Setting Time per Division

1. Determine the Input Signal Frequency:
   - Let’s assume the input signal is a sine wave with a known frequency \( f \) (e.g., 1 kHz).

2. Calculate the Period of the Signal:
   - The period \( T \) of a 1 kHz signal is:
     \[
     T = \frac{1}{f} = \frac{1}{1000 \text{ Hz}} = 1 \text{ ms}
     \]

3. Set Time per Division Based on Period:
   - A good rule of thumb is to set the time per division so that one or two full cycles of the waveform fit across the oscilloscope screen.
   - For a 1 kHz signal (1 ms period), setting the time per division to 200 μs or 500 μs would allow you to see 2–5 cycles on the screen, which is generally ideal for observing filter effects.

4. Suggested Time per Division:
   - Input Oscilloscope: Start with 500 μs per division if the input frequency is around 1 kHz. Adjust as necessary to see a full cycle or multiple cycles clearly.
   - Output Oscilloscope: Use the same 500 μs per division setting for consistency, especially if the output waveform is expected to be similar in frequency but altered in amplitude or phase.

If you’re observing frequencies much higher or lower than 1 kHz, adjust the time per division accordingly (e.g., for 10 kHz, use 50 μs per division; for 100 Hz, use 5 ms per division). This setup provides a clear view of how the filter affects both the input and output signals.

To help you understand the second step more clearly, let's break it down.

### Step-by-Step Explanation of the Second Stage (Low-Pass Filter)

1. Location of the Second Stage:
   - After creating the first high-pass filter stage (using \( C1 \) and \( R1 \)), you’ll have a point where the first resistor \( R1 \) connects to ground, and the other side of \( C1 \) has the filtered signal from the first stage.
   - This point, where the first high-pass stage ends, becomes the input for the second stage.

2. Connecting \( R2 \) (Second Stage Resistor):
   - Take a second resistor \( R2 \) and connect one end to the output of the first stage (the junction between \( C1 \) and \( R1 \)). This will allow the signal from the first stage to pass through \( R2 \) and into the second stage.

3. Connecting \( C2 \) (Second Stage Capacitor):
   - Connect the other end of \( R2 \) to one end of a capacitor \( C2 \).
   - The other end of \( C2 \) should then connect to ground. This setup completes the low-pass filter.

4. Resulting Low-Pass Filter:
   - The combination of \( R2 \) and \( C2 \) forms a low-pass filter that will allow frequencies lower than the cutoff frequency \( f_{c2} = \frac{1}{2\pi R_2 C_2} \) to pass, while higher frequencies will be attenuated.
   - The point between \( R2 \) and \( C2 \) is your output for this two-stage filter circuit.

### How the Full Circuit Works

- First Stage (High-Pass): Filters out lower frequencies, allowing higher frequencies to pass through.
- Second Stage (Low-Pass): Filters out higher frequencies, allowing lower frequencies from the high-pass output to pass.

This two-stage configuration is known as a band-pass filter because it combines a high-pass and a low-pass filter in series, allowing only a specific range of frequencies (the band between the two cutoff frequencies) to pass through.
