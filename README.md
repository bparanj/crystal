## Books

1. Fundamental Electrical and Electronic Principles by Christopher R Robertson
2. Teach Yourself Electricity and Electronics by Stan Gibilisco


I don't understand this statement:
Energy is power dissipated over a length of time.

Power is the rate at which energy is expended.

 • The current in a series circuit is the same at every point along the way.
 • The voltage across any component in a parallel circuit is the same as the voltage across any other, or across the whole set.
 • The voltages across elements in a series circuit always add up to the supply voltage.
 • The currents through elements in a parallel circuit always add up to the total current drawn from the supply.
 • The total power consumed in a series or parallel circuit is always equal to the sum of the wattages dissipated in each of the elements


https://www.circuit-fantasia.com/e-paradoxes/list_of_paradoxes.htm

## Electric Charge and Current

We need different units for electric charge and current because they measure different aspects of electricity:

Electric charge is measured in Coulombs (C). It represents the quantity of electric charge, or the amount of electrons, in a given situation. Think of it as the total amount of charge.

Current is measured in Amperes (A). It represents the rate at which electric charge flows past a point in a circuit. One Ampere is one Coulomb of charge flowing per second.

So, while charge is the amount of electricity, current is how fast that charge is moving. It’s a bit like how the volume of water in a tank is different from the flow rate of water coming out of a hose. Both are related but describe different things.

Electric charge, measured in Coulombs, is simply the total quantity of charge, with no regard for time. Current, on the other hand, measures how quickly this charge flows, hence it's measured in Amperes, which are Coulombs per second. Current is dynamic and considers the rate of charge flow over time.

So, you could think of electric charge as the "amount" of electricity and current as the "speed" at which this electricity moves through a circuit.

## Current and Magnetic Field

Small iron particles will be attracted by the magnetic field generated when a current passes through a coil. This is due to the magnetic properties of iron, which are influenced by the external magnetic field, causing the particles to align with the field and be drawn toward the coil. This principle is commonly used in devices like electromagnets.

The field around a positive or negative charge is called an electric field. It describes the force that a charge exerts on other charges in its vicinity.

Positive Charge:

The electric field radiates outward from the charge. If you place another positive charge nearby, it will feel a repulsive force pushing it away.

Negative Charge:

The electric field points inward toward the charge. If you place a positive charge nearby, it will feel an attractive force pulling it toward the negative charge.

These electric fields are visualized as lines radiating from or converging on the charges, with the direction of the lines indicating the direction of the force that would act on a positive test charge placed in the field. So, while magnets have magnetic fields, electric charges generate electric fields.

An electric field does not attract iron particles in the same way a magnetic field does. Iron particles are attracted to magnetic fields because iron is a ferromagnetic material, meaning it can be magnetized and is strongly attracted to magnets.

Electric fields, on the other hand, exert forces on charged particles. They attract or repel other electric charges depending on their polarity (positive or negative). Iron particles, being neutral in charge, do not respond to electric fields with attraction or repulsion.

So, while magnetic fields can pull iron particles toward them, electric fields influence only other charges.

## Changing Magnetic Field

Only a changing magnetic field can induce a current in a nearby coil, due to Faraday's Law of Electromagnetic Induction. This principle states that a change in the magnetic flux through a coil induces an electromotive force (EMF) in the coil, which drives the current.

A static electric field generated by positive and negative charges does not change over time, so it cannot induce a current in a nearby coil. It's the changing magnetic fields that create the necessary conditions for induction.

It's all about the dynamics of changing fields for induction to occur.

## Unit of Inductance

The henry (H) is the unit of inductance in electronics. Inductance measures the ability of a coil (or inductor) to store energy in a magnetic field when electrical current passes through it. One henry is defined as the inductance of a circuit in which a change in current of one ampere per second induces an electromotive force of one volt.

If a current changing at one ampere per second through an inductor causes a voltage of one volt across it, the inductor has an inductance of one henry. This unit is named after Joseph Henry, an American scientist who discovered electromagnetic induction independently of Michael Faraday.

## Electromotive Force

Electromotive force (EMF) is a broader term that refers to the energy provided per charge by an energy source, like a battery or generator. Voltage is one form of EMF, but it's not the only one. For instance, in electromagnetic induction, a changing magnetic field can induce an EMF, which can generate current in a coil — this is another form of EMF.

## Forms of EMF

Electromotive force (EMF) is the energy provided by a source per unit charge to drive electric current through a circuit. Different forms of EMF arise depending on how this energy is generated:

### 1. Chemical EMF

Source: Batteries, fuel cells

Generated through chemical reactions that separate positive and negative charges, creating a potential difference.

In a battery, chemical reactions between electrodes and electrolyte provide energy to move charges from one terminal to another.

