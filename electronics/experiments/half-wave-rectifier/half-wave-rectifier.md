Check biz account Half Wave Rectifier

Resistor
Diode
Oscilloscopes to observe the input and output

Components

1 k ohm resistor
Function generator:
Diode

Steps

Step 1

Take a function generator and change the settings to: frequency: 500 Hz, amplitude: 5 volts, DC offset: 0, function: sine.

Step 2

Take a oscilloscope. Change time per division to 2 ms.

Step 3

Connect the oscilloscope to the function generator. This will be the input oscilloscope.

Step 4

Connect the anode of the diode to the positive terminal of the power rails in the breadboard.


Step 5

Connect the cathode of the diode to one end of the 1 k ohm resistor.


Step 6

Connect the other end of the resistor to the negative terminal in the power rails of the breadboard.


Step 7

Take anothe oscilloscope to observe the output. Change the time per division to 2 ms.

Step 8

Connect the output oscilloscope across the resistor.


Step 9

Run the simulation. Input oscilloscope shows the sine wave form at 500 Hz. The output oscilloscope shows the sine wave form with the negative cycles removed. It stops at the horizontal line of the output oscilloscope.

Step 10

Add a 100 micro Farad capacitor to the circuit. Connect it to g15 and g16 in the breadboard.

Step 11

Connect the first terminal of the capacitor to the point where the diode and resistor meet. This is the green line from g8 to g15.

Step 12

Connect the second terminal of the capacitor to the ground. This is the black line from f16 to the ground.

Step 13

Run the simulation. You can see the voltage is now DC. Capacitor is used to smoothen the voltage.

Questions

Do we really need an LED when oscilloscopes are used to observe the input and output?

### **Half-Wave Rectification**

Demonstrate how a diode allows current to flow in only one direction by converting an AC signal into a pulsating DC signal through **half-wave rectification**.

### **Components**

1. **AC Power Source** (e.g., 5V AC)
2. **Diode** (e.g., 1N4007)
3. **LED** with appropriate resistor for current limiting

A diode acts as a one-way valve for current. In an AC circuit, it allows only the positive half-cycles of the waveform to pass through, blocking the negative half-cycles, creating a pulsating DC output.

### **Steps**

#### Step 1:

1. Connect one terminal of the AC power source to the **anode** of the diode.
2. Connect the **cathode** of the diode to one terminal of the resistor.

Turn on the AC power source.

### **Concepts Demonstrated**

1. **Rectification:**
   - The diode converts AC to pulsating DC by blocking half of the waveform.
2. **Directionality of Current:**
   - The diode’s behavior shows that current flows only in one direction, a property of diodes.

   - Demonstrates the principle behind rectifiers used in power supplies.

### **Applications**

Rectifiers can be found in AC-to-DC conversion used in almost every electronic power supply.

