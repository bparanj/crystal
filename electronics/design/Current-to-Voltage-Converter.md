### Current-to-Voltage Converter

A Current-to-Voltage Converter (I-to-V Converter) is a circuit that converts an input current into a proportional output voltage. This conversion is commonly implemented using an operational amplifier (op-amp) in a feedback configuration. Such circuits are essential in systems where current-based signals (e.g., photodiodes, sensors) need to be converted to voltage for processing or measurement.

### Concepts

1. Conversion Principle:
   - Ohm's law relates current and voltage: \( V = I \cdot R \).
   - An I-to-V Converter uses a feedback resistor (\( R_f \)) in an op-amp circuit to perform this conversion.

2. Input-Output Relationship:
   - The output voltage is proportional to the input current:
     \[
     V_{out} = -I_{in} \cdot R_f
     \]
     The negative sign indicates an inversion due to the inverting configuration of the op-amp.

3. Applications:
   - Interfacing current-output sensors like photodiodes or 4–20 mA industrial current loops.
   - Analog signal processing.

### Experiment

#### Objective

To design and simulate a Current-to-Voltage Converter using an op-amp and observe the relationship between input current and output voltage.

#### Components

1. Operational Amplifier (e.g., LM741).
2. Resistor (\( R_f = 10k\Omega \), feedback resistor).
3. Current Source (simulate with a variable resistor or a photodiode).
4. Multimeter (to measure output voltage).
5. Breadboard and wires.

### Circuit

1. Input Current:
   - Connect the current source to the inverting input of the op-amp.

2. Feedback Resistor:
   - Connect \( R_f \) between the output and the inverting input of the op-amp.

3. Reference Ground:
   - Connect the non-inverting input of the op-amp to ground.

4. Output Voltage:
   - Take the output voltage from the op-amp's output terminal.

5. Measurement:
   - Use a multimeter to measure \( V_{out} \).

### Steps

1. Set Up the Circuit:
   - Build the circuit as per the configuration above, ensuring proper polarity for the current source.

2. Apply Input Current:
   - Set the input current to a known value using a variable resistor or a current source.

3. Measure Output Voltage:
   - Measure \( V_{out} \) using a multimeter.

4. Vary Input Current:
   - Change the input current (e.g., \( 10\mu A, 20\mu A, 50\mu A \)) and observe the corresponding \( V_{out} \).

5. Experiment with Feedback Resistor:
   - Replace \( R_f \) with different resistances (\( 5k\Omega, 20k\Omega \)) and observe changes in \( V_{out} \).

### Results

1. Linear Relationship:
   - The output voltage varies linearly with the input current:
     \[
     V_{out} = -I_{in} \cdot R_f
     \]

2. Effect of Feedback Resistor:
   - Increasing \( R_f \) increases the output voltage for the same input current.

3. Zero Offset:
   - When \( I_{in} = 0 \), \( V_{out} = 0 \), assuming no op-amp offset voltage.

### Insights

1. Versatility:
   - This circuit is ideal for converting small currents from sensors (e.g., photodiodes, current loops) into measurable voltages.

2. Feedback Resistor:
   - Choose \( R_f \) to match the range of input currents and desired output voltage levels.

3. Applications:
   - Photodiode amplifiers, current loop receivers, and transimpedance amplifiers in analog circuits.

This experiment can be implemented by using a current source or variable resistor as the input and an op-amp to convert the current to voltage. The results demonstrate how the I-to-V Converter linearly maps current signals to voltage for further processing.
