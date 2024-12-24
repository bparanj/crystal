Resistance

Opposition to current flow by a resistor is called **resistance**, denoted as \( R \). It is independent of frequency and is governed by Ohm’s Law:

\[
R = \frac{V}{I}
\]

Where:
- \( R \): Resistance (in ohms)
- \( V \): Voltage (in volts)
- \( I \): Current (in amperes)

Capacitive Reactance

Opposition to current flow by a capacitor is called **reactance**, specifically **capacitive reactance**, denoted as \( X_C \). It is frequency-dependent and calculated using the formula:

\[
X_C = \frac{1}{2\pi f C}
\]

Where:
- \( X_C \): Capacitive reactance (in ohms)
- \( f \): Frequency of the AC signal (in hertz)
- \( C \): Capacitance (in farads)

Inductive Reactance

Opposition to current flow by an inductor is called **inductive reactance**, denoted as \( X_L \). It is frequency-dependent and calculated using the formula:

\[
X_L = 2\pi f L
\]

Where:
- \( X_L \): Inductive reactance (in ohms)
- \( f \): Frequency of the AC signal (in hertz)
- \( L \): Inductance (in henries)

The distinction arises because **resistance** and **capacitance** describe different phenomena:

1. **Resistor**:
   - Resistance is a constant property of a resistor that opposes current flow by converting electrical energy into heat.
   - This opposition is independent of the signal's frequency.

2. **Capacitor**:
   - Capacitance is a measure of a capacitor's ability to store charge, not directly its opposition to current flow.
   - The opposition to current flow by a capacitor is called **reactance** (specifically, **capacitive reactance**) because it varies with the frequency of the signal:
     \[
     X_C = \frac{1}{2\pi f C}
     \]
   - Higher frequency signals encounter less opposition, making the opposition dynamic and dependent on both the capacitance and the signal's frequency.

- **Resistance** is fixed for resistors, so the term resistance captures its opposing behavior.
- **Capacitance** is not directly about opposition; instead, the frequency-dependent **reactance** describes the capacitor's dynamic opposition to current flow.

The distinction arises because **resistance** and **inductance** describe different properties and behaviors:

1. **Resistor**:

   - Resistance is a constant property of a resistor that opposes current flow, converting electrical energy into heat.
   - This opposition is frequency-independent.

2. **Inductor**:

   - Inductance is a measure of an inductor's ability to store energy in a magnetic field, not its direct opposition to current flow.
   - The opposition to current flow by an inductor is called **inductive reactance** because it varies with the frequency of the signal:
     \[
     X_L = 2\pi f L
     \]
   - Higher frequency signals encounter more opposition, making the opposition dynamic and dependent on both the inductance and the signal's frequency.

**Resistance** is a fixed property, so "resistance" directly represents a resistor's behavior.
**Inductance** measures the ability to create a magnetic field, while the opposition it causes is frequency-dependent and described by **reactance**. Hence, the term **inductive reactance** is used for this specific behavior.

Inductors act as a **short circuit** for DC.

1. **Capacitor and DC**:
   - Capacitors block DC because, after the initial charging phase, the voltage across the capacitor becomes constant, and no current flows through the circuit (\( I = C \cdot \frac{dV}{dt} \), and \( \frac{dV}{dt} = 0 \) for DC).

2. **Inductor and DC**:
   - Inductors allow DC to flow freely because their opposition to current (\( V = L \cdot \frac{dI}{dt} \)) depends on changes in current (\( \frac{dI}{dt} \)).
   - For steady DC, \( \frac{dI}{dt} = 0 \), so the inductor behaves like a simple conducting wire (short circuit) after the initial transient.

- **Capacitor**: Open circuit for DC.
- **Inductor**: Short circuit for DC.

For DC:

| **Component**       | **Circuit State          **   | **Explanation**                                   |
|----------------------|------------------------------|--------------------------------------------------|
| **Resistor**         | Partial circuit             | Allows current flow, proportional to resistance. |
| **Capacitor**        | Open circuit                | Blocks DC after initial charging.               |
| **Inductor**         | Short circuit               | Allows DC flow with negligible opposition.       |
| **Diode**            | Open/Short circuit          | Conducts (short) in forward bias; blocks (open) in reverse bias. |
| **Zener Diode**      | Open/Short circuit          | Blocks reverse current until breakdown voltage is reached. |
| **Switch (Open)**    | Open circuit                | No current flow when the switch is open.         |
| **Switch (Closed)**  | Short circuit               | Allows current flow when the switch is closed.   |
| **Thermistor**       | Partial circuit             | Resistance changes based on temperature.         |
| **Varistor**         | Open/Short circuit          | Blocks voltage until threshold is exceeded (short for surges). |

This table summarizes how different components behave in terms of circuit states (open, short, or partial) for DC conditions.

For AC:

| **Component**       | **Circuit State           **        | **Explanation**                                                                 |
|----------------------|------------------------------------|---------------------------------------------------------------------------------|
| **Resistor**         | Partial circuit                  | Allows current flow, with resistance independent of frequency.                  |
| **Capacitor**        | Partial/Open circuit             | Reactance decreases as frequency increases; blocks very low-frequency signals.  |
| **Inductor**         | Partial/Short circuit            | Reactance increases as frequency increases; acts as a short at very low frequencies. |
| **Diode**            | Open/Short circuit               | Conducts (short) for positive half-cycles; blocks (open) for negative half-cycles. |
| **Zener Diode**      | Open/Short circuit               | Blocks reverse voltage unless breakdown voltage is exceeded; clips in forward bias. |
| **Switch (Open)**    | Open circuit                     | Completely blocks AC current flow.                                              |
| **Switch (Closed)**  | Short circuit                    | Allows AC current to flow without restriction.                                   |
| **Thermistor**       | Partial circuit                  | Resistance changes with temperature; no direct frequency dependency.            |
| **Varistor**         | Open/Short circuit               | Blocks voltage below threshold; conducts (short) for high-voltage AC surges.    |

This table describes how different components behave in terms of circuit states (open, short, or partial) under AC conditions, which often depend on frequency and component characteristics.
