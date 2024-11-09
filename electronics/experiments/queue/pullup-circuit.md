
Is this the same: https://www.tinkercad.com/things/hrMmi5ZQvhw-resistor-pull-up-and-pull-down

## Pull-up circuit

1. Basic Pull-up Circuit:
   - Power supply (battery or DC source)
   - Pull-up resistor (typically 1kΩ to 10kΩ)
   - Push button or switch
   - LED (with current limiting resistor)
   - Ground connection

2. Circuit Operation:
   - When switch is OPEN:
      LED gets HIGH through pull-up resistor
      LED lights up
   - When switch is CLOSED:
      Node is connected to ground
      LED turns off

3. Components needed:
   - 5V DC supply
   - 10kΩ pull-up resistor
   - Push button switch
   - LED
   - 220Ω current limiting resistor for LED

This demonstrates the basic principle of pull-up resistors:

- Ensures a defined logic level (HIGH) when input is floating
- Prevents floating inputs
- Shows how pull-up affects input states

We can observe the pull-up effect using just an LED, a resistor, a pushbutton, and a power supply.

### Objective

To demonstrate how a pull-up resistor stabilizes a HIGH voltage level when a switch is open and pulls it to a LOW level when the switch is closed.

### Components

- 1 x Resistor (10 kΩ for pull-up)
- 1 x LED (to visualize the output)
- 1 x Pushbutton switch
- 1 x Power supply (5V or 3.3V)
- 1 x Resistor (330Ω for LED current limiting)
- Connecting wires

### Setup

1. Power Supply: Connect the positive terminal of the power supply (5V or 3.3V) to the pull-up resistor.
2. Pull-Up Resistor: Connect a 10 kΩ resistor from the positive terminal to one side of the pushbutton switch.
3. Switch and Ground:
   - Connect the other side of the pushbutton switch to ground (GND).
4. LED and Observation Point:
   - At the junction between the resistor and the pushbutton switch, connect the positive (anode) side of the LED.
   - Connect the other side of the LED to ground through a 330Ω resistor to limit current.

### Procedure

1. Switch Open:
   - When the switch is open, the junction between the resistor and switch is “pulled up” to the positive voltage through the 10 kΩ resistor.
   - The LED will remain off in this state, as there is no direct path for current through the LED to ground.

2. Switch Closed:
   - When the switch is pressed (closed), the junction between the resistor and switch is connected directly to ground, bringing the voltage at this point to LOW.
   - The LED will light up as current flows from the positive terminal, through the resistor, and through the LED to ground.

The pull-up resistor keeps the junction at a HIGH level when the switch is open, preventing it from floating. When the switch is pressed, it provides a clear path to ground, bringing the junction to a LOW state, which allows the LED to light up.

This experiment shows the role of a pull-up resistor in maintaining a stable high voltage level when a switch is open and how it shifts to a low voltage when the switch is closed, activating the LED.
