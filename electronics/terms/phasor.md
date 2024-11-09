A phasor is a complex number used to represent sinusoidal functions, typically in the context of alternating current (AC) circuits and other oscillatory systems. It simplifies calculations by converting sinusoidal waveforms, which vary with time, into a fixed representation that captures both their magnitude and phase. 

1. Magnitude: The amplitude or peak value of the sinusoidal waveform.
2. Phase: The position of the waveform relative to a reference point in time, expressed in degrees or radians.
3. Frequency: The rate at which the sinusoid oscillates, usually assumed constant when using phasors.

### How Phasors Work

- A sinusoidal function like \( V(t) = V_0 \cos(\omega t + \theta) \) can be converted into a phasor representation as a complex number \( V = V_0 e^{j\theta} \), where \( j \) is the imaginary unit. This form allows for easy manipulation of the sinusoidal waveform's amplitude and phase without explicitly handling time.
- Phasors represent sinusoidal signals as vectors rotating in the complex plane. For example, a voltage or current sinusoid is represented by a vector with an angle corresponding to its phase shift and a length equal to its amplitude.

### Why Phasors are Useful

Phasors allow AC circuit analysis using algebra rather than differential equations, which is much simpler. For example, in AC circuits:
   - Impedance of resistors, inductors, and capacitors can be represented as complex numbers.
   - Ohm’s law, Kirchhoff’s laws, and other circuit laws apply to phasors similarly to DC circuit analysis.

### Example

For an AC voltage \( V(t) = 10 \cos(100t + 30^\circ) \), the phasor form would be:

\[
V = 10 \angle 30^\circ
\]

This notation expresses a voltage with an amplitude of 10 units and a phase angle of 30 degrees. 

In summary, a phasor is a mathematical tool that represents a sinusoidal waveform in terms of its magnitude and phase, making AC circuit analysis much simpler and more intuitive.
