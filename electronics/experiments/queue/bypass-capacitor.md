# Bypass Capacitor

## Components

- DC Power Supply (5V)
- Ceramic Capacitor (0.1µF)
- Two LEDs
- Two Push Buttons
- Two Resistors (220Ω)
- Digital Oscilloscope
- Breadboard and connecting wires

## Setup

### Control Circuit (Without Bypass)

1. Connect first LED and 220Ω resistor in series
2. Add push button to control LED
3. Connect to power supply

### Test Circuit (With Bypass)

1. Set up identical LED circuit
2. Add 0.1µF capacitor between power and ground
3. Place capacitor as close as possible to LED circuit

## Experiment

### Part 1: Baseline Measurement

1. Connect oscilloscope probe to power rail
2. Set oscilloscope:
   - Timebase: 100µs/division
   - Voltage: 1V/division
   - Trigger: Rising edge

### Part 2: Testing

1. Press buttons in sequence:
   a. Control circuit button only
   b. Test circuit button only
   c. Both buttons simultaneously
   d. Rapidly toggle buttons

### Measurements to Record

1. Voltage ripple without bypass capacitor
2. Voltage ripple with bypass capacitor
3. Transient response during switching
4. Recovery time after load changes

### Observations

- Without bypass: Visible voltage fluctuations when switching
- With bypass: More stable voltage during switching
- LED brightness should be more stable in bypassed circuit

## Analysis

1. Peak-to-peak voltage ripple
2. Settling time after transients
3. Effect on LED brightness stability

## Variables to Experiment With

- Different capacitor values
- Different switching speeds
- Multiple LEDs for increased load

An experiment to demonstrate how bypass capacitors filter out noise and stabilize voltage can be set up using basic components in Tinkercad. The experiment will show how a bypass capacitor helps maintain steady voltage when there are sudden changes in current draw.



This experiment demonstrates three key bypass capacitor functions:
1. Noise reduction during switching
2. Voltage stabilization during current changes
3. Transient response improvement

The oscilloscope will show:
- Voltage spikes without the bypass capacitor
- Smoother voltage with the bypass capacitor
- Reduced recovery time after load changes

To demonstrate a bypass capacitor we can create a circuit that shows how it stabilizes the voltage by filtering out noise, especially in circuits with AC signals or switching transients.

### Setup

#### Components:

- DC Power Source (9V battery)
- Signal Generator (square wave at 100 Hz, 5V amplitude)
- Resistors (e.g., 1kΩ)
- Capacitors (e.g., 100nF for bypass)
- NPN Transistor (e.g., 2N2222 to simulate a switching load)
- Oscilloscope (to measure voltage ripple)

#### Circuit Design:

1. Set Up the Power and Load Circuit:
   - Connect the 9V DC battery as the power source.
   - Create a simple load circuit with an NPN transistor and resistor to simulate a device that switches on and off, causing fluctuations on the power rail.
   - Connect the emitter of the NPN transistor to ground, the collector to a 1kΩ resistor, and the other end of the resistor to the positive terminal of the battery.

2. Add the Signal Generator:
   - Connect the signal generator to the base of the transistor with a small current-limiting resistor (e.g., 10kΩ). Set the signal generator to output a 100 Hz square wave (5V amplitude) to toggle the transistor on and off.
   - This setup will create voltage fluctuations on the power line as the transistor switches, mimicking noise.

3. Place the Bypass Capacitor:
   - Place a 100nF capacitor between the power rail (9V) and ground near the transistor. This capacitor will act as a bypass capacitor, smoothing out the voltage fluctuations by providing a low-impedance path for AC noise.

4. Connect the Oscilloscope:
   - Attach the oscilloscope across the power rail (between 9V and ground) to observe the voltage before and after adding the bypass capacitor.
   - Initially, observe the power rail without the capacitor, noting the ripple or noise caused by the switching transistor.
   - Then, connect the capacitor and observe how the ripple reduces, demonstrating the capacitor’s role in stabilizing the voltage.

#### Observations:

- Without the bypass capacitor, the oscilloscope should show noticeable fluctuations or ripple on the power rail due to the switching action of the transistor.
- When the bypass capacitor is added, the oscilloscope will show a smoother voltage with reduced ripple, as the capacitor filters out the high-frequency noise from the switching transistor.

The bypass capacitor provides a quick source of current when the load switches, reducing voltage fluctuations on the power line by shorting high-frequency noise to ground. This demonstrates the capacitor's function as a bypass capacitor, stabilizing power and protecting sensitive components.
