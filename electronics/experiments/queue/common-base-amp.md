The idea that a common-base amplifier is a "reversed" common-collector amplifier (emitter follower) stems from their symmetrical operation but opposite roles in signal handling. Here’s how we resolve this apparent paradox:

---

### Key Characteristics of Each Configuration

#### Common-Base Amplifier (CBA):
- Input: Applied to the emitter.
- Output: Taken from the collector.
- Base: Held at a constant voltage (hence "common").
- Key Features:
  - Low input impedance: The emitter directly receives the input signal, and the base-emitter junction is forward-biased, presenting a very low impedance.
  - High output impedance: The collector circuit provides high impedance, allowing for significant voltage gain.
  - Voltage Amplifier: It amplifies the input voltage with high bandwidth.

#### Common-Collector Amplifier (CCA or Emitter Follower):
- Input: Applied to the base.
- Output: Taken from the emitter.
- Collector: Connected to the supply (hence "common").
- Key Features:
  - High input impedance: The base-emitter junction is the primary input, presenting high impedance to the source.
  - Low output impedance: The emitter directly drives the load, providing a low-impedance output.
  - Current Amplifier: It amplifies current while maintaining unity voltage gain.

---

### How They Are Opposite Yet Symmetrical

1. Signal Path:
   - In a common-base amplifier, the signal flows from the emitter to the collector, with the base acting as a fixed reference.
   - In a common-collector amplifier, the signal flows from the base to the emitter, with the collector acting as a fixed reference.

2. Impedance Transformation:
   - The CBA transforms a low input impedance at the emitter into a high output impedance at the collector.
   - The CCA transforms a high input impedance at the base into a low output impedance at the emitter.

3. Primary Function:
   - The CBA focuses on voltage amplification, taking a small voltage input and producing a larger voltage swing at the output.
   - The CCA focuses on buffering and current amplification, providing a low-impedance output that can drive loads without significant voltage gain.

4. Bandwidth Behavior:
   - The CBA has inherently high bandwidth due to the low impedance at its input.
   - The CCA has limited bandwidth because of the high input impedance and capacitance at the base.

---

### Explaining the Paradox

1. Symmetrical Nature:
   - Both circuits rely on the same basic transistor operation (control of current through the base-emitter junction), but their configurations and roles are inverted.
   - This symmetry creates the illusion that one is the "reversed" version of the other.

2. Complementary Roles:
   - Despite their similarities, the two circuits serve complementary purposes:
     - CBA: Efficient voltage amplification.
     - CCA: Effective impedance matching and current buffering.

3. The Reversal:
   - The signal input/output locations and impedance characteristics are reversed:
     - In the CBA, the input is low-impedance, and the output is high-impedance.
     - In the CCA, the input is high-impedance, and the output is low-impedance.

---

### Conclusion

The common-base amplifier and the common-collector amplifier are not literal reversals but mirror images in function and operation:
- One emphasizes voltage gain (CBA), while the other emphasizes current buffering and impedance matching (CCA).
- Their complementary roles highlight the versatility of the transistor but also explain their distinct applications.
