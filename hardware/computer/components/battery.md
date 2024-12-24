```sh
upower -i /org/freedesktop/UPower/devices/battery_BAT0
upower -i `upower -e | grep 'BAT'`
upower -i $(upower -e | grep BAT) | grep --color=never -E "state|to\ full|to\ empty|percentage"
```

cat /sys/class/power_supply/BAT0/capacity
find /sys/class/power_supply/BAT0/ -type f | xargs -tn1 cat

When to replace battery in a laptop?

There are a few signs that indicate it may be time to replace the battery in your laptop:

1. Reduced battery life: If you notice that your laptop's battery life is significantly shorter than when it was new, even after fully charging, it's likely time for a replacement.

2. Slow charging: If your laptop takes much longer to charge than it used to, it could be a sign of a deteriorating battery.

3. Battery not charging at all: If your laptop only works when plugged in and the battery doesn't seem to charge, it may need to be replaced.

4. Swollen battery: If you notice that your laptop's battery has swollen or expanded, it should be replaced immediately as this can be a safety hazard.

5. Age of the battery: Laptop batteries  last between 2-4 years, depending on usage and care. If your battery is approaching or exceeding this age, it may be time to consider a replacement.

6. Battery warning messages: Many laptops will display a warning message when the battery's capacity has significantly diminished, suggesting a replacement.

If you experience any of these signs, it's best to replace your laptop's battery to ensure optimal performance and avoid potential damage to your device. Always use a compatible battery from a reputable manufacturer or authorized seller.

Battery life refers to the amount of time a laptop can run on its battery power before needing to be recharged. It's essentially the duration between a full charge and when the battery is depleted to the point where the laptop shuts down or goes into hibernation mode.

When a laptop is new, its battery  provides several hours of use before requiring a recharge. However, over time and with regular use, the battery's capacity to hold a charge diminishes. This means that the battery life becomes progressively shorter.

For example, a new laptop battery might provide 6 hours of continuous use on a full charge. After a year or two, you might notice that the same battery only provides 3-4 hours of use before needing to be recharged, even when fully charged. This reduction in battery life is a normal part of a battery's aging process and is a sign that the battery may need to be replaced soon to maintain the laptop's portability and convenience.

The  battery life varies depending on factors such as the laptop model, battery size and quality, power management settings, and the types of applications and tasks you run on your laptop.

Replacing the battery in a laptop is necessary when you notice significant signs of battery degradation. Here are key indicators that it's time to replace your laptop battery:

1. **Reduced Battery Life:**
   - If your laptop's battery life has significantly decreased from when it was new (e.g., from several hours to less than an hour), it might be time to replace it.

2. **Battery Not Charging:**
   - If the battery isn't charging properly or at all, despite being plugged in and the charging indicator light being on, it may be defective.

3. **Frequent Overheating:**
   - If your laptop or battery becomes excessively hot during use or charging, it could indicate battery problems.

4. **Battery Warning Messages:**
   - If your operating system shows warning messages about battery health, such as "Consider replacing your battery" or "Battery not detected," it's a strong indication.

5. **Swollen Battery:**
   - Physical swelling or bulging of the battery is a serious issue and requires immediate replacement to prevent potential damage or hazards.

6. **Sudden Shutdowns:**
   - If your laptop shuts down abruptly without warning, even when the battery indicator shows remaining charge, the battery may be failing.

### Steps to Check Battery Health:

- **Windows:**
  1. Open Command Prompt as an administrator.
  2. Type `powercfg /batteryreport` and press Enter.
  3. Locate and open the generated battery report file to review battery health.

- **macOS:**
  1. Hold the Option key and click the Apple menu.
  2. Select "System Information."
  3. Under the "Hardware" section, select "Power" to view battery health information.

### Tips for Prolonging Battery Life:

- **Avoid Extreme Temperatures:** Keep your laptop in a moderate temperature range.
- **Regularly Calibrate the Battery:** Fully charge and discharge the battery periodically.
- **Use Battery Saver Mode:** Enable power-saving features to extend battery life.
- **Unplug When Fully Charged:** Avoid keeping the laptop plugged in at 100% for extended periods.

