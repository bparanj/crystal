Electric field concept with both visual demonstrations and practical examples.

import numpy as np
import matplotlib.pyplot as plt

def plot_electric_fields():
    # Create figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # Plot 1: Point Charge Electric Field Lines
    def electric_field_lines(x, y, q):
        r = np.sqrt(x2 + y2)
        Ex = q * x / (r3)
        Ey = q * y / (r3)
        return Ex, Ey

    x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
    Ex, Ey = electric_field_lines(x, y, 1)

    # Normalize vectors for better visualization
    magnitude = np.sqrt(Ex2 + Ey2)
    Ex = Ex / magnitude
    Ey = Ey / magnitude

    ax1.quiver(x, y, Ex, Ey)
    ax1.set_title('Electric Field Lines (Point Charge)')
    ax1.set_aspect('equal')
    ax1.grid(True)

    # Plot 2: Electric Field Strength vs Distance
    r = np.linspace(0.1, 5, 100)
    E = 1/(r2)  # E ∝ 1/r²

    ax2.plot(r, E, 'b-', linewidth=2)
    ax2.set_xlabel('Distance from Charge (m)')
    ax2.set_ylabel('Field Strength (N/C)')
    ax2.set_title('Electric Field Strength vs Distance')
    ax2.grid(True)

    # Plot 3: Two Opposite Charges Field Pattern
    def two_charge_field(x, y, q1, q2):
        r1 = np.sqrt((x+1)2 + y2)
        r2 = np.sqrt((x-1)2 + y2)

        Ex1 = q1 * (x+1) / (r13)
        Ey1 = q1 * y / (r13)

        Ex2 = q2 * (x-1) / (r23)
        Ey2 = q2 * y / (r23)

        return Ex1 + Ex2, Ey1 + Ey2

    x, y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))
    Ex, Ey = two_charge_field(x, y, 1, -1)

    magnitude = np.sqrt(Ex2 + Ey2)
    Ex = Ex / magnitude
    Ey = Ey / magnitude

    ax3.quiver(x, y, Ex, Ey)
    ax3.plot([-1, 1], [0, 0], 'ro')  # Show charges
    ax3.set_title('Electric Field: Opposite Charges')
    ax3.set_aspect('equal')
    ax3.grid(True)

    # Plot 4: Common Electric Field Strengths
    objects = ['Air (normal)', 'Thunder cloud', 'Near power line', 'Capacitor', 'Atom (nuclear)']
    strengths = [100, 1e5, 1e4, 1e6, 1e11]

    ax4.barh(objects, np.log10(strengths))
    ax4.set_xlabel('Log₁₀(Electric Field Strength) V/m')
    ax4.set_title('Common Electric Field Strengths')
    ax4.grid(True)

    # Add actual values on bars
    for i, strength in enumerate(strengths):
        ax4.text(np.log10(strength), i, f'{strength:0.0e} V/m', va='center')

    plt.tight_layout()
    return fig

def explain_electric_field():
    """
    Comprehensive explanation of electric fields
    """
    explanation = """
    Understanding Electric Fields:

    1. Basic Definition:
       - Force per unit charge in a region
       - Measured in Newtons/Coulomb or Volts/meter
       - Shows how charged particles would move

    2. Key Characteristics:
       a) Field Lines:
          - Start from positive charges
          - End on negative charges
          - Never cross
          - Closer lines = stronger field

       b) Field Strength:
          - Decreases with distance (1/r²)
          - Adds vectorially
          - Affected by materials
          - Proportional to charge

    3. Common Values:
       - Air (normal): ~100 V/m
       - Near power lines: ~10,000 V/m
       - Thunder clouds: ~100,000 V/m
       - Capacitors: ~1,000,000 V/m
       - Inside atoms: ~10¹¹ V/m

    4. Practical Applications:
       a) Electronic Devices:
          - Capacitors
          - Electron microscopes
          - Particle accelerators
          - Electric motors

       b) Natural Phenomena:
          - Lightning
          - Static electricity
          - Aurora borealis
          - Particle behavior

    5. Important Equations:
       - E = F/q (Force per charge)
       - E = k*Q/r² (Point charge field)
       - E = V/d (Uniform field)

    6. Shielding and Materials:
       - Conductors shield internal fields
       - Dielectrics reduce field strength
       - Some materials enhance fields
       - Grounding affects field patterns
    """
    return explanation

