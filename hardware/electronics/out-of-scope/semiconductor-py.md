Let me explain where semiconductors fit in the conductivity spectrum with both an explanation and visual comparison.

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_conductivity_spectrum():
    # Create figure with multiple plots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))

    # Plot 1: Conductivity Spectrum
    materials = ['Silver', 'Copper', 'Silicon\n(doped)', 'Silicon\n(pure)', 'Glass', 'Rubber']
    conductivity = [6.3e7, 5.96e7, 1e2, 1e-3, 1e-10, 1e-15]

    ax1.barh(materials, np.log10(conductivity))
    ax1.set_xlabel('Log₁₀(Conductivity) S/m')
    ax1.set_title('Conductivity Spectrum of Materials')
    ax1.axvline(x=0, color='r', linestyle='--', alpha=0.5)
    ax1.grid(True)

    # Add regions
    ax1.axvspan(5, 8, alpha=0.2, color='green', label='Conductors')
    ax1.axvspan(-5, 5, alpha=0.2, color='yellow', label='Semiconductors')
    ax1.axvspan(-15, -5, alpha=0.2, color='red', label='Insulators')
    ax1.legend()

    # Plot 2: Band Gap Comparison
    materials_bg = ['Copper', 'Silicon', 'Germanium', 'GaAs', 'Diamond']
    band_gaps = [0, 1.1, 0.67, 1.43, 5.5]  # in eV

    ax2.bar(materials_bg, band_gaps, color=['gold', 'blue', 'green', 'red', 'gray'])
    ax2.set_ylabel('Band Gap (eV)')
    ax2.set_title('Band Gap Energy of Different Materials')
    ax2.grid(True)

    # Plot 3: Temperature Effect on Conductivity
    temp = np.linspace(250, 400, 100)

    # Simplified conductivity models
    conductor = np.ones_like(temp)  5 - (temp - 300)  0.01  # Decreases with temperature
    semiconductor = np.exp(-(1/(0.026  temp/300)))  # Increases with temperature

    ax3.plot(temp, conductor/conductor[0], 'g-', label='Conductor', linewidth=2)
    ax3.plot(temp, semiconductor/semiconductor[0], 'r-', label='Semiconductor', linewidth=2)
    ax3.set_xlabel('Temperature (K)')
    ax3.set_ylabel('Normalized Conductivity')
    ax3.set_title('Temperature Effect on Conductivity')
    ax3.grid(True)
    ax3.legend()

    plt.tight_layout()
    return fig

def explain_semiconductor_properties():
    """
    Detailed explanation of semiconductor properties
    """
    properties = """
    Semiconductor Position in Conductivity Spectrum:

    1. Conductivity Range:
       Conductors: >10⁴ S/m
       Semiconductors: 10⁻⁶ to 10⁴ S/m
       Insulators: <10⁻⁶ S/m

    2. Band Gap Characteristics:
       - Conductors: No band gap or overlapping bands
       - Semiconductors: Small band gap (0.1 to 4 eV)
       - Insulators: Large band gap (>4 eV)

    3. Unique Properties:
       a) Temperature Effect:
          - Conductivity increases with temperature
          - Opposite to metals
          - Exponential relationship

       b) Doping Effects:
          - Can be modified by adding impurities
          - Controllable conductivity
          - Creates p-type or n-type

       c) Light Sensitivity:
          - Can generate electron-hole pairs
          - Photovoltaic effect
          - Photoconductive effect

    4. Advantages of Middle Position:
       - Controllable conductivity
       - Temperature sensitivity
       - Light sensitivity
       - Switching capability
       - Amplification possible
    """
    return properties

# Generate the plots
fig = plot_conductivity_spectrum()

```
import numpy as np
import matplotlib.pyplot as plt

def plot_conductivity_spectrum():
    # Create figure with multiple plots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))

    # Plot 1: Conductivity Spectrum
    materials = ['Silver', 'Copper', 'Silicon\n(doped)', 'Silicon\n(pure)', 'Glass', 'Rubber']
    conductivity = [6.3e7, 5.96e7, 1e2, 1e-3, 1e-10, 1e-15]

    ax1.barh(materials, np.log10(conductivity))
    ax1.set_xlabel('Log₁₀(Conductivity) S/m')
    ax1.set_title('Conductivity Spectrum of Materials')
    ax1.axvline(x=0, color='r', linestyle='--', alpha=0.5)
    ax1.grid(True)

    # Add regions
    ax1.axvspan(5, 8, alpha=0.2, color='green', label='Conductors')
    ax1.axvspan(-5, 5, alpha=0.2, color='yellow', label='Semiconductors')
    ax1.axvspan(-15, -5, alpha=0.2, color='red', label='Insulators')
    ax1.legend()

    # Plot 2: Band Gap Comparison
    materials_bg = ['Copper', 'Silicon', 'Germanium', 'GaAs', 'Diamond']
    band_gaps = [0, 1.1, 0.67, 1.43, 5.5]  # in eV

    ax2.bar(materials_bg, band_gaps, color=['gold', 'blue', 'green', 'red', 'gray'])
    ax2.set_ylabel('Band Gap (eV)')
    ax2.set_title('Band Gap Energy of Different Materials')
    ax2.grid(True)

    # Plot 3: Temperature Effect on Conductivity
    temp = np.linspace(250, 400, 100)

    # Simplified conductivity models
    conductor = np.ones_like(temp)  5 - (temp - 300)  0.01  # Decreases with temperature
    semiconductor = np.exp(-(1/(0.026  temp/300)))  # Increases with temperature

    ax3.plot(temp, conductor/conductor[0], 'g-', label='Conductor', linewidth=2)
    ax3.plot(temp, semiconductor/semiconductor[0], 'r-', label='Semiconductor', linewidth=2)
    ax3.set_xlabel('Temperature (K)')
    ax3.set_ylabel('Normalized Conductivity')
    ax3.set_title('Temperature Effect on Conductivity')
    ax3.grid(True)
    ax3.legend()

    plt.tight_layout()
    return fig

def explain_semiconductor_properties():
    """
    Detailed explanation of semiconductor properties
    """
    properties = """
    Semiconductor Position in Conductivity Spectrum:

    1. Conductivity Range:
       Conductors: >10⁴ S/m
       Semiconductors: 10⁻⁶ to 10⁴ S/m
       Insulators: <10⁻⁶ S/m

    2. Band Gap Characteristics:
       - Conductors: No band gap or overlapping bands
       - Semiconductors: Small band gap (0.1 to 4 eV)
       - Insulators: Large band gap (>4 eV)

    3. Unique Properties:
       a) Temperature Effect:
          - Conductivity increases with temperature
          - Opposite to metals
          - Exponential relationship

       b) Doping Effects:
          - Can be modified by adding impurities
          - Controllable conductivity
          - Creates p-type or n-type

       c) Light Sensitivity:
          - Can generate electron-hole pairs
          - Photovoltaic effect
          - Photoconductive effect

    4. Advantages of Middle Position:
       - Controllable conductivity
       - Temperature sensitivity
       - Light sensitivity
       - Switching capability
       - Amplification possible
    """
    return properties

# Generate the plots
fig = plot_conductivity_spectrum()
