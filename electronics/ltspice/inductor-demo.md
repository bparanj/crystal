Below is the `.asc` file content to demonstrate a **Basic Inductor Demo** in LTSpice. This circuit applies an AC voltage source to an inductor and resistor to observe how the inductor behaves in response to changing current.

---

### Circuit Description
1. **Inductor (L)**: Demonstrates inductive reactance.
2. **Resistor (R)**: Provides a load to observe voltage and current.
3. **AC Voltage Source**: Supplies a sine wave input.
4. **Voltage Probes**: Measure voltage across the inductor and the resistor.

---

### LTSpice `.asc` File Content

Save the following content as `Basic_Inductor_Demo.asc`.

```plaintext
Version 4
SHEET 1 880 680
WIRE 160 48 160 128
WIRE 320 48 160 48
WIRE 320 128 320 48
WIRE 320 128 160 128
WIRE 480 128 320 128
WIRE 480 48 480 128
WIRE 480 48 640 48
WIRE 640 48 640 128
WIRE 640 128 480 128
WIRE 320 208 320 128
FLAG 320 208 0
SYMBOL voltage 160 32 R0
SYMATTR InstName V1
SYMATTR Value SINE(0 10 1k)
SYMBOL ind 320 128 R0
SYMATTR InstName L1
SYMATTR Value 10m
SYMBOL res 480 128 R0
SYMATTR InstName R1
SYMATTR Value 1k
TEXT 96 16 Left 2 !.tran 10ms
TEXT 96 32 Left 2 !.ac dec 100 10 1k
```

---

### Explanation of Components

1. **Voltage Source (V1)**:
   - Sine wave `SINE(0 10 1k)`:
     - Amplitude: 10 V (peak).
     - Frequency: 1 kHz.

2. **Inductor (L1)**:
   - Value: 10 mH.
   - Creates inductive reactance, opposing rapid changes in current.

3. **Resistor (R1)**:
   - Value: 1 kΩ.
   - Serves as a load in series with the inductor.

4. **Simulation Commands**:
   - `.tran 10ms`: Transient analysis for 10 ms to observe current and voltage waveforms over time.
   - `.ac dec 100 10 1k`: AC analysis with a frequency sweep from 10 Hz to 1 kHz to observe frequency-dependent behavior.

---

### Steps to Run in LTSpice

1. Save the `.asc` file and open it in LTSpice.
2. Run the **Transient Analysis** to observe the voltage and current waveforms over time.
3. Run the **AC Analysis** to observe how the inductor's impedance changes with frequency.

This setup demonstrates the basic behavior of an inductor in a circuit, including its frequency response and time-domain characteristics.
