The traditional Northbridge and Southbridge architecture is no longer found in modern motherboards.

### Traditional Architecture

**Northbridge**:
- Handled communication between the CPU, RAM, and GPU (AGP/PCIe).
- Managed high-speed interfaces such as the memory controller and the graphics interface.

**Southbridge**:
- Managed lower-speed peripheral interfaces such as SATA, USB, Ethernet, audio, and BIOS.

### Evolution to Modern Architectures

**Integrated Memory Controller**:
- Modern CPUs have integrated the memory controller, which was traditionally part of the Northbridge, directly into the CPU die. This reduces latency and increases performance.

**Platform Controller Hub (PCH)**:
- Intel introduced the Platform Controller Hub (PCH) architecture, which consolidates the functions of the Northbridge and Southbridge into a single chip.
- The PCH connects directly to the CPU via a high-speed interface like DMI (Direct Media Interface).

### AMD Architecture

**Fusion Controllers**:
- AMD has also integrated many functions traditionally managed by the Northbridge into their CPUs, with their APU (Accelerated Processing Unit) line.
- AMD uses a similar architecture with a single chipset that connects to the CPU, referred to as the FCH (Fusion Controller Hub).

### Modern Motherboard Layout

1. **CPU**:
   - Integrates the memory controller, PCIe lanes for graphics and storage, and sometimes even integrated graphics.
2. **Chipset (PCH/FCH)**:
   - Handles additional I/O functions such as USB, SATA, Ethernet, and sometimes additional PCIe lanes.

### Summary

The traditional Northbridge and Southbridge architecture has been replaced by integrated memory controllers within the CPU and a consolidated chipset (PCH/FCH). This change enhances performance and simplifies motherboard design, reflecting the shift towards more efficient and high-performance computing architectures.
