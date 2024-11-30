To determine the power used by a simple AC circuit, you need to consider the different types of power involved: real power, reactive power, and apparent power. 

### 1. **Real Power (P)**
- **Definition**: Real power, also known as active power, is the actual power consumed by the resistive elements in the circuit. It is measured in watts (W).
- **Formula**: 
  $$
  P = V_{\text{rms}} \cdot I_{\text{rms}} \cdot \cos(\phi)
  $$
  where \( V_{\text{rms}} \) is the root mean square (RMS) voltage, \( I_{\text{rms}} \) is the RMS current, and \( \phi \) is the phase angle between the voltage and current.

### 2. **Reactive Power (Q)**
- **Definition**: Reactive power is the power stored and released by the reactive elements (inductors and capacitors) in the circuit. It is measured in volt-amperes reactive (VAR).
- **Formula**: 
  $$
  Q = V_{\text{rms}} \cdot I_{\text{rms}} \cdot \sin(\phi)
  $$

### 3. **Apparent Power (S)**
- **Definition**: Apparent power is the combination of real power and reactive power. It represents the total power supplied to the circuit. It is measured in volt-amperes (VA).
- **Formula**: 
  $$
  S = V_{\text{rms}} \cdot I_{\text{rms}}
  $$

### 4. **Power Factor (PF)**
- **Definition**: The power factor is the ratio of real power to apparent power and indicates the efficiency of the circuit.
- **Formula**: 
  $$
  \text{PF} = \cos(\phi) = \frac{P}{S}
  $$

### Steps to Determine Power in an AC Circuit:
1. **Measure RMS Values**: Measure the RMS voltage (\( V_{\text{rms}} \)) and RMS current (\( I_{\text{rms}} \)) in the circuit.
2. **Determine Phase Angle**: Find the phase angle (\( \phi \)) between the voltage and current, which can be measured using an oscilloscope or calculated if the circuit components are known.
3. **Calculate Real Power**: Use the formula \( P = V_{\text{rms}} \cdot I_{\text{rms}} \cdot \cos(\phi) \) to find the real power.
4. **Calculate Reactive Power**: Use the formula \( Q = V_{\text{rms}} \cdot I_{\text{rms}} \cdot \sin(\phi) \) to find the reactive power.
5. **Calculate Apparent Power**: Use the formula \( S = V_{\text{rms}} \cdot I_{\text{rms}} \) to find the apparent power.
6. **Determine Power Factor**: Calculate the power factor using \( \text{PF} = \cos(\phi) \).

These calculations help you understand how much power is being used effectively in the circuit and how much is being stored and released by reactive components.
