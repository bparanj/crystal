```python
import numpy as np
import matplotlib.pyplot as plt

def visualize_circuit_energy():
    # Create figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # Plot 1: Energy Distribution in Common Circuits
    components = ['Resistor', 'Inductor', 'Capacitor', 'LED', 'Transistor']
    thermal = [95, 10, 5, 70, 30]  # %
    magnetic = [0, 85, 0, 0, 0]    # %
    electric = [0, 0, 90, 0, 0]    # %
    light = [0, 0, 0, 25, 0]       # %
    other = [5, 5, 5, 5, 70]       # %

    width = 0.35
    ax1.bar(components, thermal, width, label='Thermal', color='red')
    ax1.bar(components, magnetic, width, bottom=thermal, label='Magnetic', color='blue')
    ax1.bar(components, electric, width, bottom=np.array(thermal)+np.array(magnetic),
            label='Electric Field', color='yellow')
    ax1.bar(components, light, width, bottom=np.array(thermal)+np.array(magnetic)+np.array(electric),
            label='Light', color='green')
    ax1.bar(components, other, width, bottom=np.array(thermal)+np.array(magnetic)+np.array(electric)+np.array(light),
            label='Other', color='gray')

    ax1.set_ylabel('Energy Distribution (%)')
    ax1.set_title('Energy Types in Circuit Components')
    ax1.legend()

    # Plot 2: Capacitor Energy Storage
    voltage = np.linspace(0, 10, 100)
    capacitances = [1e-6, 2e-6, 5e-6]  # Farads

    for C in capacitances:
        energy = 0.5 * C * voltage2
        ax2.plot(voltage, energy * 1e6, label=f'{C*1e6}µF')

    ax2.set_xlabel('Voltage (V)')
    ax2.set_ylabel('Energy (µJ)')
    ax2.set_title('Capacitor Energy Storage')
    ax2.grid(True)
    ax2.legend()

    # Plot 3: Inductor Energy Storage
    current = np.linspace(0, 2, 100)
    inductances = [1e-3, 2e-3, 5e-3]  # Henries

    for L in inductances:
        energy = 0.5 * L * current2
        ax3.plot(current, energy * 1e3, label=f'{L*1e3}mH')

    ax3.set_xlabel('Current (A)')
    ax3.set_ylabel('Energy (mJ)')
    ax3.set_title('Inductor Energy Storage')
    ax3.grid(True)
    ax3.legend()

    # Plot 4: Heat Generation in Resistors
    time = np.linspace(0, 10, 100)
    currents = [0.1, 0.2, 0.5]  # Amperes
    R = 100  # Ohms

    for I in currents:
        power = I2 * R
        energy = power * time
        ax4.plot(time, energy, label=f'{I}A')

    ax4.set_xlabel('Time (s)')
    ax4.set_ylabel('Thermal Energy (J)')
    ax4.set_title('Resistor Heat Generation')
    ax4.grid(True)
    ax4.legend()

    plt.tight_layout()
    return fig

def explain_circuit_energy():
    """
    Comprehensive explanation of energy types in circuits
    """
    explanation = """
    Energy Types in Electronic Circuits:

    1. Electrical Energy (Moving Charges):
       - Primary energy form in circuits
       - Measured in Joules (J)
       - Voltage × Current × Time
       - Present in all active circuits

    2. Thermal Energy (Heat):
       Common Sources:
       - Resistor heating (I²R losses)
       - Junction heating in semiconductors
       - Contact resistance
       - Wire resistance

    3. Magnetic Field Energy:
       Found in:
       - Inductors
       - Transformers
       - Motors/Generators
       - Formula: ½LI²

    4. Electric Field Energy:
       Stored in:
       - Capacitors
       - Insulation
       - PCB substrates
       - Formula: ½CV²

    5. Light Energy:
       Conversions in:
       - LEDs
       - Photodiodes
       - Displays
       - Optocouplers

    6. Chemical Energy:
       Present in:
       - Batteries
       - Fuel cells
       - Electrolytic capacitors
       - Chemical sensors

    7. Energy Conservation:
       - Total energy is conserved
       - Often converts to heat
       - Efficiency matters
       - Power management important

    8. Energy Storage Elements:
       a) Capacitors:
          - Store electric field energy
          - Quick discharge
          - High power density

       b) Inductors:
          - Store magnetic field energy
          - Current smoothing
          - Energy transfer

       c) Batteries:
          - Chemical energy storage
          - Long-term storage
          - High energy density
    """
    return explanation

# Generate the visualization
fig = visualize_circuit_energy()

```