If your laptop exhibits any of these signs or the battery health check indicates a poor condition, it's time to consider replacing the battery.

For a Lenovo laptop, the signs indicating that it's time to replace the battery are similar to those for any other laptop, but there are specific tools and steps you can use to check battery health on Lenovo devices:

### Signs to Replace Your Lenovo Laptop Battery:

1. **Reduced Battery Life:**
   - Noticeable decrease in how long your laptop stays powered on battery alone.

2. **Battery Not Charging:**
   - Battery fails to charge even when connected to power and the charging indicator light is on.

3. **Frequent Overheating:**
   - The laptop or battery gets unusually hot during use or charging.

4. **Battery Warning Messages:**
   - System alerts such as "Consider replacing your battery" or "Battery not detected."

5. **Swollen Battery:**
   - Physical swelling or bulging of the battery, which can be hazardous.

6. **Sudden Shutdowns:**
   - Unexpected shutdowns even when the battery indicator shows sufficient charge.

### Checking Battery Health on Lenovo Laptops:

#### Using Lenovo Vantage:
1. **Open Lenovo Vantage:**
   - If you don't have it installed, download and install Lenovo Vantage from the Microsoft Store.
   - Open Lenovo Vantage from your start menu.

2. **Navigate to the Hardware Settings:**
   - Click on "Device" and then "Battery."

3. **Check Battery Health:**
   - Lenovo Vantage provides detailed battery information,  health status, charge cycles, and battery capacity.

#### Using Lenovo Diagnostics:
1. **Open Lenovo Diagnostics:**
   - Download and install Lenovo Diagnostics from the Lenovo support website if you don't already have it.
   - Open Lenovo Diagnostics from your start menu.

2. **Run Battery Test:**
   - In Lenovo Diagnostics, go to "Battery" and run the battery test.
   - Review the test results for battery health and performance.

### Steps to Replace the Battery:

1. **Power Down and Unplug:**
   - Turn off your laptop and disconnect it from any power source.

