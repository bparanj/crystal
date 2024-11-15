an experiment that demonstrates how a capacitor can be used for timing in electronic circuits using a simple LED flasher circuit.
PENDING

Move to out of scope folder

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_timing(R, C):
    """
    Calculate timing characteristics for RC circuit
    R: Resistance in ohms
    C: Capacitance in farads
    """
    tau = R * C  # Time constant
    charge_time = 5 * tau  # Time to fully charge (5 time constants)
    frequency = 1 / (2 * charge_time)  # Oscillation frequency

    # Calculate voltage over time
    t = np.linspace(0, charge_time, 1000)
    v_charge = 9 * (1 - np.exp(-t / tau))
    v_discharge = 9 * np.exp(-t / tau)

    return {
        'tau': tau,
        'charge_time': charge_time,
        'frequency': frequency,
        't': t,
        'v_charge': v_charge,
        'v_discharge': v_discharge
    }

# Example calculation for 100kΩ and 100µF
R = 100000  # 100kΩ
C = 0.0001  # 100µF

results = calculate_timing(R, C)
print(f"Time constant (τ): {results['tau']:.2f} seconds")
print(f"Charge time (5τ): {results['charge_time']:.2f} seconds")
print(f"Oscillation frequency: {results['frequency']:.2f} Hz")

# Plot voltage curves
plt.figure(figsize=(10, 6))
plt.plot(results['t'], results['v_charge'], label='Charging')
plt.plot(results['t'], results['v_discharge'], label='Discharging')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Charging and Discharging Curves')
plt.grid(True)
plt.legend()
plt.show()

```

Here's a detailed experiment to demonstrate capacitor timing:

Components:

1. 2x 2N2222 NPN transistors
2. 2x LEDs (different colors recommended)
3. 2x 1kΩ resistors (LED current limiting)
4. 2x 100kΩ resistors (timing control)
5. 1x 100µF electrolytic capacitor
6. 9V battery or power supply
7. Breadboard and jumper wires

Setup:

1. Build the circuit as shown in the diagram
2. Make sure to observe the correct polarity of:
   - LEDs (longer lead is positive)
   - Capacitor (marked negative stripe)
   - Transistors (flat side orientation)

How it works:

1. The circuit creates an astable multivibrator where the LEDs flash alternatively
2. The capacitor charging and discharging time determines the flash rate
3. The 100kΩ resistors and 100µF capacitor create the RC time constant
4. The timing follows the formula: T = RC (time constant)

Measurements to make:

1. Use Tinkercad's oscilloscope to observe:
   - Capacitor voltage
   - LED voltage
   - Timing of the flashing sequence

Results:

1. LEDs will flash alternatively
2. With the given components:
   - Time constant (τ) = 100kΩ × 100µF = 0.01 seconds
   - Full cycle ≈ 0.02 seconds
   - Flash frequency ≈ 50 Hz

Variations:

1. Change the capacitor value to alter the timing:
   - Larger capacitor = slower flashing
   - Smaller capacitor = faster flashing
2. Change the resistor values:
   - Larger resistors = slower flashing
   - Smaller resistors = faster flashing

Variables to explore:

1. Try different RC combinations:
   - 47µF capacitor with 220kΩ resistors
   - 220µF capacitor with 47kΩ resistors
2. Observe how the timing changes with temperature (can be simulated in Tinkercad)

Python script that helps visualize the charging and discharging curves and calculate timing characteristics. You can modify the R and C values to predict the behavior before building the circuit.
