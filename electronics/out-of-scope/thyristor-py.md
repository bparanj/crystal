Problems that thyristors solve and demonstrate their unique characteristics.

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_thyristor_response(voltage, gate_trigger=0.7, holding_current=0.1):
    """
    Simulate thyristor I-V characteristics with gate triggering
    """
    current = np.zeros_like(voltage)
    state_on = False
    
    for i, v in enumerate(voltage):
        if state_on:
            # Once triggered, conducts until current falls below holding current
            if abs(v) < holding_current:
                state_on = False
                current[i] = 0
            else:
                current[i] = v / 0.1  # Low on-state resistance
        else:
            # Check for trigger conditions
            if abs(v) > gate_trigger:
                state_on = True
                current[i] = v / 0.1
            else:
                current[i] = 0

    return current

def plot_characteristics():
    # Create voltage array for one complete cycle
    voltage = np.linspace(-2, 2, 1000)
    
    # Simulate different gate trigger voltages
    current_no_gate = np.zeros_like(voltage)  # No gate trigger
    current_gate1 = simulate_thyristor_response(voltage, gate_trigger=1.0)
    current_gate2 = simulate_thyristor_response(voltage, gate_trigger=0.5)
    
    # Create figure with multiple subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: I-V Characteristics
    ax1.plot(voltage, current_no_gate, 'b--', label='No Gate Trigger', linewidth=2)
    ax1.plot(voltage, current_gate1, 'r-', label='Gate Trigger = 1.0V', linewidth=2)
    ax1.plot(voltage, current_gate2, 'g-', label='Gate Trigger = 0.5V', linewidth=2)
    ax1.set_xlabel('Voltage (V)')
    ax1.set_ylabel('Current (A)')
    ax1.set_title('Thyristor I-V Characteristics with Different Gate Triggers')
    ax1.grid(True)
    ax1.legend()
    
    # Plot 2: Time Domain Response
    time = np.linspace(0, 2*np.pi, 1000)
    input_voltage = 2 * np.sin(time)
    output_current = simulate_thyristor_response(input_voltage, gate_trigger=0.7)
    
    ax2.plot(time, input_voltage, 'b-', label='Input Voltage', linewidth=2)
    ax2.plot(time, output_current, 'r-', label='Output Current', linewidth=2)
    ax2.set_xlabel('Time (radians)')
    ax2.set_ylabel('Voltage/Current')
    ax2.set_title('Thyristor Response to AC Input')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    return fig

def list_applications():
    """
    List common thyristor applications and benefits
    """
    applications = """
    Key Problems Solved by Thyristors:

    1. Power Control Problems:
       - High-power switching with low control power
       - Precise phase-angle control in AC circuits
       - Efficient power regulation
       - Protection against voltage surges

    2. Circuit Limitations:
       - Overcomes limitations of simple transistors/diodes
       - Provides latching behavior
       - Handles high voltage and current
       - Offers controlled turn-on timing

    3. Industrial Applications:
       - Motor speed control
       - Light dimming
       - Power supply control
       - Soft starting of motors
       - Induction heating
       - UPS systems

    4. Advantages:
       - High power handling capability
       - Low forward voltage drop
       - High surge current capability
       - Simple gate control
       - Latching behavior
       - No continuous gate signal needed

    5. Unique Features:
       - Bidirectional control (in TRIACs)
       - Self-latching operation
       - High blocking voltage
       - Temperature stability
       - Robust construction
    """
    return applications

# Generate plots
fig = plot_characteristics()

```
