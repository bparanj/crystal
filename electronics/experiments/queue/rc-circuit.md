

You can add a LED to visually show the charging and discharging of capacitor.

PENDING

This is the same as the existing capacitor experiment #7. Merge or delete this document.


Let's design a simple experiment using this circuit.


```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <!-- Battery -->
  <line x1="50" y1="50" x2="50" y2="150" stroke="black" stroke-width="2"/>
  <line x1="60" y1="70" x2="60" y2="130" stroke="black" stroke-width="2"/>
  <text x="30" y="100" font-size="14">9V</text>

  <!-- Resistor -->
  <line x1="100" y1="50" x2="130" y2="50" stroke="black" stroke-width="2"/>
  <path d="M130 50 Q140 30 150 50 Q160 70 170 50 Q180 30 190 50" fill="none" stroke="black" stroke-width="2"/>
  <line x1="190" y1="50" x2="220" y2="50" stroke="black" stroke-width="2"/>
  <text x="155" y="30" font-size="14">1kΩ</text>

  <!-- Capacitor -->
  <line x1="220" y1="50" x2="220" y2="70" stroke="black" stroke-width="2"/>
  <line x1="200" y1="70" x2="240" y2="70" stroke="black" stroke-width="2"/>
  <line x1="200" y1="80" x2="240" y2="80" stroke="black" stroke-width="2"/>
  <line x1="220" y1="80" x2="220" y2="150" stroke="black" stroke-width="2"/>
  <text x="245" y="80" font-size="14">100µF</text>

  <!-- Switch -->
  <circle cx="100" cy="50" r="3" fill="black"/>
  <line x1="50" y1="50" x2="97" y2="50" stroke="black" stroke-width="2"/>
  <line x1="100" y1="50" x2="120" y2="30" stroke="black" stroke-width="2"/>
  <text x="80" y="30" font-size="14">S</text>

  <!-- Ground -->
  <line x1="50" y1="150" x2="220" y2="150" stroke="black" stroke-width="2"/>
  <line x1="125" y1="150" x2="145" y2="150" stroke="black" stroke-width="4"/>
  <line x1="130" y1="155" x2="140" y2="155" stroke="black" stroke-width="3"/>
  <line x1="133" y1="160" x2="137" y2="160" stroke="black" stroke-width="2"/>
</svg>

```

A simple RC circuit experiment:

Components:

1. 9V battery
2. 1kΩ resistor
3. 100µF capacitor
4. Switch
5. Breadboard and jumper wires

Circuit setup:

1. Connect the positive terminal of the 9V battery to one side of the switch.
2. Connect the other side of the switch to one end of the 1kΩ resistor.
3. Connect the other end of the resistor to one lead of the 100µF capacitor.
4. Connect the negative terminal of the battery to the other lead of the capacitor.

Experiment procedure:

1. Charging the capacitor:

   - Close the switch (or connect the wire).
   - The capacitor will start charging through the resistor.
   - You can measure the voltage across the capacitor with a multimeter to see it increase over time.

2. Discharging the capacitor:

   - Open the switch (or disconnect the wire).
   - The capacitor will start discharging through the resistor.
   - You can measure the voltage across the capacitor to see it decrease over time.

3. Observations:

   - Notice how the capacitor charges quickly at first, then slows down as it approaches full charge.
   - Similarly, it discharges quickly at first, then more slowly.
   - The time constant (τ) of this circuit is R * C = 1kΩ * 100µF = 0.1 seconds.
   - It takes about 5 time constants (0.5 seconds) to fully charge or discharge the capacitor.

This simple experiment demonstrates the fundamental behavior of capacitors in DC circuits, charging, discharging, and the concept of the time constant.