# Generate the visualization
fig = plot_electric_fields()

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_electric_fields():
    # Create figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # Plot 1: Point Charge Electric Field Lines
    def electric_field_lines(x, y, q):
        r = np.sqrt(x2 + y2)
        Ex = q * x / (r3)
        Ey = q * y / (r3)
        return Ex, Ey

    x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
    Ex, Ey = electric_field_lines(x, y, 1)

    # Normalize vectors for better visualization
    magnitude = np.sqrt(Ex2 + Ey2)
    Ex = Ex / magnitude
    Ey = Ey / magnitude

    ax1.quiver(x, y, Ex, Ey)
    ax1.set_title('Electric Field Lines (Point Charge)')
    ax1.set_aspect('equal')
    ax1.grid(True)

    # Plot 2: Electric Field Strength vs Distance
    r = np.linspace(0.1, 5, 100)
    E = 1/(r2)  # E ∝ 1/r²

    ax2.plot(r, E, 'b-', linewidth=2)
    ax2.set_xlabel('Distance from Charge (m)')
    ax2.set_ylabel('Field Strength (N/C)')
    ax2.set_title('Electric Field Strength vs Distance')
    ax2.grid(True)

    # Plot 3: Two Opposite Charges Field Pattern
    def two_charge_field(x, y, q1, q2):
        r1 = np.sqrt((x+1)2 + y2)
        r2 = np.sqrt((x-1)2 + y2)

        Ex1 = q1 * (x+1) / (r13)
        Ey1 = q1 * y / (r13)

        Ex2 = q2 * (x-1) / (r23)
        Ey2 = q2 * y / (r23)

        return Ex1 + Ex2, Ey1 + Ey2

    x, y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))
    Ex, Ey = two_charge_field(x, y, 1, -1)

    magnitude = np.sqrt(Ex2 + Ey2)
    Ex = Ex / magnitude
    Ey = Ey / magnitude

    ax3.quiver(x, y, Ex, Ey)
    ax3.plot([-1, 1], [0, 0], 'ro')  # Show charges
    ax3.set_title('Electric Field: Opposite Charges')
    ax3.set_aspect('equal')
    ax3.grid(True)

    # Plot 4: Common Electric Field Strengths
    objects = ['Air (normal)', 'Thunder cloud', 'Near power line', 'Capacitor', 'Atom (nuclear)']
    strengths = [100, 1e5, 1e4, 1e6, 1e11]

    ax4.barh(objects, np.log10(strengths))
    ax4.set_xlabel('Log₁₀(Electric Field Strength) V/m')
    ax4.set_title('Common Electric Field Strengths')
    ax4.grid(True)

    # Add actual values on bars
    for i, strength in enumerate(strengths):
        ax4.text(np.log10(strength), i, f'{strength:0.0e} V/m', va='center')

    plt.tight_layout()
    return fig

def explain_electric_field():
    """
    Comprehensive explanation of electric fields
    """
    explanation = """
    Understanding Electric Fields:

    1. Basic Definition:
       - Force per unit charge in a region
       - Measured in Newtons/Coulomb or Volts/meter
       - Shows how charged particles would move

    2. Key Characteristics:
       a) Field Lines:
          - Start from positive charges
          - End on negative charges
          - Never cross
          - Closer lines = stronger field

       b) Field Strength:
          - Decreases with distance (1/r²)
          - Adds vectorially
          - Affected by materials
          - Proportional to charge

    3. Common Values:
       - Air (normal): ~100 V/m
       - Near power lines: ~10,000 V/m
       - Thunder clouds: ~100,000 V/m
       - Capacitors: ~1,000,000 V/m
       - Inside atoms: ~10¹¹ V/m

    4. Practical Applications:
       a) Electronic Devices:
          - Capacitors
          - Electron microscopes
          - Particle accelerators
          - Electric motors

       b) Natural Phenomena:
          - Lightning
          - Static electricity
          - Aurora borealis
          - Particle behavior

    5. Important Equations:
       - E = F/q (Force per charge)
       - E = k*Q/r² (Point charge field)
       - E = V/d (Uniform field)

    6. Shielding and Materials:
       - Conductors shield internal fields
       - Dielectrics reduce field strength
       - Some materials enhance fields
       - Grounding affects field patterns
    """
    return explanation

# Generate the visualization
fig = plot_electric_fields()

```

