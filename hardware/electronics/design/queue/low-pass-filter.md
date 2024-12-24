A low-pass filter allows lower frequencies to pass through while attenuating higher frequencies.

A RC low-pass filter to observe how it filters out high frequencies and allows low frequencies to pass.

For an RC low-pass filter, it does not matter if the capacitor is polarized or non-polarized, as long as the following conditions are met:

1. DC vs. AC Signals:
   - If the low-pass filter is used with a DC-biased or purely DC signal (where the voltage stays positive or negative relative to ground), a polarized capacitor can be used. The positive terminal of the capacitor should be connected to the more positive voltage in the circuit.
   - For pure AC signals (where the voltage alternates between positive and negative values with no DC offset), it’s recommended to use a non-polarized capacitor. AC signals can reverse the polarity across a polarized capacitor, potentially damaging it over time.

2. Signal Voltage:
   - Ensure that the capacitor's voltage rating is higher than the peak voltage of the signal to avoid any breakdown or damage.

- A polarized capacitor is suitable for DC or AC with a DC offset (no polarity reversal).

Using a non-polarized capacitor is appropriate when working with a square wave from a function generator.

A square wave alternates between high and low levels, and if the signal switches between positive and negative voltages (without a consistent DC offset), a non-polarized capacitor is preferred. This type of capacitor can handle polarity reversals without damage, which makes it suitable for AC and alternating signals like square waves.

For a square wave input:

- Use a non-polarized capacitor if the waveform has both positive and negative cycles.
- If the square wave has a DC offset that keeps it entirely positive or entirely negative, a polarized capacitor would also work, as it won’t experience polarity reversal.

This is a classic first-order low-pass filter.

Let's calculate the key parameters:

1. Input signal:
- Frequency (f) = 100 Hz
- Peak voltage = 5V
- Angular frequency (ω) = 2πf = 2π × 100 = 628.32 rad/s

2. Circuit components:
- R = 100 kΩ = 100,000 Ω
- C = 50 µF = 50 × 10^-6 F

3. The cutoff frequency (fc) for this RC filter:
fc = 1/(2πRC)
= 1/(2π × 100,000 × 50 × 10^-6)
= 0.032 Hz

Since your input frequency (100 Hz) is much higher than the cutoff frequency (0.032 Hz), the output signal will be significantly attenuated.

The attenuation factor at 100 Hz can be calculated:
|H(jω)| = 1/√(1 + (f/fc)²)
= 1/√(1 + (100/0.032)²)
= 1/3125
≈ 0.00032

Therefore, the output voltage amplitude should be:
Vout = 5V × 0.00032 = 1.6 mV

This explains why you're seeing a millivolt-level sine wave across the capacitor. The large difference between your input frequency and the cutoff frequency causes significant attenuation.

### Capacitor as a Filter in AC Circuits

An experiment that demonstrates how a capacitor acts as a filter in an AC circuit.

To show how a capacitor can filter high frequencies in an AC circuit by reducing the output voltage at higher frequencies.

### Components

- AC Voltage Source (simulated with a DC power source in Tinkercad, switching rapidly between values)
- Capacitor (e.g., 10 µF)
- Resistor (e.g., 1 kΩ)
- Multimeter (to measure voltage drop across the resistor and capacitor)
- Oscilloscope (to visualize the capacitor output and input to the circuit)
- Wires for connections

### Setup

   - Connect the AC source (approximated in Tinkercad using a square wave generator with a frequency you can change) to one end of the resistor.
   - Connect the other end of the resistor to the positive terminal of the capacitor.
   - Connect the negative terminal of the capacitor to the ground of the AC source.

   - Connect the multimeter (set to measure AC voltage) across the capacitor to monitor how the output voltage changes with frequency.

   - Start with a low frequency (simulate around 1 Hz using the frequency adjustment for the square wave in Tinkercad).
   - Measure the voltage across the capacitor. At low frequency, the capacitor will block less of the AC signal, so you should see a voltage close to the input.

   - Gradually increase the square wave frequency in Tinkercad (e.g., 10 Hz, 100 Hz).
   - At higher frequencies, observe that the voltage across the capacitor decreases as the capacitor acts as a filter, blocking higher frequencies.

### Results

- At low frequencies, the capacitor passes most of the AC signal, so the voltage across it is close to the input.
- As the frequency increases, the capacitor blocks more of the AC signal, and the voltage across the capacitor decreases, illustrating the filtering effect.

This experiment demonstrates a low-pass filter effect, where the capacitor allows low-frequency signals to pass through more easily than high-frequency signals. This behavior is fundamental in electronics for filtering out noise or unwanted high-frequency components in AC signals.

### Components:

1. AC Voltage Source: Set to generate various frequencies (e.g., a sine wave).
2. Resistor: 1 kΩ.
3. Capacitor: 0.1 µF.
4. Oscilloscope: To observe the input and output waveforms.

