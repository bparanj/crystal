
TAG

relay

The simplest electronic circuit to learn about relays is using a relay to control a higher-power device with a lower-power signal. 

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
  <!-- Control Circuit -->
  <text x="20" y="30" font-size="14">Control Circuit</text>
  <!-- Battery -->
  <line x1="50" y1="50" x2="50" y2="150" stroke="black" stroke-width="2"/>
  <line x1="60" y1="70" x2="60" y2="130" stroke="black" stroke-width="2"/>
  <text x="30" y="100" font-size="14">5V</text>

  <!-- Switch -->
  <circle cx="100" cy="50" r="3" fill="black"/>
  <line x1="50" y1="50" x2="97" y2="50" stroke="black" stroke-width="2"/>
  <line x1="100" y1="50" x2="120" y2="30" stroke="black" stroke-width="2"/>
  <text x="110" y="25" font-size="14">S</text>

  <!-- Relay Coil -->
  <rect x="150" y="30" width="40" height="80" fill="none" stroke="black" stroke-width="2"/>
  <text x="155" y="70" font-size="14">Relay</text>
  <text x="155" y="85" font-size="14">Coil</text>

  <!-- Load Circuit -->
  <text x="220" y="30" font-size="14">Load Circuit</text>
  <!-- Power Source -->
  <line x1="250" y1="50" x2="250" y2="150" stroke="black" stroke-width="2"/>
  <line x1="260" y1="70" x2="260" y2="130" stroke="black" stroke-width="2"/>
  <text x="230" y="100" font-size="14">12V</text>

  <!-- Relay Contact -->
  <line x1="300" y1="50" x2="320" y2="50" stroke="black" stroke-width="2"/>
  <line x1="320" y1="50" x2="340" y2="70" stroke="black" stroke-width="2"/>
  <line x1="340" y1="70" x2="360" y2="70" stroke="black" stroke-width="2"/>

  <!-- LED -->
  <circle cx="360" cy="100" r="10" fill="none" stroke="black" stroke-width="2"/>
  <line x1="355" y1="95" x2="365" y2="105" stroke="black" stroke-width="2"/>
  <line x1="355" y1="105" x2="365" y2="95" stroke="black" stroke-width="2"/>

  <!-- Ground -->
  <line x1="50" y1="150" x2="360" y2="150" stroke="black" stroke-width="2"/>
  <line x1="195" y1="150" x2="215" y2="150" stroke="black" stroke-width="4"/>
  <line x1="200" y1="155" x2="210" y2="155" stroke="black" stroke-width="3"/>
  <line x1="203" y1="160" x2="207" y2="160" stroke="black" stroke-width="2"/>
</svg>

```

This simple relay circuit consists of two main parts:

1. Control Circuit (Low power):

   - 5V power source (e.g., battery or power supply)
   - Switch
   - Relay coil

2. Load Circuit (Higher power):

   - 12V power source
   - Relay contact (switch controlled by the relay coil)
   - LED (representing the load)

Here's how this circuit works:

1. When the switch in the control circuit is open:

   - No current flows through the relay coil
   - The relay contact in the load circuit remains open
   - The LED is off

2. When the switch in the control circuit is closed:

   - Current flows through the relay coil, energizing it
   - The magnetic field created by the coil closes the relay contact in the load circuit
   - The LED turns on

Components:

1. 5V power source (for the control circuit)
2. 12V power source (for the load circuit)
3. SPST (Single Pole Single Throw) switch
4. Relay (5V coil voltage, contacts rated for at least 12V)
5. LED
6. Resistor (appropriate for the LED,  220Ω to 1kΩ)
7. Breadboard and jumper wires

Learning:

1. Electrical isolation: The control circuit and load circuit are electrically isolated from each other.
2. Power amplification: A low-power signal (5V) controls a higher-power circuit (12V).
3. Switching: The relay acts as an electrically controlled switch.

This circuit demonstrates the basic principle of a relay: using a low-power signal to control a higher-power circuit. It's a foundational concept in electronics and automation.

To expand on this experiment, you could:

1. Add a flyback diode across the relay coil to protect against voltage spikes
2. Use the relay to control a motor or other high-power device instead of an LED
3. Implement transistor-based relay control for even lower power switching
