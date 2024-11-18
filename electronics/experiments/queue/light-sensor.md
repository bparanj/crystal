### Light Sensor with Tinkercad

This experiment demonstrates the use of a photoresistor (LDR) as a light sensor to control the brightness of an LED based on ambient light levels.

#### Components

1. Photoresistor (LDR)
2. 10kΩ resistor
3. LED
4. 220Ω resistor
5. 5V power supply (or battery)
6. Breadboard
7. Jumper wires

### Steps

   - Connect the positive terminal of the 5V power supply to the positive rail of the breadboard.
   - Connect the negative terminal of the power supply to the negative rail of the breadboard.

2. Photoresistor Voltage Divider:
   - Place the photoresistor (LDR) on the breadboard.
   - Connect one terminal of the photoresistor to the positive rail of the breadboard.
   - Connect the other terminal of the photoresistor to one terminal of the 10kΩ resistor.
   - Connect the other terminal of the 10kΩ resistor to the negative rail of the breadboard.
   - This forms a voltage divider where the midpoint voltage depends on light intensity.

3. LED Circuit:
   - Place the LED on the breadboard, with the anode (long leg) connected to the positive rail and the cathode (short leg) connected to one terminal of the 220Ω resistor.
   - Connect the other terminal of the 220Ω resistor to the negative rail of the breadboard.

4. Connect LDR to LED:
   - Connect the midpoint of the voltage divider (junction of the photoresistor and the 10kΩ resistor) to the anode of the LED.

### Procedure

1. Run the simulation in Tinkercad.
2. Adjust the light level on the photoresistor (click on it in the simulation to simulate different light intensities).
3. Observe the brightness of the LED:
   - Bright Light: The resistance of the LDR decreases, increasing the voltage at the junction, making the LED brighter.
   - Dim Light: The resistance of the LDR increases, reducing the voltage at the junction, dimming the LED.

This experiment demonstrates how light intensity can control an electronic circuit, showcasing a basic light-sensitive application.

Yes, Tinkercad has a temperature sensor (TMP36) in its component library. You can use it to design temperature-related experiments. The TMP36 outputs a voltage proportional to temperature and can be used with Arduino for temperature sensing and control applications.