### Setup:

   - Connect one terminal of the AC source to the resistor.
   - Connect the other end of the resistor to one terminal of the capacitor.
   - Connect the other terminal of the capacitor to ground.

   - The output is taken across the capacitor. Connect the oscilloscope probe here to observe the output signal.
   - Also, place another oscilloscope probe across the AC source to observe the input signal for comparison.

   - Connect the first oscilloscope probe to the input (AC source) and the second probe to the output (across the capacitor).
   - This setup allows you to observe how the input and output signals compare at different frequencies.

### Steps:

   - Set the AC source to a high frequency, such as 10 kHz, to observe how the circuit behaves at higher frequencies.

   - With a high-frequency input, check the oscilloscope to see the output across the capacitor.
   - Expected Outcome: At high frequencies, the output signal will be much weaker or nearly zero. This is because the capacitor’s impedance is low at high frequencies, causing most of the signal to bypass the output and go to ground.

   - Gradually decrease the frequency of the AC source to around 1 kHz and then lower (e.g., 10 Hz).
   - Expected Outcome: As the frequency decreases, the output signal amplitude should increase. This is because the capacitor’s impedance increases at lower frequencies, allowing more of the input signal to pass through to the output.

4. Calculate the Cutoff Frequency:
   - The cutoff frequency \( f_c \) of an RC low-pass filter is given by:
     \[
     f_c = \frac{1}{2\pi RC}
     \]
   - For a 1 kΩ resistor and a 0.1 µF capacitor, the cutoff frequency is approximately 1.59 kHz. Below this frequency, signals pass through with minimal attenuation; above this frequency, signals are increasingly attenuated.

5. Test at the Cutoff Frequency:
   - Set the AC source frequency near the cutoff frequency (around 1.6 kHz).
   - Expected Outcome: At the cutoff frequency, the output signal amplitude should be approximately 70% of the input signal amplitude, indicating the point where the filter begins to attenuate higher frequencies.

Low-Pass Filter Behavior:

This RC circuit acts as a low-pass filter because the capacitor allows low frequencies to pass while presenting low impedance to high frequencies, which causes them to be filtered out.

Cutoff Frequency:

The cutoff frequency is the point where the filter transitions from passing low frequencies to attenuating high frequencies. Frequencies below this point pass with minimal attenuation, while frequencies above are increasingly blocked.

This experiment demonstrates how an RC low-pass filter selectively allows lower frequencies while attenuating higher ones, which is useful in applications like audio signal processing, smoothing DC signals, and removing high-frequency noise.

Solving How an Inductor Works in a Filter Circuit:

Let’s assume we want to design a low-pass filter using an inductor and resistor to remove high-frequency noise from a signal.

1. Choose an inductor and resistor: For example, select a 100μH inductor and a 1kΩ resistor.

2. Calculate the cutoff frequency: Use the formula for the cutoff frequency of an RL low-pass filter:

   $$ f_c = \frac{R}{2\pi L} $$

   $$ f_c = \frac{1,000}{2\pi \times 100 \times 10^{-6}} \approx 1.59 \, \text{kHz} $$

   The cutoff frequency is about 1.59kHz, meaning frequencies below this pass through, while higher frequencies get filtered out.

3. Connect the inductor and resistor in series: Wire the inductor and resistor in series with the signal input.

4. Test the circuit: Feed a signal with high-frequency noise into the circuit. The inductor will block high frequencies, and only the clean, low-frequency part of the signal will pass through to the output.

This demonstrates how an inductor can be used to filter out unwanted high-frequency noise in a circuit.

To design a low-pass filter experiment using Tinkercad, follow these steps:

Create a simple RC (Resistor-Capacitor) low-pass filter to observe how it allows low-frequency signals to pass while attenuating higher frequencies.

### Components

1. Resistor (R) - 10 kΩ (or any suitable resistance)
2. Capacitor (C) - 0.1 µF
3. Signal Generator - To provide variable frequency signals (use the Function Generator in Tinkercad's circuit workspace)
4. Oscilloscope - To observe the input and output signals (use the oscilloscope in Tinkercad)
5. Breadboard - For connecting components

### Setup

1. Connect the Resistor and Capacitor in Series:
   - Place the resistor on the breadboard and connect it to the signal generator's output.
   - Connect the capacitor’s positive leg to the other end of the resistor.
   - Connect the capacitor's negative leg to the ground of the signal generator.
2. Connect Oscilloscope Probes:
   - Place the oscilloscope probe at the input (signal generator output before the resistor) to monitor the input signal.
   - Place another oscilloscope probe at the output (junction between resistor and capacitor) to monitor the output signal.

### Procedure

1. Set Signal Generator: Start with a low-frequency signal (e.g., 100 Hz) with a small amplitude (e.g., 5V peak).
2. Observe Input and Output Signals: Check both signals on the oscilloscope.
3. Increase Frequency: Gradually increase the frequency (e.g., 500 Hz, 1 kHz, 10 kHz, and so on).
4. Record Observations: Note how the amplitude of the output signal changes compared to the input as you increase frequency.

### Results

- At low frequencies, the output signal's amplitude should be close to the input amplitude.
- As the frequency increases, the output amplitude should decrease, showing the low-pass filter effect.

This experiment demonstrates that an RC low-pass filter allows low-frequency signals to pass while attenuating high frequencies, verifying the behavior of a simple low-pass filter.
