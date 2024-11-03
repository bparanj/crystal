Electrical energy explanation with visual demonstrations.

```python
import numpy as np
import matplotlib.pyplot as plt

def visualize_electrical_energy():
    # Create figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Common Household Energy Usage
    devices = ['LED Bulb', 'Phone Charger', 'Laptop', 'Microwave', 'AC Unit']
    power = [10, 5, 65, 1100, 3500]  # Watts
    daily_hours = [5, 3, 4, 0.5, 6]  # Hours per day
    
    daily_energy = np.array(power) * np.array(daily_hours) / 1000  # kWh
    
    ax1.bar(devices, daily_energy, color=['yellow', 'green', 'blue', 'orange', 'red'])
    ax1.set_ylabel('Daily Energy Usage (kWh)')
    ax1.set_title('Daily Electrical Energy Consumption')
    ax1.grid(True)
    
    # Add values on bars
    for i, e in enumerate(daily_energy):
        ax1.text(i, e, f'{e:.2f} kWh', ha='center', va='bottom')
    
    # Plot 2: Energy Cost Over Time
    hours = np.linspace(0, 24, 100)
    rates = [0.10, 0.15, 0.20]  # Cost per kWh
    power_usage = 2  # kW constant usage
    
    for rate in rates:
        cost = hours * power_usage * rate
        ax2.plot(hours, cost, label=f'${rate}/kWh')
    
    ax2.set_xlabel('Hours')
    ax2.set_ylabel('Cost ($)')
    ax2.set_title('Energy Cost Over Time')
    ax2.grid(True)
    ax2.legend()
    
    # Plot 3: Power to Energy Conversion
    time = np.linspace(0, 10, 100)
    powers = [100, 200, 500]  # Watts
    
    for p in powers:
        energy = p * time / 3600  # Convert to Wh
        ax3.plot(time, energy, label=f'{p}W')
    
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('Energy (Wh)')
    ax3.set_title('Energy Accumulation Over Time')
    ax3.grid(True)
    ax3.legend()
    
    # Plot 4: Energy Efficiency Comparison
    devices = ['Incandescent', 'CFL', 'LED', 'Solar Panel', 'Electric Motor']
    efficiency = [5, 20, 90, 20, 85]  # percentage
    
    ax4.barh(devices, efficiency, color=['red', 'yellow', 'green', 'blue', 'orange'])
    ax4.set_xlabel('Efficiency (%)')
    ax4.set_title('Energy Conversion Efficiency')
    ax4.grid(True)
    
    # Add efficiency values on bars
    for i, eff in enumerate(efficiency):
        ax4.text(eff, i, f'{eff}%', va='center')
    
    plt.tight_layout()
    return fig

def explain_electrical_energy():
    """
    Comprehensive explanation of electrical energy
    """
    explanation = """
    Understanding Electrical Energy:

    1. Basic Definition:
       - Energy carried by moving electrons
       - Measured in Joules (J) or kilowatt-hours (kWh)
       - 1 kWh = 3,600,000 Joules
       - Power × Time = Energy
       
    2. Common Units:
       a) Small Scale:
          - Watt-hour (Wh)
          - Joule (J)
          - Electron-volt (eV)
          
       b) Large Scale:
          - Kilowatt-hour (kWh)
          - Megawatt-hour (MWh)
          - Gigawatt-hour (GWh)
          
    3. Typical Consumption:
       Daily Usage:
       - LED bulb: 0.05 kWh
       - Smartphone: 0.015 kWh
       - Laptop: 0.26 kWh
       - AC unit: 21 kWh
       - Home: 30 kWh
       
    4. Energy Conversion:
       Input → Output:
       - Chemical → Electrical (Batteries)
       - Mechanical → Electrical (Generators)
       - Light → Electrical (Solar)
       - Heat → Electrical (Thermoelectric)
       
    5. Efficiency Examples:
       - LED lights: ~90%
       - Solar panels: ~20%
       - Electric motors: ~85%
       - Phone charger: ~80%
       
    6. Cost Calculations:
       - Cost = Energy × Rate
       - Energy = Power × Time
       - Common rate: $0.12/kWh
       - Monthly bill = Daily usage × 30 × Rate
       
    7. Energy Saving Tips:
       - Use efficient appliances
       - Turn off unused devices
       - Optimize usage times
       - Regular maintenance
    """
    return explanation

# Generate the visualization
fig = visualize_electrical_energy()

```

Electrical energy in simple terms:

1. Basic Concept:
   - Energy carried by electric current
   - Like water carrying energy in a pipe
   - Measured in kilowatt-hours (kWh)
   - Power × Time = Energy

2. Common Examples:
   Daily Usage:
   - LED bulb: 0.05 kWh/day
   - Phone charging: 0.015 kWh/day
   - Laptop: 0.26 kWh/day
   - Air conditioner: 21 kWh/day

3. Understanding Units:
   - Watt (W): Rate of energy use
   - Kilowatt (kW): 1000 watts
   - Kilowatt-hour (kWh): Energy used by 1kW for 1 hour
   - Example: 100W bulb for 10 hours = 1 kWh

