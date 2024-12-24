PENDING

Extract content from dc-decoupling.md and delete that file after merging with this document.

DC Decoupling

Components

0

Steps

Step 1

Take a breadboard.

Image 1

Step 2

Take a diode. Connect it to i4 and i8 in the breadboard.

Image 2

Anode is connected to i4 in the breadboard.

image 3

Cathode is connected to i8 in the breadboard.

image 4

Step 3

Connect 1 k ohm resistor to the cathode of the diode. Resistor is on f8 and d8 in the breadboard.

Image 5

Step 4

Connect the other end of the resistor to the ground. This is the black line from a8 to the ground.

Image 6

Step 5

Connect the anode of the diode to the positive terminal of the power rails in the breadboard.

Image 7

Step 6

Take a DC power supply. Set the voltage to : 10 volts. The default setting of current is at 5.

Image 8

Step 7

Connect the power supply to the breadboard.

Image 9

Step 8

Take a multimeter. The settings must be to measure the voltage.

Image 10

Step 9

Connect the multimeter across the resistor to measure the voltage.

Image 11

Step 10

Run the simulation. You will observe the voltage drop of 9.41 volts across the resistor.

Image 12

Step 11

Change the diode position, such that the cathode is connected to the positive terminal and the anode is connected to the resistor.

Image 13

Cathode of diode is connected to i4 in the breadboard:

image 14

Anode of the diode is connected to i8 in the breadboard:

image 15

Step 12

Run the simulation. The voltage across the resistor is now 0. Because the diode blocks the current flow when connected in reverse bias.

Image 16
