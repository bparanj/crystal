### 3-State Zero LED Indicator Using Diode Switching

A 3-State Zero LED Indicator uses a combination of diodes and LEDs to visually indicate whether an input voltage is positive, negative, or zero. This is commonly used in signal monitoring or debugging circuits to display polarity states.

1. Voltage Polarity Detection:
   - The circuit identifies three states:
     1. Positive Voltage: Lights up one LED.
     2. Negative Voltage: Lights up another LED.
     3. Zero Voltage: Both LEDs are off.

2. Diode Switching:
   - Diodes allow current to flow in specific directions, enabling the circuit to switch between the LEDs based on the input voltage.

3. Applications:
   - Polarity indicators.
   - Signal monitoring and debugging.

### Experiment

To design and simulate a 3-State Zero LED Indicator that uses diodes and LEDs to display the polarity of an input voltage.

#### Components:

1. 2 LEDs (e.g., Red and Green).
2. 2 Diodes (1N4007 or similar).
3. Resistors (\( R_{LED1} = R_{LED2} = 330\Omega \)).
4. Power Supply (\( V_{in} = -10V \text{ to } +10V \)).
5. Breadboard and wires.

### Circuit:

1. Positive Voltage Indicator:
   - Connect the anode of the first LED (\( LED1 \)) to the cathode of a diode (\( D1 \)).
   - Connect the anode of \( D1 \) to the positive terminal of the input voltage (\( V_{in} \)).
   - Place a resistor (\( R_{LED1} \)) in series with \( LED1 \), and connect its cathode to ground.

2. Negative Voltage Indicator:
   - Connect the cathode of the second LED (\( LED2 \)) to the anode of a diode (\( D2 \)).
   - Connect the cathode of \( D2 \) to the positive terminal of \( V_{in} \).
   - Place a resistor (\( R_{LED2} \)) in series with \( LED2 \), and connect its anode to ground.

3. Input Voltage (\( V_{in} \)):
   - Connect the positive terminal of \( V_{in} \) to the shared nodes of \( D1 \) and \( D2 \).

### Steps

1. Set Up the Circuit:
   - Build the circuit on a breadboard in Tinkercad as described above.

2. Apply Positive Voltage:
   - Set \( V_{in} \) to \( +5V \) using the power supply.
   - Observe:
     - \( LED1 \) lights up (indicating positive voltage).
     - \( LED2 \) remains off.

3. Apply Negative Voltage:
   - Set \( V_{in} \) to \( -5V \).
   - Observe:
     - \( LED2 \) lights up (indicating negative voltage).
     - \( LED1 \) remains off.

4. Apply Zero Voltage:
   - Set \( V_{in} \) to \( 0V \).
   - Observe:
     - Both \( LED1 \) and \( LED2 \) are off (indicating zero voltage).

5. Test Boundary Conditions:
   - Gradually vary \( V_{in} \) around \( 0V \) to observe the switching behavior of the LEDs.

### Results:

1. Positive Voltage (\( V_{in} > 0 \)):
   - \( D1 \) conducts, lighting up \( LED1 \) (positive indicator).
   - \( D2 \) blocks current, keeping \( LED2 \) off.

2. Negative Voltage (\( V_{in} < 0 \)):
   - \( D2 \) conducts, lighting up \( LED2 \) (negative indicator).
   - \( D1 \) blocks current, keeping \( LED1 \) off.

3. Zero Voltage (\( V_{in} = 0 \)):
   - Both \( D1 \) and \( D2 \) block current, leaving both LEDs off.

### Insights:

1. Diode Switching:
   - The diodes control the current flow to the appropriate LED based on the polarity of the input voltage.

2. Clear Visual Feedback:
   - The circuit provides an intuitive indication of the input voltage's polarity or zero state.

3. Applications:
   - Useful for monitoring signal polarity in electronics testing and debugging.

In Tinkercad, you can simulate this circuit by varying the input voltage (\( V_{in} \)) using a DC power supply. Observe the LEDs lighting up based on the input polarity and validate the circuit's behavior.
