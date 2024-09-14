
-   NIST 800-88r1 Clear
-   U.S. Department of Defense 5220.22-M 3-Pass
-   U.S. Department of Defense 5220.28-STD 7-Pass

Several open-source tools can provide data wiping capabilities that meet or exceed these standards. Here are some options:

1. DBAN (Darik's Boot and Nuke):
   - Supports NIST 800-88 Clear method
   - Offers DoD 5220.22-M 3-pass 
   - Can be configured for 7-pass overwriting

2. Eraser:
   - Supports NIST 800-88 Clear
   - Offers DoD 5220.22-M 3-pass
   - Provides customizable overwriting patterns, so 7-pass can be configured

3. shred (part of GNU Core Utilities):
   - Can be configured to meet NIST 800-88 Clear
   - Supports customizable overwrite patterns, so both 3-pass and 7-pass DoD standards can be implemented

4. nwipe:
   - Supports NIST 800-88 Clear
   - Offers DoD 5220.22-M 3-pass
   - Can be configured for 7-pass overwriting

5. BCWipe:
   - Supports NIST 800-88 Clear
   - Offers DoD 5220.22-M 3-pass
   - Provides 7-pass DoD 5220.28-STD

 while these tools can meet or exceed the specified standards, the effectiveness of data wiping can also depend on the type of storage media being wiped. For modern SSDs, some of these overwriting methods may not be as effective due to wear leveling and other SSD-specific technologies.

Would you like more details on any of these tools or information about their usage?

Several open-source tools provide data wiping standards like NIST 800-88r1 Clear, DoD 5220.22-M (3-Pass), and DoD 5220.28-STD (7-Pass). Here are some that you can consider:

### 1. **Nwipe** (Used in ShredOS)
   - **Standards Supported**:
     - NIST 800-88r1 Clear
     - DoD 5220.22-M (3-Pass)
     - DoD 5220.28-STD (7-Pass)
   - **Overview**:
     - Nwipe is a disk-wiping tool that originated from the DBAN project but is actively maintained. It supports a variety of secure data erasure standards, including those required by NIST and DoD.
   - **How to Use**:
     - Nwipe can be run from the command line or integrated into a bootable Linux system like ShredOS. You can specify the desired wiping method by using its flags when invoking the tool on a disk.
   - **Website**: [Nwipe on GitHub](https://github.com/PartialVolume/nwipe)

### 2. **DBAN (Darik's Boot and Nuke)**
   - **Standards Supported**:
     - DoD 5220.22-M (3-Pass)
     - DoD 5220.28-STD (7-Pass)
   - **Overview**:
     - DBAN is one of the original tools for secure disk erasure and supports several wiping standards. While it is no longer actively maintained, it is still used for basic secure wiping tasks.
   - **How to Use**:
     - DBAN boots from a USB or CD and offers menu-driven options to select the wiping standard, including DoD and custom overwriting methods.
   - **Website**: [DBAN Official](https://dban.org/)

### 3. **Blancco Drive Eraser** (Open-source alternative: Nwipe or DBAN)
   - **Standards Supported**:
     - NIST 800-88r1 Clear
     - DoD 5220.22-M (3-Pass)
     - DoD 5220.28-STD (7-Pass)
   - **Overview**:
     - While Blancco itself is a commercial solution, its open-source alternatives like **Nwipe** and **DBAN** provide similar standards for data wiping.

### 4. **Secure Erase (For NIST 800-88r1 Clear)**
   - **Standards Supported**:
     - NIST 800-88r1 Clear
   - **Overview**:
     - This tool, available in Linux distributions as part of the `hdparm` package, performs a secure erase command on SSDs and HDDs that complies with NIST 800-88r1 Clear standards. This command overwrites the entire drive with a single pass.
   - **How to Use**:
     - You can run `hdparm` to invoke the Secure Erase feature on a drive to perform NIST-compliant clear operations.
   - **Example Command**:
     ```bash
     sudo hdparm --user-master u --security-erase NULL /dev/sdX
     ```

### 5. **GNU Shred**
   - **Standards Supported**:
     - Can be configured to simulate DoD 5220.22-M (3-Pass)
   - **Overview**:
     - GNU Shred is a standard tool available on most Linux systems. It overwrites data multiple times and can be used to meet specific requirements like a 3-pass wipe.
   - **How to Use**:
     - Example command to overwrite a file/device 3 times:
     ```bash
     sudo shred -n 3 /dev/sdX
     ```

### Summary:
- **Nwipe** (via ShredOS or directly) is the closest open-source equivalent supporting multiple erasure standards, including NIST 800-88r1 and DoD 5220.22-M.
- **DBAN** is an older but still usable option for DoD standards.
- **Secure Erase** (`hdparm`) can be used for NIST 800-88r1 Clear operations, especially for SSDs.

You can combine these tools depending on your specific needs for wiping disks securely according to the required standards.
