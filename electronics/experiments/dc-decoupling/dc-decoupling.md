PENDING

Document the steps in voltage-decoupling.md

This is a slight variation of the diode experiment. The focus here is observing the voltage drop.

Voltage decoupling using a **series diode** involves placing a diode in series with the supply line to isolate sections of a circuit. The diode prevents reverse current flow, ensuring that voltage fluctuations or faults in one part of the circuit do not affect other sections. This method is useful for protecting sensitive components and maintaining stable operation.

### Voltage Decoupling Using a Series Diode

A series diode can decouple voltage in a circuit by blocking the flow of current in one direction, allowing current to flow only when the diode is forward-biased. This behavior is used to isolate parts of a circuit, prevent reverse current flow, and regulate current flow based on the applied voltage.

1. Forward Bias:
   - When the diode's anode is at a higher voltage than the cathode, the diode conducts, allowing voltage and current to pass.

2. Reverse Bias:
   - When the cathode is at a higher voltage than the anode, the diode blocks current flow, effectively decoupling the downstream circuit from the voltage source.

3. Voltage Drop:
   - A silicon diode introduces a voltage drop of approximately 0.7V (for a silicon diode) when forward-biased.

### Experiment

#### Components:

1. DC voltage source (\( V_1 = 10V \)).
2. Resistor (Load) (\( R = 1k\Omega \)).
3. Diode (e.g., 1N4148).
4. Multimeter (to measure voltage across the load).

### Setup:

   - Connect the anode of the diode to the positive terminal of the DC voltage source.
   - Connect the cathode of the diode to one end of the resistor (\( R \)).
   - Connect the other end of the resistor to the ground of the voltage source.

   - Place the multimeter across the resistor to measure the voltage after the diode.

### Steps:

1. Forward-Bias Operation:
   - Set the DC voltage source to \( 10V \).
   - Measure the voltage across the resistor. It should be approximately:
     \[
     V_{out} = V_1 - V_{diode} \approx 10V - 0.7V = 9.3V
     \]

2. Reverse-Bias Operation:
   - Reverse the polarity of the voltage source (connect the diode's anode to ground and cathode to \( +10V \)).
   - Measure the voltage across the resistor. It should be \( 0V \), as the diode blocks current flow.

### Observations:

1. Forward-Bias Case:
   - The diode conducts, and the load receives a decoupled voltage reduced by the diode's forward voltage drop (\( \approx 0.7V \)).

2. Reverse-Bias Case:
   - The diode blocks current flow, and the load receives no voltage (\( 0V \)).

### Applications:

1. Voltage Isolation:
   - Diodes are used to isolate sections of a circuit, preventing backflow of current.

2. Polarity Protection:
   - Protects circuits from reverse voltage by blocking current flow in reverse-bias conditions.

3. Voltage Decoupling:
   - Used in applications where voltage needs to be selectively passed or blocked based on polarity.

4. Ripple Filtering:
   - In power supplies, diodes in series decouple voltage fluctuations and rectify signals.

You can test both forward and reverse-bias conditions by reversing the voltage source. It demonstrates the diode's role in voltage decoupling.