2. **Remove the Back Cover:**
   - Unscrew and remove the back cover of your laptop (refer to your laptop's manual for detailed instructions).

3. **Disconnect the Old Battery:**
   - Carefully disconnect the battery connector from the motherboard.
   - Remove the screws securing the battery and lift it out.

4. **Install the New Battery:**
   - Place the new battery in the compartment and secure it with screws.
   - Connect the battery to the motherboard.

5. **Replace the Back Cover:**
   - Reattach the back cover and secure it with screws.

6. **Power On and Charge:**
   - Turn on your laptop and connect it to the power source. Allow the new battery to fully charge.

### Tips for Prolonging Battery Life:

- **Avoid Extreme Temperatures:** Store and use your laptop in moderate temperatures.
- **Calibrate the Battery:** Perform a full charge and discharge cycle periodically.
- **Use Battery Saver Mode:** Enable power-saving settings to extend battery life.
- **Unplug When Fully Charged:** Avoid leaving the laptop plugged in at 100% for long periods.

To decide if your laptop battery needs to be replaced, you can look for several signs and use tools to check its health. Here are steps and factors to consider:

### Signs Your Battery May Need Replacement

1. **Short Battery Life:**
   - If your laptop battery drains quickly despite a full charge, it might be nearing the end of its lifespan.

2. **Unexpected Shutdowns:**
   - If your laptop shuts down suddenly, even when the battery shows remaining charge, this is a strong indicator of battery problems.

3. **Battery Warning Messages:**
   - Many operating systems will notify you if there is an issue with your battery. Pay attention to warnings about low battery health or the need for replacement.

4. **Overheating:**
   - If your laptop gets unusually hot, the battery might be faulty and needs checking.

5. **Physical Damage:**
   - Bulging, leaks, or other physical deformities in the battery case are serious signs that it needs to be replaced immediately.

### Checking Battery Health

#### Windows

1. **Battery Report:**
   - Open Command Prompt as an administrator and type:
     ```bash
     powercfg /batteryreport
     ```
   - This generates a detailed battery report in the specified directory. Review this report for battery wear and health status.

2. **Battery Health Tools:**
   - Some manufacturers provide their own tools for checking battery health (e.g., Dell Power Manager, Lenovo Vantage).

#### macOS

1. **Battery Health:**
   - Click the Apple logo > About This Mac > System Report > Power.
   - Check the “Cycle Count” and “Condition.” A high cycle count and a condition other than “Normal” indicate it’s time to consider a replacement.

2. **Battery Status Menu:**
   - Hold the Option key and click the battery icon in the menu bar to see the battery condition.

### Battery Diagnostic Tools

- **Third-Party Software:**
  - Tools like BatteryInfoView, HWMonitor, or CoconutBattery (for macOS) provide detailed information about your battery health,  capacity, wear level, and cycle count.

### General Guidelines

- **Cycle Count:**
  - Most laptop batteries are rated for a specific number of charge cycles (often 300-500). Check your battery’s cycle count and compare it with the manufacturer’s rating.

- **Design Capacity vs. Full Charge Capacity:**
  - Compare the original design capacity of your battery with its current full charge capacity. A significant drop indicates battery degradation.

### Summary

- Look for signs like short battery life, unexpected shutdowns, and overheating.
- Use built-in tools or third-party software to check battery health and cycle count.
- Pay attention to manufacturer warnings and battery status indicators.

If you find significant wear or performance issues, it’s likely time to replace your laptop battery.

If your Lenovo laptop shows signs of battery degradation or the battery health check indicates poor condition, it's time to replace the battery to ensure optimal performance and safety.

For a Lenovo laptop, you can follow these specific steps to decide if the battery needs to be replaced:

### Signs Your Lenovo Laptop Battery May Need Replacement

1. **Short Battery Life:**
   - Notice if your laptop battery drains quickly despite being fully charged.

2. **Unexpected Shutdowns:**
   - Watch for unexpected shutdowns even when the battery shows a significant charge.

3. **Battery Warning Messages:**
   - Pay attention to any system notifications about battery health.

4. **Overheating:**
   - Check if the laptop gets unusually hot, which might indicate a battery issue.

5. **Physical Damage:**
   - Look for bulging, leaks, or other physical deformities in the battery case.

### Checking Battery Health on a Lenovo Laptop

#### Using Lenovo Vantage

1. **Install Lenovo Vantage:**
   - If you don’t have it installed, download and install Lenovo Vantage from the Microsoft Store.

2. **Open Lenovo Vantage:**
   - Launch the application from your Start menu.

3. **Check Battery Status:**
   - Navigate to the “Hardware Settings” section.
   - Click on “Power” to view the battery status.
   - Lenovo Vantage provides information on the battery condition, cycle count, and other health indicators.

#### Using Command Prompt

1. **Generate Battery Report:**
   - Open Command Prompt as an administrator.
   - Type the following command and press Enter:
     ```bash
     powercfg /batteryreport
     ```
   - This generates a detailed battery report,  saved in your user directory. Open the report to check the battery’s health, cycle count, and other details.

### Interpreting the Battery Report

1. **Cycle Count:**
   - Compare the cycle count with Lenovo’s specifications for your battery model. Typically, laptop batteries are rated for 300-500 cycles.

2. **Design Capacity vs. Full Charge Capacity:**
   - Look at the “Design Capacity” and the “Full Charge Capacity.” A significant difference indicates battery degradation.

3. **Health Indicators:**
   - The battery report will include a section on the battery’s health, providing insights into its performance and whether it may need replacing.

### Summary

- **Use Lenovo Vantage** for a straightforward check of your battery health.
- **Generate and review a battery report** via Command Prompt to get detailed information.
- Look for signs of battery degradation like short battery life, unexpected shutdowns, overheating, and physical damage.
- Compare the cycle count and capacity values with Lenovo’s specifications.

If the battery health is poor or the cycle count is high, it's likely time to replace the battery.
