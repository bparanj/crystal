### Context and Problem

The RC low-pass filter is a fundamental circuit in electronics used to attenuate high-frequency signals while allowing low-frequency signals to pass through. This behavior relies on the frequency-dependent reactance of the capacitor. By varying the input frequency, we can observe how the circuit selectively filters components of the input signal, demonstrating the essential principles of low-pass filtering.

### Terminology

**RC Low-Pass Filter:**

A circuit consisting of a resistor (R) and capacitor (C) that allows low-frequency signals to pass while attenuating high-frequency signals.

**Capacitive Reactance (\(X_c\)):**

The opposition to current flow by a capacitor, inversely proportional to the signal frequency (\(X_c = \frac{1}{2 \pi f C}\)).

**Cutoff Frequency:**

The frequency at which the filter begins significantly attenuating the signal, determined by the resistor and capacitor values (\(f_c = \frac{1}{2 \pi R C}\)).

### Observations

#### **Low Frequencies (1 Hz):**

- The capacitor charges and discharges slowly, allowing most of the signal to pass through.
- The output resembles the input square wave, with slightly rounded edges due to smoothing.

#### **Intermediate Frequencies (100 Hz – 1.42 kHz):**

- The capacitor begins to resist the signal, attenuating the output.
- At 100 Hz, the square wave transitions into a sawtooth shape due to the capacitor’s charging and discharging patterns.
- At 1.42 kHz, the output voltage drops to millivolt levels, effectively blocking most of the high-frequency signal.

#### **High Frequencies (7.33 kHz – 1 MHz):**

- The capacitor charges and discharges so rapidly that it appears as an open circuit.
- The output voltage is negligible, measured in microvolts at 1 MHz.

#### Behavior of the RC Circuit

1. **Low Frequencies:**
   - At low frequencies, the capacitive reactance (\(X_c\)) is high, allowing the capacitor to charge and discharge more slowly.
   - This enables low-frequency signals to pass through with minimal attenuation.

2. **High Frequencies:**
   - At high frequencies, \(X_c\) decreases, and the capacitor effectively acts as a short circuit, bypassing high-frequency components to ground.
   - The output voltage across the capacitor becomes negligible.

3. **Transition Region:**
   - Near the cutoff frequency, the capacitor begins attenuating the signal.
   - The square wave transitions into smoother waveforms, such as sawtooth shapes, due to the capacitor’s gradual response to rapid transitions.

The RC low-pass filter demonstrates the capacitor’s role in selectively attenuating high-frequency signals:

1. **Low-Frequency Behavior:**

The circuit allows low-frequency signals to pass through with minimal attenuation.

2. **High-Frequency Behavior:**

The capacitor blocks high-frequency signals, effectively reducing their amplitude to near-zero levels.

3. **Signal Smoothing:**

The filter transitions square waves into smoother forms at intermediate frequencies, illustrating its ability to reshape signals.

#### Applications

- Signal Conditioning: Filtering out noise from signals.
- Power Supplies: Smoothing voltage ripples after rectification.
- Audio Systems: Separating low-frequency bass signals from higher frequencies.

PENDING

Compare this experiment with
experiments/queue/low-pass-filter.md,
book/circuits.md,
book/resistor/sequence.md,
design/discrete-passive-circuit.md