``python
import numpy as np
import matplotlib.pyplot as plt

def visualize_circuit_energy():
    # Create figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # Plot 1: Energy Distribution in Common Circuits
    components = ['Resistor', 'Inductor', 'Capacitor', 'LED', 'Transistor']
    thermal = [95, 10, 5, 70, 30]  # %
    magnetic = [0, 85, 0, 0, 0]    # %
    electric = [0, 0, 90, 0, 0]    # %
    light = [0, 0, 0, 25, 0]       # %
    other = [5, 5, 5, 5, 70]       # %

    width = 0.35
    ax1.bar(components, thermal, width, label='Thermal', color='red')
    ax1.bar(components, magnetic, width, bottom=thermal, label='Magnetic', color='blue')
    ax1.bar(components, electric, width, bottom=np.array(thermal)+np.array(magnetic),
            label='Electric Field', color='yellow')
    ax1.bar(components, light, width, bottom=np.array(thermal)+np.array(magnetic)+np.array(electric),
            label='Light', color='green')
    ax1.bar(components, other, width, bottom=np.array(thermal)+np.array(magnetic)+np.array(electric)+np.array(light),
            label='Other', color='gray')

    ax1.set_ylabel('Energy Distribution (%)')
    ax1.set_title('Energy Types in Circuit Components')
    ax1.legend()

    # Plot 2: Capacitor Energy Storage
    voltage = np.linspace(0, 10, 100)
    capacitances = [1e-6, 2e-6, 5e-6]  # Farads

    for C in capacitances:
        energy = 0.5 * C * voltage2
        ax2.plot(voltage, energy * 1e6, label=f'{C*1e6}µF')

    ax2.set_xlabel('Voltage (V)')
    ax2.set_ylabel('Energy (µJ)')
    ax2.set_title('Capacitor Energy Storage')
    ax2.grid(True)
    ax2.legend()

    # Plot 3: Inductor Energy Storage
    current = np.linspace(0, 2, 100)
    inductances = [1e-3, 2e-3, 5e-3]  # Henries

    for L in inductances:
        energy = 0.5 * L * current2
        ax3.plot(current, energy * 1e3, label=f'{L*1e3}mH')

    ax3.set_xlabel('Current (A)')
    ax3.set_ylabel('Energy (mJ)')
    ax3.set_title('Inductor Energy Storage')
    ax3.grid(True)
    ax3.legend()

    # Plot 4: Heat Generation in Resistors
    time = np.linspace(0, 10, 100)
    currents = [0.1, 0.2, 0.5]  # Amperes
    R = 100  # Ohms

    for I in currents:
        power = I2 * R
        energy = power * time
        ax4.plot(time, energy, label=f'{I}A')

    ax4.set_xlabel('Time (s)')
    ax4.set_ylabel('Thermal Energy (J)')
    ax4.set_title('Resistor Heat Generation')
    ax4.grid(True)
    ax4.legend()

    plt.tight_layout()
    return fig

def explain_circuit_energy():
    """
    Comprehensive explanation of energy types in circuits
    """
    explanation = """
    Energy Types in Electronic Circuits:

    1. Electrical Energy (Moving Charges):
       - Primary energy form in circuits
       - Measured in Joules (J)
       - Voltage × Current × Time
       - Present in all active circuits

    2. Thermal Energy (Heat):
       Common Sources:
       - Resistor heating (I²R losses)
       - Junction heating in semiconductors
       - Contact resistance
       - Wire resistance

    3. Magnetic Field Energy:
       Found in:
       - Inductors
       - Transformers
       - Motors/Generators
       - Formula: ½LI²

    4. Electric Field Energy:
       Stored in:
       - Capacitors
       - Insulation
       - PCB substrates
       - Formula: ½CV²

    5. Light Energy:
       Conversions in:
       - LEDs
       - Photodiodes
       - Displays
       - Optocouplers

    6. Chemical Energy:
       Present in:
       - Batteries
       - Fuel cells
       - Electrolytic capacitors
       - Chemical sensors

    7. Energy Conservation:
       - Total energy is conserved
       - Often converts to heat
       - Efficiency matters
       - Power management important

    8. Energy Storage Elements:
       a) Capacitors:
          - Store electric field energy
          - Quick discharge
          - High power density

       b) Inductors:
          - Store magnetic field energy
          - Current smoothing
          - Energy transfer

       c) Batteries:
          - Chemical energy storage
          - Long-term storage
          - High energy density
    """
    return explanation

# Generate the visualization
fig = visualize_circuit_energy()
```
