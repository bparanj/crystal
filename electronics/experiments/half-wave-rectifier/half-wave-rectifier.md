Half Wave Rectifier

Components

0

Steps

Step 1

Take a breadboard

a1

Step 2

Take a function generator. 

a2

Change the settings to: frequency: 500 Hz, amplitude: 5 volts, DC offset: 0, function: sine.

a3

Step 2

Take a diode. Connect it to i4 and i8 in the breadboard.

a4

Step 3


Cathode of the diode:

a6

Connect the cathode of the diode to one side of the 1 k ohm resistor. The resistor is connected to f8 and d8 in the breadboard.

a7

Step 4

Connect the other end of the resistor to the negative terminal in the power rails of the breadboard. This is the black line from a8 to the ground.

a8

Step 5

Anode of the diode:

a5

Connect the anode of the diode to the positive terminal of the power rails in the breadboard. This is the red line from j4 to the positive terminal.

a9

Step 6

Take a oscilloscope. 

a10

Change time per division to 2 ms.

a11

Step 7

Connect the function generator to the breadboard.

a12

Step 8

Connect the oscilloscope to the function generator. 

a13

This will be the input oscilloscope.

Step 9

Take another oscilloscope to observe the output. 

a14

Change the time per division to 2 ms.

Step 10

Connect the output oscilloscope across the resistor.

a15

Step 11

Run the simulation. Input oscilloscope shows the sine wave form at 500 Hz. The output oscilloscope shows the sine wave form with the negative cycles removed. It stops at the horizontal line of the output oscilloscope.

a16

In an AC circuit, it allows only the positive half-cycles of the waveform to pass through, blocking the negative half-cycles, creating a pulsating DC output.

Half Wave Rectifier with Smoothing

Step 1

Add a 100 micro Farad capacitor to the circuit. Connect it to g15 and g16 in the breadboard.

s1

Step 2

Connect the first terminal of the capacitor to the point where the diode and resistor meet. This is the green line from g8 to g15.

s2

Step 3

Connect the second terminal of the capacitor to the ground. This is the black line from f16 to the ground.

s3

Step 4

Run the simulation. You can see the voltage is now DC. Capacitor is used to smoothen the voltage. If you look closely there is ripples in the output wave.

s4

Questions

Do we really need an LED when oscilloscopes are used to observe the input and output?

Rectifiers can be found in AC-to-DC conversion used in almost every electronic power supply.
