Yes, you can set up a PXE boot from a ThinkPad to allow other machines on the same network to boot into ShredOS and be wiped. Here’s a general outline of how you can achieve this:

1. **Set Up the PXE Server**:
   - You will need a machine (your ThinkPad) to act as the PXE server. Install a Linux distribution like Ubuntu or Debian on it.
   - Configure the PXE server to serve the ShredOS image. This involves setting up a DHCP server to assign IP addresses to client machines and a TFTP server to serve the ShredOS boot image¹.

2. **Download ShredOS**:
   - Download the latest ShredOS image from the [ShredOS GitHub repository](https://github.com/PartialVolume/shredos.x86_64)².

3. **Configure the PXE Boot Environment**:
   - Place the ShredOS boot image in the TFTP server directory.
   - Configure the DHCP server to point to the TFTP server and the ShredOS boot image. This  involves editing the `dhcpd.conf` file to include the necessary boot parameters¹.

4. **Boot Client Machines**:
   - Ensure that the client machines are set to boot from the network (PXE boot). This usually involves changing the boot order in the BIOS/UEFI settings.
   - When the client machines boot, they will receive an IP address from the DHCP server and download the ShredOS image from the TFTP server, allowing them to boot into ShredOS and start the wiping process³.

5. **Network Considerations**:
   - For optimal performance, use a gigabit network to ensure fast data transfer rates during the boot process¹.

¹: [GitHub - ShredOS PXE Boot Setup](https://github.com/PartialVolume/shredos.x86_64/discussions/148)
²: [ShredOS GitHub Repository](https://github.com/PartialVolume/shredos.x86_64)
³: [Enabling PXE Boot for Lenovo ThinkPad](https://it.engr.ncsu.edu/help/kb/enabling-pxe-boot-for-lenovo-thinkpad/)

Source: Conversation with Copilot, 9/6/2024
(1) How to create a simple PXE server to serve a single version of ShredOS .... https://github.com/PartialVolume/shredos.x86_64/discussions/148.
(2) ShredOS x86_64 - Disk Eraser - GitHub. https://github.com/PartialVolume/shredos.x86_64.
(3) Enabling PXE Boot for Lenovo ThinkPad - Engineering Information .... https://it.engr.ncsu.edu/help/kb/enabling-pxe-boot-for-lenovo-thinkpad/.
(4) How to PXE boot to Shredos · PartialVolume shredos.x86_64 - GitHub. https://github.com/PartialVolume/shredos.x86_64/discussions/137.
(5) undefined. https://github.com/netbootxyz/netboot.xyz.
(6) Alternative to wipe drives with DBAN, Veracrypt? : r/sysadmin - Reddit. https://www.reddit.com/r/sysadmin/comments/zdaiwl/alternative_to_wipe_drives_with_dban_veracrypt/.
(7) Wipe disks with ShredOS - TechSoup Forums. https://forums.techsoup.org/t/wipe-disks-with-shredos/7347.
(8) undefined. https://partedmagic.com/.
(9) undefined. https://www.youtube.com/watch?v=J9vjvPth71U.
(10) undefined. https://purelev.com/.
