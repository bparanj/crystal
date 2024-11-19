### Current Autoswitching Diodes

A Current Autoswitching Diode Circuit ensures that current is automatically supplied to a load from the higher-current-capacity source. This type of circuit is used in systems requiring seamless transitions between current sources, such as power supplies and batteries.

1. Diode Behavior:
   - Diodes allow current flow in only one direction, enabling current autoswitching between sources based on their ability to provide current.

2. Current Source Selection:
   - The diode connected to the source with a higher current capacity automatically conducts, while the diode connected to the lower-capacity source remains reverse-biased.

3. Applications:
   - Battery backup systems.
   - Multi-source power supplies (e.g., solar and grid).
   - Load sharing between current sources.

### Experiment

To design and simulate a Current Autoswitching Diode Circuit that switches between two current sources based on their output capacity.

#### Components:

1. 2 Diodes (1N4007 or similar).
2. 2 Power Supplies (\( V_1 = 9V \), \( V_2 = 9V \)).
3. Resistors:
   - \( R_1 = 100\Omega \) (to limit current from \( V_1 \)).
   - \( R_2 = 1k\Omega \) (to limit current from \( V_2 \)).
   - \( R_{load} = 500\Omega \) (represents the load).
4. Multimeters (to measure current and voltage).
5. Breadboard and wires.

### Circuit

1. Primary Current Source (\( V_1 \)):
   - Connect \( V_1 \) to the anode of the first diode (\( D_1 \)).
   - Place \( R_1 \) between \( V_1 \) and the anode of \( D_1 \).
   - Connect the cathode of \( D_1 \) to one end of \( R_{load} \).

2. Secondary Current Source (\( V_2 \)):
   - Connect \( V_2 \) to the anode of the second diode (\( D_2 \)).
   - Place \( R_2 \) between \( V_2 \) and the anode of \( D_2 \).
   - Connect the cathode of \( D_2 \) to the same end of \( R_{load} \).

3. Load Resistor (\( R_{load} \)):
   - Connect the other end of \( R_{load} \) to ground.

4. Multimeters:
   - Place one multimeter in series with \( D_1 \) to measure current from \( V_1 \).
   - Place another multimeter in series with \( D_2 \) to measure current from \( V_2 \).
   - Place another multimeter across \( R_{load} \) to measure the load voltage.

### Steps

#### 1. Equal Current Capacity:

1. Set \( R_1 = 100\Omega \) and \( R_2 = 1k\Omega \), and turn on both power supplies (\( V_1 = 9V, V_2 = 9V \)).
2. Observe:
   - \( D_1 \) conducts more current because \( R_1 \) offers less resistance.
   - \( D_2 \) is reverse-biased, blocking current from \( V_2 \).

#### 2. Simulate Higher Resistance on \( V_1 \):

1. Increase \( R_1 \) to \( 1k\Omega \) to reduce the current from \( V_1 \).
2. Observe:
   - \( D_2 \) conducts as the primary source, supplying current from \( V_2 \).
   - \( D_1 \) is reverse-biased.

#### 3. Simulate Fault on \( V_2 \):

1. Turn off \( V_2 \).
2. Observe:
   - \( D_1 \) becomes the sole conductor, supplying current from \( V_1 \).

#### 4. Restore Both Sources:

1. Turn \( V_2 \) back on and reduce \( R_1 \) to \( 100\Omega \).
2. Observe:
   - \( D_1 \) resumes conduction as the primary source with higher current capacity.

### Results

1. Equal Voltage Sources:
   - The source with the lower resistance path (higher current capacity) powers the load.

2. Higher Resistance Path:
   - If the primary source's resistance increases, the secondary source takes over automatically.

3. Fault Conditions:
   - If one source is turned off, the circuit seamlessly switches to the other source without interruption.

### Insights

1. Seamless Current Switching:
   - The diodes ensure smooth transitions between sources based on their current capacities.

2. Load Sharing:
   - The load is always powered by the source capable of delivering the required current.

3. Applications:
   - Used in systems where multiple current sources, such as batteries or power supplies, must cooperate to power a load.

This experiment can be implemented in Tinkercad, where you can:
1. Toggle the power supplies on/off.
2. Adjust resistances (\( R_1 \), \( R_2 \)) to simulate varying current capacities.
3. Use multimeters to measure current through the diodes and voltage across the load, confirming autoswitching behavior.
