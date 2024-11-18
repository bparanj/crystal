### Decoupling Diode

A Decoupling Diode is used in circuits to isolate power supply branches, ensuring that a fault or fluctuation in one branch does not affect others. It allows current to flow in one direction, preventing backflow into other parts of the circuit.

### Applications:

1. Preventing reverse current in multi-supply systems.
2. Isolating critical components during power supply failure.
3. Protecting batteries or sensitive devices from backfeed currents.

### Circuit Operation:

1. Forward Current Flow:
   - The diode allows current to flow when the voltage is correctly applied (positive at the anode and negative at the cathode).

2. Reverse Blocking:
   - The diode blocks current flow if the voltage reverses, protecting the circuit from reverse currents.

### Experiment

#### Objective:

To design and simulate a Decoupling Diode Circuit that demonstrates current isolation between two power branches.

#### Components:

1. 1N4007 Diode (or similar).
2. Resistors:
   - \( R1 = 1k\Omega \) (to represent a load on one branch).
   - \( R2 = 1k\Omega \) (to represent a load on the other branch).
3. Power Supplies:
   - \( V1 = 9V \).
   - \( V2 = 5V \) (simulating a secondary supply).
4. Multimeters (to measure current and voltage in each branch).

#### Circuit Connections:

1. Decoupling Diodes:
   - Place a diode (\( D1 \)) between \( V1 \) and \( R1 \) (anode to \( V1 \), cathode to \( R1 \)).
   - Place another diode (\( D2 \)) between \( V2 \) and \( R2 \) (anode to \( V2 \), cathode to \( R2 \)).

2. Loads:
   - Connect \( R1 \) and \( R2 \) to ground to simulate separate loads for the two power supplies.

3. Multimeters:
   - Place one multimeter in series with \( R1 \) to measure current through \( R1 \).
   - Place another multimeter in series with \( R2 \) to measure current through \( R2 \).

### Steps

#### 1. Set Up Circuit:

   - Assemble the circuit in Tinkercad as described.

#### 2. Normal Operation (Both Supplies On):

   - Turn on both power supplies (\( V1 = 9V \), \( V2 = 5V \)).
   - Observe:
     - \( D1 \) conducts, supplying current to \( R1 \).
     - \( D2 \) conducts, supplying current to \( R2 \).
     - Both branches operate independently.

#### 3. Simulate Failure of \( V2 \):

   - Turn off \( V2 \).
   - Observe:
     - \( D2 \) blocks reverse current from \( V1 \).
     - \( R2 \) does not receive power.
     - \( R1 \) continues to operate normally on \( V1 \).

#### 4. Simulate Failure of \( V1 \):

   - Turn off \( V1 \) and turn \( V2 \) back on.
   - Observe:
     - \( D1 \) blocks reverse current from \( V2 \).
     - \( R1 \) does not receive power.
     - \( R2 \) continues to operate normally on \( V2 \).

### Results

1. Both Supplies On:
   - Current flows through both branches independently.
   - No interference between \( R1 \) and \( R2 \).

2. One Supply Off:
   - The diode associated with the turned-off supply blocks current backflow, isolating the faulty branch.
   - The load connected to the working supply operates normally.

### Insights

1. Isolation:
   - The diodes effectively decouple the power branches, ensuring one branch's failure does not affect the other.

2. Protection:
   - The decoupling diodes prevent reverse currents, protecting both power supplies and sensitive components.

3. Applications:
   - Multi-supply systems, battery isolation, and fault-tolerant designs.

This experiment can be easily implemented in Tinkercad, where you can toggle power supplies on and off to observe the decoupling diode's behavior in maintaining branch isolation. Use multimeters to verify current flow and isolation.
