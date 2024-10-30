PENDING

- Search youtube for this experiment

### Revised RC Circuit Experiment (for 5V battery)

#### Materials:
- 1 Resistor (e.g., 10kΩ)
- 1 Capacitor (e.g., 100μF)
- 1 Power source (5V battery)
- 1 Switch
- Connecting wires
- Multimeter (to measure voltage across the capacitor)
- Breadboard (optional for easy assembly)

#### Circuit Setup:
1. **Connect the resistor** in series with the capacitor.
2. **Connect the 5V battery** to the circuit.
3. **Place the switch** in series with the resistor and capacitor.
4. Connect a multimeter across the capacitor to measure its voltage.

### Procedure:

1. **Step 1: Charging the capacitor**
   - Close the switch to allow current to flow through the circuit.
   - Measure the voltage across the capacitor using the multimeter.
   - Observe how the voltage across the capacitor increases from 0V to 5V as the capacitor charges.

2. **Step 2: Discharging the capacitor**
   - Open the switch to disconnect the power source.
   - Watch the multimeter again and observe how the voltage across the capacitor decreases over time, eventually reaching 0V.

### Key Observations:
- The capacitor will charge up to **5V** and discharge back to 0V.
- The time constant (τ = R × C) will determine how fast the capacitor charges and discharges.

The simplest electronic circuit to learn about capacitors is a basic RC (Resistor-Capacitor) circuit. This circuit demonstrates capacitor charging and discharging, which is fundamental to understanding capacitor behavior. Let's design a simple experiment using this circuit.


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

Here's a description of the simple RC circuit experiment:

Components needed:
1. 9V battery
2. 1kΩ resistor
3. 100µF capacitor
4. Switch (optional, can use wire to connect/disconnect)
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

This simple experiment demonstrates the fundamental behavior of capacitors in DC circuits,  charging, discharging, and the concept of the time constant.

We can simulate this RC circuit using Python. We'll use the NumPy library for numerical calculations and Matplotlib for plotting the results. This simulation will show the charging and discharging of the capacitor over time.

Let's create a Python script to simulate this circuit:


```python
import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
V = 9.0  # Voltage source (9V)
R = 1000  # Resistance (1kΩ)
C = 100e-6  # Capacitance (100µF)
tau = R * C  # Time constant

# Time array
t = np.linspace(0, 1, 1000)  # 1 second, 1000 points

# Function to calculate voltage across capacitor during charging
def v_charging(t):
    return V * (1 - np.exp(-t / tau))

# Function to calculate voltage across capacitor during discharging
def v_discharging(t):
    return V * np.exp(-t / tau)

# Simulate charging for 0.5 seconds, then discharging
t_charge = t[t <= 0.5]
t_discharge = t[t > 0.5] - 0.5

v_charge = v_charging(t_charge)
v_discharge = v_discharging(t_discharge)

# Combine the results
v_total = np.concatenate([v_charge, v_discharge])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, v_total)
plt.title('RC Circuit - Capacitor Voltage vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.axvline(x=0.5, color='r', linestyle='--', label='Switch opened')
plt.legend()
plt.show()

# Print some key values
print(f"Time constant (tau): {tau:.6f} seconds")
print(f"Voltage at t=tau during charging: {v_charging(tau):.2f} V")
print(f"Voltage at t=5*tau during charging: {v_charging(5*tau):.2f} V")

```

This script simulates our RC circuit and plots the voltage across the capacitor over time. Here's a breakdown of what the code does:

1. We import NumPy for numerical calculations and Matplotlib for plotting.
2. We define our circuit parameters: V (voltage source), R (resistance), and C (capacitance).
3. We calculate the time constant (tau) of the circuit.
4. We create a time array for 1 second with 1000 points.
5. We define functions for charging and discharging voltages based on the RC circuit equations.
6. We simulate charging for the first 0.5 seconds, then discharging for the next 0.5 seconds.
7. We plot the results, showing the voltage across the capacitor over time.
8. Finally, we print some key values,  the time constant and voltages at specific times.

To run this simulation:

1. Make sure you have Python installed on your computer.
2. Install the required libraries if you haven't already:
   ```
   pip install numpy matplotlib
   ```
3. Copy the code into a Python file (e.g., `rc_circuit_simulation.py`).
4. Run the script:
   ```
   python rc_circuit_simulation.py
   ```

This simulation will generate a graph showing the capacitor voltage over time,  both the charging and discharging phases. It also prints out some key values to help understand the circuit behavior.

Using PySpice is an excellent choice for simulating electronic circuits in Python. PySpice provides a more comprehensive simulation environment that's closer to real-world circuit behavior. Here's how we can simulate our RC circuit using PySpice:


```python
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

# Create a new circuit
circuit = Circuit('RC Circuit')

# Define circuit parameters
V = 9@u_V  # 9V source
R = 1@u_kΩ  # 1kΩ resistor
C = 100@u_uF  # 100µF capacitor

# Create circuit elements
circuit.SinusoidalVoltageSource(1, 'input', 'input', 'ground', amplitude=V)
circuit.R(1, 'input', 'output', R)
circuit.C(1, 'output', 'ground', C)

# Run the simulation
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=1@u_ms, end_time=1@u_s)

# Extract time and voltage data
time = [float(t) for t in analysis.time]
voltage = [float(analysis['output']) for _ in analysis.time]

# Plotting
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(time, voltage)
plt.title('RC Circuit - Capacitor Voltage vs Time (PySpice Simulation)')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()

# Print some key values
tau = float(R * C)
print(f"Time constant (tau): {tau:.6f} seconds")
print(f"Voltage at t=tau: {voltage[int(tau*1000)]:.2f} V")
print(f"Voltage at t=5*tau: {voltage[int(5*tau*1000)]:.2f} V")

```

This script uses PySpice to simulate our RC circuit.

1. We import necessary modules from PySpice and create a new Circuit object.
2. We define our circuit parameters using PySpice's unit system.
3. We create circuit elements: a voltage source, a resistor, and a capacitor.
4. We run a transient analysis simulation for 1 second with 1ms steps.
5. We extract time and voltage data from the simulation results.
6. We plot the results using Matplotlib.
7. Finally, we print some key values,  the time constant and voltages at specific times.

To run this simulation:

1. Make sure you have Python installed on your computer.
2. Install PySpice and Matplotlib if you haven't already:
   ```
   pip install PySpice matplotlib
   ```
3. Copy the code into a Python file (e.g., `pyspice_rc_simulation.py`).
4. Run the script:
   ```
   python pyspice_rc_simulation.py
   ```

This simulation provides a more accurate representation of the circuit behavior,  the initial charging phase and any potential non-ideal behaviors that might occur in a real circuit.

The resulting graph will show the capacitor voltage over time, demonstrating how it charges up to the source voltage. The printed values will give you specific data points to understand the circuit's behavior.
