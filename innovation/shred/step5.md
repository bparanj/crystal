Provide instructions to implement:
Connect a desktop or laptop (don't use an Apple computer for your first test) via Ethernet to the Expunge Ubuntu server's LAN port. Attempt to network boot the device, and wait for the Expunge Wiping Menu to appear.

Here’s a step-by-step guide to implement the feature for network booting a device connected via Ethernet to the **Expunge Ubuntu server's LAN port** and displaying the Expunge Wiping Menu:

### 1. **Prepare the Ubuntu Server (Expunge) for PXE Boot**
   PXE (Preboot Execution Environment) allows a client machine to boot from the network. You need to configure a PXE server on your Expunge Ubuntu server.

#### 1.1 Install the Necessary Packages
   - You need to install a **TFTP server**, **DHCP server**, and **NFS/HTTP server** (for serving files):
     ```bash
     sudo apt update
     sudo apt install isc-dhcp-server tftpd-hpa tftp-hpa
     sudo apt install apache2  # Optional if you prefer HTTP over NFS for file transfer
     ```

#### 1.2 Configure the DHCP Server (for PXE Boot)
   - Edit the DHCP server configuration to allow PXE booting on the LAN interface of the Ubuntu server:
     ```bash
     sudo nano /etc/dhcp/dhcpd.conf
     ```
   - Add or modify the following lines:
     ```bash
     subnet 10.0.0.0 netmask 255.255.255.0 {
       range 10.0.0.100 10.0.0.200;  # IP range for clients
       option routers 10.0.0.1;
       option subnet-mask 255.255.255.0;
       option broadcast-address 10.0.0.255;
       option domain-name-servers 10.0.0.1;  # Or your preferred DNS
       next-server 10.0.0.1;  # IP of your TFTP/PXE server
       filename "pxelinux.0";  # Boot file for PXE clients
     }
     ```

   - Save and exit the file. Restart the DHCP service:
     ```bash
     sudo systemctl restart isc-dhcp-server
     ```

#### 1.3 Configure TFTP and PXE Boot Files
   - Create the directory for TFTP and PXE boot files:
     ```bash
     sudo mkdir -p /srv/tftp/pxelinux.cfg
     sudo mkdir /srv/tftp/images
     ```
   - Copy the **PXELinux** boot loader and related files:
     ```bash
     sudo apt install pxelinux syslinux-common
     sudo cp /usr/lib/PXELINUX/pxelinux.0 /srv/tftp/
     sudo cp /usr/lib/syslinux/modules/bios/ldlinux.c32 /srv/tftp/
     sudo cp /usr/lib/syslinux/modules/bios/menu.c32 /srv/tftp/
     sudo cp /usr/lib/syslinux/modules/bios/libutil.c32 /srv/tftp/
     sudo cp /usr/lib/syslinux/modules/bios/vesamenu.c32 /srv/tftp/
     ```

#### 1.4 Create the PXE Boot Menu
   - Create a default boot menu file:
     ```bash
     sudo nano /srv/tftp/pxelinux.cfg/default
     ```
   - Add the following content to define the menu:
     ```bash
     DEFAULT vesamenu.c32
     PROMPT 0
     TIMEOUT 50
     MENU TITLE Expunge Wiping Menu

     LABEL wipe
       MENU LABEL Start Expunge Wiping Process
       KERNEL vmlinuz
       APPEND initrd=initrd.img boot=wipe
     
     LABEL local
       MENU LABEL Boot from Local Drive
       LOCALBOOT 0
     ```

   - Save and exit the file.

### 2. **Prepare the Expunge Wiping System Files**
   You need to provide the kernel (`vmlinuz`) and the initial RAM disk (`initrd.img`) that will boot the client into the wiping environment.

   - Copy or download your custom **Expunge Wiping System** kernel and initrd files into `/srv/tftp/images/`. If you don’t have these yet, you will need to build or provide a basic Linux kernel image.

### 3. **Configure the LAN Port on the Ubuntu Server**
   - Ensure the Ubuntu server’s LAN port is configured to a static IP address (e.g., `10.0.0.1`), which matches the subnet in the DHCP configuration.

   Edit the Netplan configuration for the LAN interface:
   ```bash
   sudo nano /etc/netplan/00-installer-config.yaml
   ```
   Example content:
   ```yaml
   network:
     version: 2
     ethernets:
       enp3s0:
         dhcp4: no
         addresses:
           - 10.0.0.1/24
         gateway4: 10.0.0.1
   ```
   Apply the changes:
   ```bash
   sudo netplan apply
   ```

### 4. **Connect the Client Device and Boot**

#### 4.1 Connect via Ethernet
   - Connect a desktop or laptop (not an Apple computer) via an Ethernet cable to the LAN port of the Expunge Ubuntu server.

#### 4.2 Enable Network Boot on Client
   - Power on the client device and access its BIOS/UEFI settings. Look for the **Boot Order** settings and ensure that **PXE Boot (Network Boot)** is enabled and set as the first boot option.

#### 4.3 Boot the Device
   - Reboot the client device. It should send a DHCP request to the Ubuntu server’s LAN port and boot using the PXE configuration provided.
   - You should see the **Expunge Wiping Menu** appear with the options:
     - **Start Expunge Wiping Process** (to initiate the wiping)
     - **Boot from Local Drive** (to bypass PXE and boot normally).

### 5. **Test the Wiping Menu**
   - Select "Start Expunge Wiping Process" from the menu.
   - The client should now boot into the Expunge wiping system (as configured in the `vmlinuz` and `initrd.img` files) and display the wiping interface.

### 6. **Troubleshoot (if needed)**
   - **Check TFTP logs**:
     ```bash
     sudo journalctl -u tftpd-hpa
     ```
   - **Check DHCP logs**:
     ```bash
     sudo journalctl -u isc-dhcp-server
     ```

This setup should allow you to network boot a client machine into the Expunge Wiping Menu from your Ubuntu server.

To implement network booting from the Ubuntu server's LAN port and display an Expunge Wiping Menu, we'll need to set up a PXE (Preboot Execution Environment) server on the Ubuntu machine. This involves configuring DHCP, TFTP, and HTTP services. Here's a step-by-step guide:

1. Install necessary packages:

```bash
sudo apt update
sudo apt install isc-dhcp-server tftpd-hpa apache2 syslinux-common pxelinux
```

2. Configure DHCP server:

Edit the DHCP configuration file:
```bash
sudo nano /etc/dhcp/dhcpd.conf
```

Add the following configuration (adjust the IP ranges as needed):

```
subnet 172.18.0.0 netmask 255.255.0.0 {
  range 172.18.0.10 172.18.0.100;
  option routers 172.18.0.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
  filename "pxelinux.0";
  next-server 172.18.0.1;
}
```

3. Configure the network interface for the LAN port:

Edit the Netplan configuration:
```bash
sudo nano /etc/netplan/01-netcfg.yaml
```

Add configuration for the LAN interface (replace `<LAN_INTERFACE>` with your  interface name, e.g., eth1):

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    <LAN_INTERFACE>:
      addresses: [172.18.0.1/16]
      dhcp4: no
```

Apply the configuration:
```bash
sudo netplan apply
```

4. Configure TFTP server:

Edit the TFTP configuration:
```bash
sudo nano /etc/default/tftpd-hpa
```

Ensure it contains:
```
TFTP_USERNAME="tftp"
TFTP_DIRECTORY="/var/lib/tftpboot"
TFTP_ADDRESS=":69"
TFTP_OPTIONS="--secure"
```

5. Set up PXE boot files:

```bash
sudo mkdir -p /var/lib/tftpboot/pxelinux.cfg
sudo cp /usr/lib/PXELINUX/pxelinux.0 /var/lib/tftpboot/
sudo cp /usr/lib/syslinux/modules/bios/*.c32 /var/lib/tftpboot/
```

6. Create a PXE menu:

```bash
sudo nano /var/lib/tftpboot/pxelinux.cfg/default
```

Add the following content:

```
DEFAULT menu.c32
PROMPT 0
TIMEOUT 300
ONTIMEOUT local

MENU TITLE Expunge Wiping Menu

LABEL local
    MENU LABEL Boot from local drive
    LOCALBOOT 0

LABEL expunge
    MENU LABEL Expunge Wiping Tool
    KERNEL expunge/vmlinuz
    APPEND initrd=expunge/initrd.img
```

7. Prepare the Expunge Wiping Tool:

You'll need to create or obtain the Linux kernel (vmlinuz) and initial ramdisk (initrd.img) for your Expunge Wiping Tool. Place these files in `/var/lib/tftpboot/expunge/`.

8. Restart services:

```bash
sudo systemctl restart isc-dhcp-server
sudo systemctl restart tftpd-hpa
sudo systemctl restart apache2
```

9. Configure the Ubuntu server's firewall to allow DHCP, TFTP, and HTTP:

```bash
sudo ufw allow 67/udp
sudo ufw allow 69/udp
sudo ufw allow 80/tcp
```

10. On the client machine (desktop or laptop):

- Connect it to the Ubuntu server's LAN port via Ethernet.
- Enter the BIOS/UEFI settings and enable network booting (PXE boot).
- Set the boot order to prioritize network booting.

When you boot the client machine, it should now attempt to network boot from the Ubuntu server. The Expunge Wiping Menu should appear, allowing you to choose between booting from the local drive or launching the Expunge Wiping Tool.

- Ensure that the Expunge Wiping Tool's kernel and initrd are compatible with PXE booting.
- This setup assumes the Expunge Wiping Tool can run directly from the network. If it requires additional files, you may need to set up an NFS share or include the files in the initrd.
- Test thoroughly in a controlled environment before deploying.
- Ensure proper security measures are in place, as PXE booting can be a security risk if not properly configured.

