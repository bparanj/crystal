NEXT

See Current Limiting Transistor in personal account

An experiment to demonstrate current limiting using a transistor.

Components:

1. 2N2222 NPN transistor
2. LED
3. 1 kΩ resistor
4. 1 mΩ potentiometer
5. 9V battery or power supply
6. Breadboard and jumper wires

#### Step 1: 

- Place the 2N2222 NPN transistor on the breadboard, collector, base, emitter are in separate rows.
- Place the LED near the transistor
- Place the 1kΩ resistor and the 10kΩ potentiometer on the breadboard in separate locations for easy connections.

#### Step 2: 

1. Connect the negative terminal of the 9V battery to the negative rail on the breadboard.
2. Connect the positive terminal of the battery to the positive rail on the breadboard.

#### Step 3: 

Connect the LED to the Transistor

1. Connect the anode (long leg) of the LED to the positive rail on the breadboard.
2. Connect the cathode (short leg) of the LED to the collector of the transistor.

#### Step 4: 

Connect the Resistor to the Transistor Base

1. Connect one terminal of the 10kΩ potentiometer to the positive rail on the breadboard.
2. Connect the wiper (middle terminal) of the potentiometer to one terminal of the 1kΩ resistor.
3. Connect the other terminal of the 1kΩ resistor to the base of the transistor.

#### Step 5: 

Connect the Emitter to Ground

1. Connect the emitter of the transistor to the negative rail on the breadboard.

### Experiment

- Ensure the potentiometer is set to maximum resistance (fully turned in one direction).
- Turn on the simulation in Tinkercad.
- Slowly reduce the potentiometer resistance by turning it. Observe how the LED brightness increases as more base current flows into the transistor.

### Observations

- At maximum potentiometer resistance, the LED will be dim or off due to insufficient base current.
- As resistance decreases, more base current flows, causing the transistor to allow more current through the collector-emitter path.
- The LED brightness increases until it reaches maximum brightness, indicating saturation of the transistor.

This demonstrates the transistor's role as a current amplifier, controlled by the base current via the potentiometer.

The potentiometer will control the base current, which in turn limits the collector current

To perform the experiment:

2. Start with the potentiometer at maximum resistance
3. Turn on the simulation
4. Slowly decrease the potentiometer resistance
5. Observe how the LED brightness changes as you adjust the base current

results:

- When the potentiometer is at maximum resistance, the LED will be dim or off
- As you decrease the resistance, more base current flows
- The LED brightness will increase until it reaches maximum brightness
- The transistor prevents the LED from drawing too much current, protecting it from damage

You can use Tinkercad's built-in multimeter to measure:

- Base current at different potentiometer positions
- Collector current through the LED
- The relationship between base current and collector current (β or hFE)
