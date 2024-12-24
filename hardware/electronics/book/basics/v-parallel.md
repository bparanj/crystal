### Effect of Connecting Voltage Sources in Parallel

When voltage sources are connected in parallel, their output voltage remains the same as that of a single source (if they are identical). However, the total current capability increases because the sources share the load current.

### Reasoning

1. **Same Voltage Requirement**:
   - In a parallel connection, the voltage across all parallel components must be the same because they share the same two nodes.
   - Therefore, only voltage sources with equal output voltages can be connected in parallel without causing issues like circulating currents.

2. **Increased Current Capacity**:
   - Each voltage source contributes to the total current based on its current rating.
   - The total current available to the load is the sum of the currents that each source can provide:
     \[
     I_T = I_1 + I_2 + \dots + I_n
     \]

3. **Load Sharing**:
   - If the sources are identical (same voltage and internal resistance), they share the load current equally.
   - If the sources have different internal resistances, the current contribution depends on those resistances.

4. **Avoiding Mismatch**:
   - Connecting sources with slightly different voltages can cause circulating currents, which can lead to overheating or damage.

### Formula

1. **Total Current**:
   For \(n\) identical voltage sources in parallel, each providing \(I_{\text{max}}\):
   \[
   I_T = n \cdot I_{\text{max}}
   \]

2. **Voltage Across the Load**:
   The voltage across the parallel combination remains the same as the voltage of a single source:
   \[
   V_T = V_{\text{source}}
   \]

### Example

- Two \(12 \, \text{V}\) batteries, each capable of providing \(10 \, \text{A}\), are connected in parallel.
- The total voltage across the load remains \(12 \, \text{V}\).
- The total current capacity increases:
  \[
  I_T = 10 + 10 = 20 \, \text{A}.
  \]

This configuration increases current capacity while maintaining the same voltage, making it suitable for high-current applications like powering motors or inverters.
