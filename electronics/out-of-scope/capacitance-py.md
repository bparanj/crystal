Explanation and a visualization that demonstrates capacitive reactance.

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_reactance(frequency, capacitance=1e-6):
    """
    Calculate capacitive reactance for given frequencies
    Xc = 1/(2πfC)
    """
    return 1 / (2 * np.pi * frequency * capacitance)

def simulate_capacitor_response(input_signal, frequency, dt, capacitance=1e-6):
    """
    Simulate capacitor's response to input signal
    """
    t = np.arange(0, len(input_signal)) * dt
    # Calculate phase shift and attenuation
    Xc = calculate_reactance(frequency, capacitance)
    Z = Xc  # Assuming purely capacitive circuit
    phase_shift = -np.pi/2  # Capacitor current leads voltage by 90°
    attenuation = 1 / np.sqrt(1 + (Xc/1000)2)  # Assuming 1kΩ reference
    
    output_signal = attenuation * input_signal * np.exp(1j * phase_shift)
    return t, np.real(output_signal)

def plot_frequency_response():
    # Create figure with multiple subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
    
    # Plot 1: Capacitive Reactance vs Frequency
    f = np.logspace(0, 5, 1000)  # 1 Hz to 100 kHz
    Xc = calculate_reactance(f)
    
    ax1.loglog(f, Xc, 'b-', linewidth=2)
    ax1.grid(True)
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Reactance (Ω)')
    ax1.set_title('Capacitive Reactance vs Frequency')
    
    # Plot 2: Signal Comparison - Low Frequency (100 Hz)
    dt = 1e-5
    t_low = np.arange(0, 0.03, dt)
    low_freq = 100  # Hz
    input_signal_low = np.sin(2 * np.pi * low_freq * t_low)
    _, output_signal_low = simulate_capacitor_response(input_signal_low, low_freq, dt)
    
    ax2.plot(t_low * 1000, input_signal_low, 'b-', label='Input Signal', linewidth=2)
    ax2.plot(t_low * 1000, output_signal_low, 'r--', label='Output Signal', linewidth=2)
    ax2.set_xlabel('Time (ms)')
    ax2.set_ylabel('Amplitude')
    ax2.set_title(f'Low Frequency Response ({low_freq} Hz)')
    ax2.grid(True)
    ax2.legend()
    
    # Plot 3: Signal Comparison - High Frequency (10 kHz)
    t_high = np.arange(0, 0.001, dt)
    high_freq = 10000  # Hz
    input_signal_high = np.sin(2 * np.pi * high_freq * t_high)
    _, output_signal_high = simulate_capacitor_response(input_signal_high, high_freq, dt)
    
    ax3.plot(t_high * 1000, input_signal_high, 'b-', label='Input Signal', linewidth=2)
    ax3.plot(t_high * 1000, output_signal_high, 'r--', label='Output Signal', linewidth=2)
    ax3.set_xlabel('Time (ms)')
    ax3.set_ylabel('Amplitude')
    ax3.set_title(f'High Frequency Response ({high_freq} Hz)')
    ax3.grid(True)
    ax3.legend()
    
    plt.tight_layout()
    return fig

# Generate the plots
fig = plot_frequency_response()

```

Let me explain why high-frequency signals pass through capacitors more easily:

1. Capacitive Reactance (Xc):
   - The opposition to current flow through a capacitor is called capacitive reactance
   - It's given by the formula: Xc = 1/(2πfC)
   - As frequency (f) increases, reactance (Xc) decreases
   - This means less opposition to current flow at higher frequencies

2. Physical Explanation:
   - Capacitors store charge on parallel plates
   - At low frequencies:
     * The plates have time to fully charge
     * This creates a strong opposing voltage
     * Results in less current flow
   - At high frequencies:
     * The plates don't have time to fully charge
     * Less opposing voltage develops
     * More current can flow through

3. Practical Effects:
   - For DC (f = 0): Infinite reactance, no current flows
   - For very high frequencies: Near-zero reactance, current flows easily
   - Creates a high-pass filter effect
   - Used in crossover networks, coupling circuits, and filters

4. The simulation shows:
   - The inverse relationship between frequency and reactance
   - How low-frequency signals are attenuated more
   - How high-frequency signals pass through with less attenuation
   - The 90-degree phase shift between voltage and current

This behavior makes capacitors useful for:
- Blocking DC while passing AC
- Creating frequency filters
- Coupling between circuit stages
- Signal timing and phase shifting

Would you like me to:
1. Explain any aspect in more detail?
2. Show how different capacitor values affect the frequency response?
3. Demonstrate specific applications of this behavior?

import numpy as np
import matplotlib.pyplot as plt

def calculate_reactance(frequency, capacitance=1e-6):
    """
    Calculate capacitive reactance for given frequencies
    Xc = 1/(2πfC)
    """
    return 1 / (2 * np.pi * frequency * capacitance)

def simulate_capacitor_response(input_signal, frequency, dt, capacitance=1e-6):
    """
    Simulate capacitor's response to input signal
    """
    t = np.arange(0, len(input_signal)) * dt
    # Calculate phase shift and attenuation
    Xc = calculate_reactance(frequency, capacitance)
    Z = Xc  # Assuming purely capacitive circuit
    phase_shift = -np.pi/2  # Capacitor current leads voltage by 90°
    attenuation = 1 / np.sqrt(1 + (Xc/1000)2)  # Assuming 1kΩ reference
    
    output_signal = attenuation * input_signal * np.exp(1j * phase_shift)
    return t, np.real(output_signal)

def plot_frequency_response():
    # Create figure with multiple subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
    
    # Plot 1: Capacitive Reactance vs Frequency
    f = np.logspace(0, 5, 1000)  # 1 Hz to 100 kHz
    Xc = calculate_reactance(f)
    
    ax1.loglog(f, Xc, 'b-', linewidth=2)
    ax1.grid(True)
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Reactance (Ω)')
    ax1.set_title('Capacitive Reactance vs Frequency')
    
    # Plot 2: Signal Comparison - Low Frequency (100 Hz)
    dt = 1e-5
    t_low = np.arange(0, 0.03, dt)
    low_freq = 100  # Hz
    input_signal_low = np.sin(2 * np.pi * low_freq * t_low)
    _, output_signal_low = simulate_capacitor_response(input_signal_low, low_freq, dt)
    
    ax2.plot(t_low * 1000, input_signal_low, 'b-', label='Input Signal', linewidth=2)
    ax2.plot(t_low * 1000, output_signal_low, 'r--', label='Output Signal', linewidth=2)
    ax2.set_xlabel('Time (ms)')
    ax2.set_ylabel('Amplitude')
    ax2.set_title(f'Low Frequency Response ({low_freq} Hz)')
    ax2.grid(True)
    ax2.legend()
    
    # Plot 3: Signal Comparison - High Frequency (10 kHz)
    t_high = np.arange(0, 0.001, dt)
    high_freq = 10000  # Hz
    input_signal_high = np.sin(2 * np.pi * high_freq * t_high)
    _, output_signal_high = simulate_capacitor_response(input_signal_high, high_freq, dt)
    
    ax3.plot(t_high * 1000, input_signal_high, 'b-', label='Input Signal', linewidth=2)
    ax3.plot(t_high * 1000, output_signal_high, 'r--', label='Output Signal', linewidth=2)
    ax3.set_xlabel('Time (ms)')
    ax3.set_ylabel('Amplitude')
    ax3.set_title(f'High Frequency Response ({high_freq} Hz)')
    ax3.grid(True)
    ax3.legend()
    
    plt.tight_layout()
    return fig

# Generate the plots
fig = plot_frequency_response()