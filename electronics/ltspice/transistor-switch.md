Below is the content for an LTSpice `.asc` file to demonstrate how a transistor can act as a switch to control an LED. This circuit uses an NPN transistor to turn the LED on and off based on the input control voltage.

---

### Circuit Description
1. **Transistor (NPN)**: Acts as the switch.
2. **Resistor (Base)**: Limits the base current.
3. **Resistor (LED)**: Limits the current through the LED.
4. **LED**: Indicates the transistor's switching action.
5. **Voltage Source**: Provides the control signal for the transistor base.

---

### LTSpice `.asc` File Content

Save the following content as `Transistor_Switch_LED.asc`.

```plaintext
Version 4
SHEET 1 880 680
WIRE 160 128 160 48
WIRE 320 128 160 128
WIRE 320 192 320 128
WIRE 480 192 320 192
WIRE 480 128 480 192
WIRE 480 48 480 128
WIRE 480 48 160 48
WIRE 320 288 320 192
WIRE 480 288 480 208
WIRE 480 288 320 288
WIRE 480 288 640 288
WIRE 640 288 640 48
WIRE 640 48 480 48
WIRE 640 48 160 48
FLAG 320 288 0
FLAG 160 128 VIN
SYMBOL npn 320 208 M180
SYMATTR InstName Q1
SYMATTR Value 2N2222
SYMBOL res 160 48 R0
SYMATTR InstName R1
SYMATTR Value 1k
SYMBOL res 480 288 R90
SYMATTR InstName R2
SYMATTR Value 330
SYMBOL led 640 208 R180
SYMATTR InstName D1
SYMATTR Value LED
SYMBOL voltage 160 128 R0
SYMATTR InstName V1
SYMATTR Value PULSE(0 5 0 1ms 1ms 5ms 10ms)
TEXT 96 32 Left 2 !.tran 50ms
```

---

### Explanation of Components

1. **Voltage Source (V1)**:
   - A pulse signal `PULSE(0 5 0 1ms 1ms 5ms 10ms)`:
     - 0V (off state) and 5V (on state).
     - Rise and fall time: 1 ms.
     - On duration: 5 ms.
     - Period: 10 ms.

2. **Transistor (Q1)**:
   - NPN transistor (2N2222) acts as the switch.
   - Base voltage determines the LED state.

3. **Resistor (R1)**:
   - 1 kΩ resistor limits the base current to protect the transistor.

4. **Resistor (R2)**:
   - 330 Ω resistor limits the current through the LED.

5. **LED (D1)**:
   - Visualizes the on/off state controlled by the transistor.

6. **Simulation Command**:
   - `.tran 50ms`: Simulates the circuit for 50 ms to observe the switching behavior.

---

### Steps to Run in LTSpice

1. Save the `.asc` file and open it in LTSpice.
2. Run the **Transient Analysis** to observe the LED turning on and off based on the control signal applied to the transistor base.

This experiment demonstrates how a transistor functions as a switch to control an LED using a pulse input signal.