### 2. Magnetic (Inductive) EMF

Source: Generators, inductors

Created by changing magnetic fields, according to Faraday’s Law of Electromagnetic Induction. A varying magnetic field induces an EMF in a conductor.

In an AC generator, a rotating coil in a magnetic field induces an EMF, which produces alternating current.

### 3. Thermal EMF (Thermoelectric Effect)

Source: Thermocouples

Generated when two different metals are joined and exposed to a temperature gradient. The temperature difference creates a potential difference, producing EMF.

Thermocouples use this effect to measure temperature by producing a voltage related to the temperature difference.

### 4. Photoelectric EMF

Source: Solar cells, photodiodes

Produced when light photons strike a material, typically a semiconductor, and excite electrons, creating a potential difference.

Solar cells generate EMF when sunlight hits the cell, creating current as electrons are freed from the material.

### 5. Piezoelectric EMF

Source: Piezoelectric crystals (e.g., quartz)

Produced by applying mechanical pressure to certain materials, which generates an electric field and thus an EMF.

Piezoelectric sensors generate EMF when subjected to vibrations or pressure, commonly used in microphones and accelerometers.

### 6. Electrostatic EMF

Source: Van de Graaff generators, capacitors

Created by separating charges through electrostatic means, creating a high-voltage EMF.

In a Van de Graaff generator, charges are accumulated on a sphere, creating a high voltage relative to ground.

Different forms of EMF include chemical, magnetic, thermal, photoelectric, piezoelectric, and electrostatic EMF, each generated through distinct mechanisms. These various forms allow for diverse applications across energy storage, power generation, sensing, and more.

## Function Generator

A function generator along with a DC power source can be used to turn on an LED in an electronic circuit. The function generator can provide the required signal (AC or pulsed DC), and the DC power source provides the necessary forward voltage and current. Include a current-limiting resistor in the circuit to protect the LED from excessive current.

If you only have a function generator and no DC power source, you can still turn on an LED using the function generator, as long as it can output a DC signal or an appropriate AC signal.

DC Signal:

Set the function generator to output a constant DC voltage that matches the LED’s forward voltage. Include a current-limiting resistor in the circuit to prevent excessive current from damaging the LED.

AC Signal:

If the function generator outputs an AC signal, the LED will only light up during the positive half-cycles when the voltage is in the correct polarity. This might cause the LED to flicker if the frequency is low.

In both cases, ensure the voltage and current are within the LED’s safe operating limits.

## Eliminate Flicker

Adding a capacitor in parallel to the resistor and LED can help reduce or even eliminate the flicker, depending on the capacitor's value and the frequency of the AC signal.

The capacitor will smooth out the voltage fluctuations by charging and discharging during the AC signal's cycles, providing a more stable DC-like voltage across the LED. This should reduce the flicker, especially at higher frequencies. The capacitor acts as a filter, smoothing out the variations and maintaining a more constant current through the LED.

Choose a capacitor with an appropriate value for your specific application to smooth out the fluctuations. Too small of a value might not adequately reduce the flicker, while too large of a value could affect the circuit's response time.

## Capacitor Choice

To choose the appropriate value of the capacitor and set the frequency on the function generator.

The capacitor value will depend on the LED's flicker frequency and the desired level of smoothing. The time constant (\( \tau \)) of the RC (resistor-capacitor) circuit is key:

\[ \tau = R \times C \]

- R is the resistance in ohms (Ω)
- C is the capacitance in farads (F)

For effective smoothing, the time constant should be at least 10 times the period of the AC signal. The period (\( T \)) is the inverse of the frequency (\( f \)):

\[ T = \frac{1}{f} \]

So, if the function generator's frequency is 60 Hz (a common choice for reducing flicker), the period is approximately 16.67 ms:

\[ \tau \approx 10 \times 16.67 \, ms \approx 167 \, ms \]

If you have a resistor \( R = 1k\Omega \):

\[ C = \frac{\tau}{R} = \frac{167 \, ms}{1000 \, \Omega} = 167 \, \mu F \]

So, a capacitor around 167 microfarads (μF) would be a good starting point.

### Setting the Frequency on the Function Generator

To reduce flicker, set the function generator to a frequency higher than the flicker detection threshold of the human eye (typically above 50-60 Hz). A common choice is 60 Hz or higher.

Higher frequencies (e.g., 1 kHz) can provide smoother illumination but may require a larger capacitor to smooth effectively, balancing between the capacitor value and the flicker reduction.

Capacitor Value:

Use the time constant formula and ensure it's at least 10 times the period of your chosen frequency.

Frequency:

Set the function generator to at least 60 Hz to reduce visible flicker, higher if smoother illumination is desired.
