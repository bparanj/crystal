The traditional north bridge and south bridge architecture is largely obsolete in modern motherboards. However, the concepts have evolved:

1. North Bridge:
   - Functions mostly integrated into the CPU itself
   - Handles high-speed communications (RAM, PCIe lanes for graphics)

2. South Bridge:
   - Evolved into what's now called the Platform Controller Hub (PCH)
   - Manages lower-speed connections (USB, SATA, audio, etc.)

Modern systems use a more integrated approach:

- CPU directly handles memory and PCIe lanes
- PCH handles most I/O functions
- Direct communication between CPU and PCH via DMI (Direct Media Interface)

This integration has several benefits:
- Reduced latency
- Improved power efficiency
- Simplified motherboard design

While the terms "north bridge" and "south bridge" are still sometimes used colloquially, they don't accurately describe the architecture of current motherboards.

No, the traditional Northbridge and Southbridge architecture is no longer  found in modern motherboards. This shift has occurred due to advancements in CPU and chipset design. Here's a more detailed explanation:

### Traditional Architecture

**Northbridge**:
- Managed communication between the CPU, RAM, and GPU.
- Handled high-speed interfaces such as the memory controller and the graphics interface (AGP/PCIe).

**Southbridge**:
- Managed lower-speed peripheral interfaces such as SATA, USB, Ethernet, audio, and BIOS.

### Modern Architecture

**Integrated Memory Controller**:
- Modern CPUs, particularly those from Intel and AMD, have integrated the memory controller and often the graphics controller directly into the CPU die. This reduces latency and increases performance.

**Platform Controller Hub (PCH)**:
- Intel introduced the Platform Controller Hub (PCH) architecture, which consolidates the functions of the Northbridge and Southbridge into a single chip.
- The PCH connects directly to the CPU via a high-speed interface such as DMI (Direct Media Interface).

### AMD's Equivalent

**AMD Fusion and Infinity Fabric**:
- AMD's modern architectures integrate many Northbridge functions into the CPU as well. Their Ryzen and EPYC processors, for example, use Infinity Fabric to interconnect various components on the die,  memory controllers and PCIe lanes.
- AMD also uses a similar single-chip solution for other functions, known as the chipset, which connects to the CPU.

### Benefits of the Modern Architecture

1. **Improved Performance**:
   - Lower latency due to direct integration of memory and graphics controllers into the CPU.
   - Faster communication between CPU and peripherals through high-speed interfaces.

2. **Reduced Complexity**:
   - Simplifies motherboard design by reducing the number of separate chips.
   - Lowers power consumption and increases efficiency.

3. **Enhanced Features**:
   - Allows for more sophisticated power management and thermal control.
   - Supports higher-speed interfaces and more advanced connectivity options.

### Summary

The traditional Northbridge and Southbridge have been replaced by integrated solutions in modern CPUs and a single chipset (like Intel's PCH or AMD's chipset) that handles the remaining I/O functions. This evolution enhances performance, reduces latency, and simplifies motherboard design.