4. Energy Conversion:
   From Other Forms:
   - Chemical (batteries)
   - Mechanical (generators)
   - Light (solar panels)
   - Heat (thermoelectric)

5. Efficiency Levels:
   - LED lights: ~90%
   - Solar panels: ~20%
   - Electric motors: ~85%
   - Phone chargers: ~80%

6. Practical Applications:
   - Powering devices
   - Heating/cooling
   - Lighting
   - Transportation

Would you like me to:
1. Explain energy calculations?
2. Show more about energy efficiency?
3. Demonstrate cost calculations?

```python
import numpy as np
import matplotlib.pyplot as plt

def visualize_electrical_energy():
    # Create figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Common Household Energy Usage
    devices = ['LED Bulb', 'Phone Charger', 'Laptop', 'Microwave', 'AC Unit']
    power = [10, 5, 65, 1100, 3500]  # Watts
    daily_hours = [5, 3, 4, 0.5, 6]  # Hours per day
    
    daily_energy = np.array(power) * np.array(daily_hours) / 1000  # kWh
    
    ax1.bar(devices, daily_energy, color=['yellow', 'green', 'blue', 'orange', 'red'])
    ax1.set_ylabel('Daily Energy Usage (kWh)')
    ax1.set_title('Daily Electrical Energy Consumption')
    ax1.grid(True)
    
    # Add values on bars
    for i, e in enumerate(daily_energy):
        ax1.text(i, e, f'{e:.2f} kWh', ha='center', va='bottom')
    
    # Plot 2: Energy Cost Over Time
    hours = np.linspace(0, 24, 100)
    rates = [0.10, 0.15, 0.20]  # Cost per kWh
    power_usage = 2  # kW constant usage
    
    for rate in rates:
        cost = hours * power_usage * rate
        ax2.plot(hours, cost, label=f'${rate}/kWh')
    
    ax2.set_xlabel('Hours')
    ax2.set_ylabel('Cost ($)')
    ax2.set_title('Energy Cost Over Time')
    ax2.grid(True)
    ax2.legend()
    
    # Plot 3: Power to Energy Conversion
    time = np.linspace(0, 10, 100)
    powers = [100, 200, 500]  # Watts
    
    for p in powers:
        energy = p * time / 3600  # Convert to Wh
        ax3.plot(time, energy, label=f'{p}W')
    
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('Energy (Wh)')
    ax3.set_title('Energy Accumulation Over Time')
    ax3.grid(True)
    ax3.legend()
    
    # Plot 4: Energy Efficiency Comparison
    devices = ['Incandescent', 'CFL', 'LED', 'Solar Panel', 'Electric Motor']
    efficiency = [5, 20, 90, 20, 85]  # percentage
    
    ax4.barh(devices, efficiency, color=['red', 'yellow', 'green', 'blue', 'orange'])
    ax4.set_xlabel('Efficiency (%)')
    ax4.set_title('Energy Conversion Efficiency')
    ax4.grid(True)
    
    # Add efficiency values on bars
    for i, eff in enumerate(efficiency):
        ax4.text(eff, i, f'{eff}%', va='center')
    
    plt.tight_layout()
    return fig

def explain_electrical_energy():
    """
    Comprehensive explanation of electrical energy
    """
    explanation = """
    Understanding Electrical Energy:

    1. Basic Definition:
       - Energy carried by moving electrons
       - Measured in Joules (J) or kilowatt-hours (kWh)
       - 1 kWh = 3,600,000 Joules
       - Power × Time = Energy
       
    2. Common Units:
       a) Small Scale:
          - Watt-hour (Wh)
          - Joule (J)
          - Electron-volt (eV)
          
       b) Large Scale:
          - Kilowatt-hour (kWh)
          - Megawatt-hour (MWh)
          - Gigawatt-hour (GWh)
          
    3. Typical Consumption:
       Daily Usage:
       - LED bulb: 0.05 kWh
       - Smartphone: 0.015 kWh
       - Laptop: 0.26 kWh
       - AC unit: 21 kWh
       - Home: 30 kWh
       
    4. Energy Conversion:
       Input → Output:
       - Chemical → Electrical (Batteries)
       - Mechanical → Electrical (Generators)
       - Light → Electrical (Solar)
       - Heat → Electrical (Thermoelectric)
       
    5. Efficiency Examples:
       - LED lights: ~90%
       - Solar panels: ~20%
       - Electric motors: ~85%
       - Phone charger: ~80%
       
    6. Cost Calculations:
       - Cost = Energy × Rate
       - Energy = Power × Time
       - Common rate: $0.12/kWh
       - Monthly bill = Daily usage × 30 × Rate
       
    7. Energy Saving Tips:
       - Use efficient appliances
       - Turn off unused devices
       - Optimize usage times
       - Regular maintenance
    """
    return explanation

# Generate the visualization
fig = visualize_electrical_energy()
```
