Experiments to demonstrate and plot the I-V characteristics of resistors and diodes.


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def simulate_resistor_data(voltage_range, resistance=1000, noise_level=0.001):
    """
    Simulate resistor I-V data with some experimental noise
    """
    current = voltage_range / resistance
    noise = np.random.normal(0, noise_level, len(voltage_range))
    return current + noise

def simulate_diode_data(voltage_range, Is=1e-12, Vt=0.026, noise_level=1e-6):
    """
    Simulate diode I-V data using Shockley equation with noise
    Is: reverse saturation current
    Vt: thermal voltage (~26mV at room temperature)
    """
    current = Is * (np.exp(voltage_range/Vt) - 1)
    noise = np.random.normal(0, noise_level, len(voltage_range))
    return current + noise

def run_experiments():
    # Create voltage ranges for measurements
    resistor_voltage = np.linspace(-5, 5, 100)
    diode_voltage = np.linspace(-1, 1, 200)  # More points around origin for diode
    
    # Simulate measurement data
    resistor_current = simulate_resistor_data(resistor_voltage)
    diode_current = simulate_diode_data(diode_voltage)
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot resistor characteristics
    ax1.plot(resistor_voltage, resistor_current * 1000, 'b.', label='Measured Data')
    ax1.set_xlabel('Voltage (V)')
    ax1.set_ylabel('Current (mA)')
    ax1.set_title('Resistor I-V Characteristics')
    ax1.grid(True)
    ax1.legend()
    
    # Plot diode characteristics
    ax2.plot(diode_voltage, diode_current * 1000, 'r.', label='Measured Data')
    ax2.set_xlabel('Voltage (V)')
    ax2.set_ylabel('Current (mA)')
    ax2.set_title('Diode I-V Characteristics')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    return fig

# Function to perform actual experiments (pseudocode)
def real_experiment_setup():
    """
    Pseudocode for actual experimental setup
    """
    experiment_steps = """
    Equipment needed:
    1. Variable DC power supply (0-10V)
    2. Digital multimeter (voltage and current measurement)
    3. Resistor (1kΩ)
    4. Silicon diode (1N4148 or similar)
    5. Breadboard
    6. Connecting wires
    
    Resistor Experiment Steps:
    1. Connect resistor to power supply
    2. Connect voltmeter in parallel with resistor
    3. Connect ammeter in series with circuit
    4. Vary voltage from -5V to +5V in 0.5V steps
    5. Record voltage and current readings
    
    Diode Experiment Steps:
    1. Connect diode to power supply (observe polarity)
    2. Connect voltmeter in parallel with diode
    3. Connect ammeter in series with circuit
    4. Add current-limiting resistor for protection
    5. Vary voltage from -1V to +1V in 0.1V steps
    6. Record voltage and current readings
    
    Safety Considerations:
    - Never exceed component ratings
    - Include current-limiting resistor with diode
    - Double-check polarity of components
    - Verify meter settings before connecting
    """
    return experiment_steps

# Run simulation
fig = run_experiments()

```

I've created a complete experimental setup that includes both simulation code and practical experimental guidelines. Here's what's included:

1. For the Resistor (Linear Relationship):

- Voltage range: -5V to +5V
- Shows perfect linear relationship (Ohm's Law)
- Includes simulated measurement noise for realism
- Plots I-V curve showing linear characteristics

2. For the Diode (Non-linear Relationship):

- Voltage range: -1V to +1V (typical for silicon diodes)
- Uses Shockley diode equation to model behavior
- Shows exponential relationship in forward bias
- Demonstrates near-zero current in reverse bias

3. Practical Setup:

- Lists required equipment
- Provides step-by-step instructions
- Includes safety considerations
- Specifies measurement ranges and steps

To conduct the actual experiments:
1. Use the power supply to apply voltage in steps
2. Measure both voltage across and current through each component
3. Record data points in a table
4. Plot the results using the provided code

Would you like me to:
1. Explain any part of the code in more detail?
2. Add error analysis to the measurements?
3. Include additional component characteristics?

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def simulate_resistor_data(voltage_range, resistance=1000, noise_level=0.001):
    """
    Simulate resistor I-V data with some experimental noise
    """
    current = voltage_range / resistance
    noise = np.random.normal(0, noise_level, len(voltage_range))
    return current + noise

def simulate_diode_data(voltage_range, Is=1e-12, Vt=0.026, noise_level=1e-6):
    """
    Simulate diode I-V data using Shockley equation with noise
    Is: reverse saturation current
    Vt: thermal voltage (~26mV at room temperature)
    """
    current = Is * (np.exp(voltage_range/Vt) - 1)
    noise = np.random.normal(0, noise_level, len(voltage_range))
    return current + noise

def run_experiments():
    # Create voltage ranges for measurements
    resistor_voltage = np.linspace(-5, 5, 100)
    diode_voltage = np.linspace(-1, 1, 200)  # More points around origin for diode
    
    # Simulate measurement data
    resistor_current = simulate_resistor_data(resistor_voltage)
    diode_current = simulate_diode_data(diode_voltage)
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot resistor characteristics
    ax1.plot(resistor_voltage, resistor_current * 1000, 'b.', label='Measured Data')
    ax1.set_xlabel('Voltage (V)')
    ax1.set_ylabel('Current (mA)')
    ax1.set_title('Resistor I-V Characteristics')
    ax1.grid(True)
    ax1.legend()
    
    # Plot diode characteristics
    ax2.plot(diode_voltage, diode_current * 1000, 'r.', label='Measured Data')
    ax2.set_xlabel('Voltage (V)')
    ax2.set_ylabel('Current (mA)')
    ax2.set_title('Diode I-V Characteristics')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    return fig

# Function to perform actual experiments (pseudocode)
def real_experiment_setup():
    """
    Pseudocode for actual experimental setup
    """
    experiment_steps = """
    Equipment needed:
    1. Variable DC power supply (0-10V)
    2. Digital multimeter (voltage and current measurement)
    3. Resistor (1kΩ)
    4. Silicon diode (1N4148 or similar)
    5. Breadboard
    6. Connecting wires
    
    Resistor Experiment Steps:
    1. Connect resistor to power supply
    2. Connect voltmeter in parallel with resistor
    3. Connect ammeter in series with circuit
    4. Vary voltage from -5V to +5V in 0.5V steps
    5. Record voltage and current readings
    
    Diode Experiment Steps:
    1. Connect diode to power supply (observe polarity)
    2. Connect voltmeter in parallel with diode
    3. Connect ammeter in series with circuit
    4. Add current-limiting resistor for protection
    5. Vary voltage from -1V to +1V in 0.1V steps
    6. Record voltage and current readings
    
    Safety Considerations:
    - Never exceed component ratings
    - Include current-limiting resistor with diode
    - Double-check polarity of components
    - Verify meter settings before connecting
    """
    return experiment_steps

# Run simulation
fig = run_experiments()