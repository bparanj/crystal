The data used in UEFI (Unified Extensible Firmware Interface) is primarily stored in the **NVRAM (Non-Volatile Random Access Memory)** on the motherboard. This includes boot entries, configuration settings, and other essential information required for the boot process.

Additionally, the UEFI firmware itself is typically stored on a **NOR-based EEPROM (Electrically Erasable Programmable Read-Only Memory)** chip on the motherboard³. This ensures that the firmware remains intact even when the computer is powered off.

### BIOS Password

The BIOS password is typically stored in the **CMOS (Complementary Metal-Oxide-Semiconductor) memory** on the motherboard¹². This memory is powered by a small battery, often referred to as the CMOS battery, which helps retain the BIOS settings, including the password, even when the computer is turned off.

### CMOS Battery

When the CMOS battery is dead, the BIOS settings, including the BIOS password, are typically lost. Here’s what happens:

1. **Loss of Settings**: The CMOS battery powers the CMOS memory, which stores BIOS settings. When the battery dies, these settings, including the BIOS password, are reset to their default values⁵.

2. **Date and Time Reset**: The system clock and date settings will also reset, often reverting to a default date and time.

3. **Boot Issues**: You might encounter boot issues or error messages, as the system may not remember the correct boot order or other configuration settings.

4. **Password Reset**: If a BIOS password was set, it will be cleared, allowing access without a password.

Replacing the CMOS battery and reconfiguring the BIOS settings is usually necessary to restore normal operation.
