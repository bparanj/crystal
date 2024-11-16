### Voltage-by-Ratio Multiplier

A Voltage-by-Ratio Multiplier is a circuit that generates an output voltage proportional to the input voltage scaled by a ratio of resistances, typically \( R_1 / R_2 \). This type of circuit is widely used in signal conditioning, analog computation, and voltage scaling.

---

### Key Concepts:

1. Scaling Principle:
   - The circuit produces an output voltage \( V_{out} \) based on the input voltage \( V_{in} \) and the resistance ratio:
     \[
     V_{out} = V_{in} \cdot \frac{R_1}{R_2}
     \]

2. Applications:
   - Signal attenuation or amplification.
   - Adjusting sensor outputs to fit a specific voltage range.
   - Analog computation and control systems.

---

### Common Implementations:

#### 1. Voltage Divider (Passive Circuit):
- A simple voltage divider can implement a fixed scaling:
  \[
  V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}
  \]
- This approach is limited to attenuating signals (\( V_{out} \leq V_{in} \)).

#### 2. Operational Amplifier Circuit (Active Circuit):
- An op-amp in a non-inverting configuration allows both scaling up (amplification) and down (attenuation):
  \[
  V_{out} = V_{in} \cdot \left(1 + \frac{R_1}{R_2}\right)
  \]

---

### Experiment Design for Tinkercad (Op-Amp Method):

#### Objective:
To design and simulate a Voltage-by-Ratio Multiplier using an operational amplifier.

#### Components:
1. Operational Amplifier (e.g., LM741).
2. Resistors (\( R_1 = 10k\Omega, R_2 = 5k\Omega \)).
3. DC Voltage Source (\( V_{in} = 5V \)).
4. Multimeter (to measure \( V_{out} \)).
5. Breadboard and wires.

---

### Circuit Configuration:

#### Non-Inverting Op-Amp Configuration:
1. Input Voltage:
   - Connect \( V_{in} \) to the non-inverting input (\( + \)) of the op-amp.

2. Feedback Network:
   - Connect \( R_1 \) between the op-amp output and inverting input (\( - \)).
   - Connect \( R_2 \) between the inverting input (\( - \)) and ground.

3. Output Voltage:
   - Measure \( V_{out} \) at the op-amp output terminal.

4. Power Supply:
   - Provide \( \pm 12V \) as the op-amp power supply.

---

### Steps to Perform:

1. Set Up the Circuit:
   - Assemble the circuit as described.

2. Apply Input Voltage:
   - Set \( V_{in} = 5V \).

3. Measure Output Voltage:
   - Use a multimeter to measure \( V_{out} \).

4. Experiment with Resistor Values:
   - Replace \( R_1 \) and \( R_2 \) with different values to observe how \( V_{out} \) changes with the ratio \( R_1 / R_2 \).

---

### Expected Results:

#### Example:
1. With \( V_{in} = 5V, R_1 = 10k\Omega, R_2 = 5k\Omega \):
   \[
   V_{out} = 5V \cdot \left(1 + \frac{10k\Omega}{5k\Omega}\right) = 5V \cdot (1 + 2) = 15V
   \]

2. For a unity gain configuration (\( R_1 = R_2 \)):
   \[
   V_{out} = 5V \cdot \left(1 + \frac{5k\Omega}{5k\Omega}\right) = 5V \cdot 2 = 10V
   \]

---

### Key Insights:

1. Scaling Range:
   - The circuit can scale \( V_{in} \) up or down depending on \( R_1 \) and \( R_2 \).

2. Flexibility:
   - The op-amp configuration provides precise and adjustable scaling compared to a passive divider.

3. Applications:
   - Voltage scaling in instrumentation, sensor interfaces, and signal processing.

---

This experiment can be implemented in Tinkercad, where you can adjust resistor values and input voltages to observe the scaling effect. The op-amp configuration offers a practical and versatile way to implement a Voltage-by-Ratio Multiplier.
