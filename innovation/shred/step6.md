Provide instructions to implement:
Once that test is successful, use an unmanaged, gigabit network switch to the LAN port of the Ubuntu Server (Expunge). This network is the one that will boot directly into Expunge. No router/internet connection/other network should be plugged into this subnet. 

Here are the instructions to implement this setup using an unmanaged gigabit network switch connected to the LAN port of your Ubuntu Server (Expunge):

1. Physical Setup:
   
   a. Disconnect any existing devices from the Ubuntu Server's LAN port.
   
   b. Connect an unmanaged gigabit network switch to the LAN port of the Ubuntu Server.
   
   c. Ensure no other network devices (routers, modems, etc.) are connected to this switch.

2. Verify Ubuntu Server Configuration:

   Ensure your Ubuntu Server's LAN interface is still correctly configured as per the previous setup:

   ```bash
   sudo nano /etc/netplan/01-netcfg.yaml
   ```

   Verify the LAN interface configuration:

   ```yaml
   network:
     version: 2
     renderer: networkd
     ethernets:
       <LAN_INTERFACE>:
         addresses: [172.18.0.1/16]
         dhcp4: no
   ```

   If any changes were made, apply them:

   ```bash
   sudo netplan apply
   ```

3. DHCP Server Configuration:

   Verify the DHCP server configuration is still correct:

   ```bash
   sudo nano /etc/dhcp/dhcpd.conf
   ```

   Ensure it contains:

   ```
   subnet 172.18.0.0 netmask 255.255.0.0 {
     range 172.18.0.10 172.18.0.100;
     option routers 172.18.0.1;
     option domain-name-servers 8.8.8.8, 8.8.4.4;
     filename "pxelinux.0";
     next-server 172.18.0.1;
   }
   ```

4. Restart DHCP Service:

   ```bash
   sudo systemctl restart isc-dhcp-server
   ```

5. Verify PXE Boot Configuration:

   Check that your PXE boot menu is still correctly set up:

   ```bash
   sudo nano /var/lib/tftpboot/pxelinux.cfg/default
   ```

   Ensure it contains the Expunge Wiping Menu options.

6. Firewall Configuration:

   Verify that the firewall allows the necessary services:

   ```bash
   sudo ufw status
   ```

   Ensure that ports 67/udp (DHCP), 69/udp (TFTP), and 80/tcp (HTTP) are allowed.

7. Testing the Setup:

   a. Connect a client computer to the unmanaged switch.
   
   b. Configure the client computer's BIOS/UEFI to prioritize network booting (PXE).
   
   c. Boot the client computer and verify that it receives an IP address from the Ubuntu Server's DHCP service.
   
   d. The client should boot into the Expunge Wiping Menu.

8. Scaling the Setup:

   a. You can now connect multiple client computers to the unmanaged switch.
   
   b. Each client should be able to PXE boot and access the Expunge Wiping Menu independently.

9. Isolation Verification:

   a. Ensure that no devices on this network can access the internet or any other network.
   
   b. Verify that the only network services available are those provided by the Ubuntu Server for PXE booting and the Expunge Wiping Tool.

10. Monitoring and Maintenance:

    a. Regularly check the Ubuntu Server's logs for any issues:
    
    ```bash
    sudo journalctl -u isc-dhcp-server
    sudo journalctl -u tftpd-hpa
    ```
    
    b. Monitor the server's resource usage to ensure it can handle the number of connected clients.

11. Security Considerations:

    a. Since this is an isolated network, ensure physical security of the switch and the Ubuntu Server.
    
    b. Regularly update the Ubuntu Server and the Expunge Wiping Tool to patch any vulnerabilities.

By following these steps, you'll have a dedicated, isolated network for booting client machines directly into WipeOS using PXE. This setup allows for efficient wiping of multiple devices simultaneously without exposing them to external networks.

Test this setup with various client devices to ensure compatibility and reliability before using it in a production environment.

To extend the setup to use an unmanaged gigabit switch for connecting multiple clients that will boot directly into WipeOS, follow these steps:

### Step 1: **Set up the Unmanaged Gigabit Switch**

1. **Connect the Switch**:
   - Plug one end of an Ethernet cable into the **LAN port** of your **Ubuntu server (Expunge)**.
   - Connect the other end to the **unmanaged gigabit switch**.

2. **Connect Client Devices**:
   - Plug your client devices (desktops, laptops, etc.) into the unmanaged switch using Ethernet cables.
   - These client devices will use this switch to communicate with the Ubuntu server for network booting.

### Step 2: **Ensure Proper Network Configuration**

Since no router or internet connection will be present on this subnet, the Ubuntu server (Expunge) needs to act as the **DHCP server** and **TFTP server** to serve the PXE boot files. You've already set this up in the previous steps.

- **Subnet**: Ensure the subnet of the LAN interface on the Ubuntu server is set to a private range like `10.0.0.0/24`, which is already configured.

### Step 3: **Check the DHCP Configuration**

Make sure your **DHCP configuration** is set up correctly. You already configured the DHCP server, but verify that it assigns IP addresses correctly on the **unmanaged subnet**.

1. Open the DHCP configuration file:
   ```bash
   sudo nano /etc/dhcp/dhcpd.conf
   ```

2. Confirm the settings:
   ```bash
   subnet 10.0.0.0 netmask 255.255.255.0 {
     range 10.0.0.100 10.0.0.200;  # IP range for clients
     option routers 10.0.0.1;
     option subnet-mask 255.255.255.0;
     option broadcast-address 10.0.0.255;
     option domain-name-servers 10.0.0.1;  # Or leave empty if no DNS needed
     next-server 10.0.0.1;  # IP of your TFTP server
     filename "pxelinux.0";  # Boot file for PXE clients
   }
   ```

3. **Restart the DHCP server**:
   ```bash
   sudo systemctl restart isc-dhcp-server
   ```

### Step 4: **Test Booting Multiple Devices**

1. **Power on the client devices** connected to the switch.
2. Ensure that PXE boot is enabled in the BIOS/UEFI settings of the clients.
3. The clients should now send a DHCP request through the unmanaged switch, and the Ubuntu server should respond by providing an IP address and the PXE boot configuration.
4. After receiving the boot files (kernel and initrd), the **Expunge Wiping Menu** should appear on each client device.

### Step 5: **Verify Booting to WipeOS**

Once the clients boot successfully, they should reach the **Expunge Wiping Menu** or boot directly into **WipeOS** as configured in the PXE boot setup.

### Step 6: **Monitor the Connections**

- On the **Ubuntu server**, you can monitor the connected clients and ensure they are receiving the appropriate PXE boot information:
   - **Check DHCP Logs**:
     ```bash
     sudo journalctl -u isc-dhcp-server
     ```
   - **Check TFTP Logs**:
     ```bash
     sudo journalctl -u tftpd-hpa
     ```

### Step 7: **Troubleshooting (if needed)**

- **Network Issues**:
  - Ensure that all client devices are correctly connected to the gigabit switch and the switch is functioning properly.
  - If clients are not receiving IP addresses, check the DHCP server logs and verify that the clients are in the same subnet.

- **Boot Issues**:
  - Ensure that the PXE boot configuration is correct (`/srv/tftp/pxelinux.cfg/default`).
  - If the clients are not booting into the **WipeOS**, check that the `vmlinuz` and `initrd` files are being served correctly by the TFTP server.

### Summary of Key Points:
- The unmanaged switch is used to allow multiple clients to connect to the Expunge Ubuntu server via Ethernet.
- The Ubuntu server acts as the **DHCP server** and **TFTP server**, providing IP addresses and booting configurations.
- Ensure the subnet is isolated with no external router or internet connection plugged into this network.
- PXE booting should automatically load WipeOS or the Expunge Wiping Menu on the connected clients.

This setup enables a fully isolated network where multiple client machines can boot into Expunge via the Ubuntu server acting as a PXE server.

Certainly. Let's set up an isolated network using an unmanaged gigabit switch connected to the LAN port of your Ubuntu Server (Expunge) for booting directly into Expunge. Here are the step-by-step instructions:

1. Physical Setup:
   a. Disconnect any existing devices from the Ubuntu Server's LAN port.
   b. Connect an unmanaged gigabit network switch to the LAN port of the Ubuntu Server.
   c. Ensure no other network devices (routers, modems, etc.) are connected to this switch.

2. Configure the Ubuntu Server's LAN interface:
   Edit the Netplan configuration file:
   ```bash
   sudo nano /etc/netplan/01-netcfg.yaml
   ```
   Add or modify the configuration for the LAN interface:
   ```yaml
   network:
     version: 2
     renderer: networkd
     ethernets:
       <LAN_INTERFACE>:  # Replace with  interface name (e.g., eth1, enp3s0)
         addresses: [172.18.0.1/16]
         dhcp4: no
   ```
   Apply the configuration:
   ```bash
   sudo netplan apply
   ```

3. Configure DHCP server:
   Edit the DHCP configuration file:
   ```bash
   sudo nano /etc/dhcp/dhcpd.conf
   ```
   Ensure it contains the following configuration:
   ```
   subnet 172.18.0.0 netmask 255.255.0.0 {
     range 172.18.0.10 172.18.0.254;
     option routers 172.18.0.1;
     option domain-name-servers 172.18.0.1;
     filename "pxelinux.0";
     next-server 172.18.0.1;
   }
   ```
   Restart the DHCP server:
   ```bash
   sudo systemctl restart isc-dhcp-server
   ```

4. Verify PXE boot configuration:
   Ensure your TFTP server is correctly configured:
   ```bash
   sudo nano /etc/default/tftpd-hpa
   ```
   It should contain:
   ```
   TFTP_USERNAME="tftp"
   TFTP_DIRECTORY="/var/lib/tftpboot"
   TFTP_ADDRESS=":69"
   TFTP_OPTIONS="--secure"
   ```

5. Check PXE boot menu:
   Verify the PXE boot menu is set up correctly:
   ```bash
   sudo nano /var/lib/tftpboot/pxelinux.cfg/default
   ```
   Ensure it contains the option to boot into Expunge.

6. Firewall configuration:
   Allow necessary services through the firewall:
   ```bash
   sudo ufw allow 67/udp
   sudo ufw allow 69/udp
   sudo ufw allow 4011/udp
   ```

7. Disable internet forwarding:
   Edit the sysctl configuration:
   ```bash
   sudo nano /etc/sysctl.conf
   ```
   Ensure the following line is present and uncommented:
   ```
   net.ipv4.ip_forward=0
   ```
   Apply the changes:
   ```bash
   sudo sysctl -p
   ```

8. Testing the setup:
   a. Connect a client computer to the unmanaged switch.
   b. Configure the client's BIOS/UEFI to prioritize network booting (PXE).
   c. Boot the client and verify it receives an IP address from the Ubuntu Server's DHCP.
   d. The client should boot directly into Expunge.

9. Scaling the setup:
   - You can now connect multiple client computers to the unmanaged switch.
   - Each client should be able to PXE boot and launch Expunge independently.

10. Isolation verification:
    - Use a network analysis tool on a connected client to ensure no external network access is available.
    - Attempt to ping external IP addresses to confirm isolation.

11. Monitoring and maintenance:
    Regularly check server logs for any issues:
    ```bash
    sudo journalctl -u isc-dhcp-server
    sudo journalctl -u tftpd-hpa
    ```

12. Security considerations:
    - Ensure physical security of the switch and the Ubuntu Server.
    - Regularly update the Ubuntu Server and Expunge to patch any vulnerabilities.
    - Consider implementing MAC address filtering in the DHCP server for additional security.

By following these steps, you'll have created an isolated network where client machines connected to the unmanaged switch will boot directly into Expunge via PXE, without any access to external networks or the internet. This setup allows for secure and efficient operation of Expunge across multiple devices simultaneously.

Remember to thoroughly test this configuration with various client devices to ensure compatibility and reliability before using it in a production environment.

To implement a network using an unmanaged gigabit switch that allows client devices to boot directly into **Expunge** without any external network connections (such as routers or internet), follow these instructions:

### Step 1: **Set up the Unmanaged Gigabit Switch**

1. **Connect the Ubuntu Server to the Switch**:
   - Plug one end of an Ethernet cable into the **LAN port** of your **Ubuntu server (Expunge)**.
   - Connect the other end of the cable to the unmanaged gigabit switch.

2. **Connect Client Devices to the Switch**:
   - Connect each client device (desktop, laptop, etc.) to the unmanaged gigabit switch using Ethernet cables.
   - These devices will now be in the same isolated subnet as the Ubuntu server.

### Step 2: **Prepare the Expunge Ubuntu Server for PXE Boot**

You need to ensure that the server acts as a **PXE Boot** server, which includes DHCP and TFTP services, without any reliance on the internet or other external networks.

#### 2.1 **Check DHCP Server Configuration**
- The Ubuntu server should already be acting as the **DHCP server**. You will verify and fine-tune its configuration to provide IP addresses to the clients.

1. **Edit the DHCP configuration** to match the isolated subnet, ensuring no external routers or internet connections are involved.
   ```bash
   sudo nano /etc/dhcp/dhcpd.conf
   ```
   
2. **Verify the configuration** to ensure it provides IP addresses in the correct range for the isolated network:
   ```bash
   subnet 10.0.0.0 netmask 255.255.255.0 {
       range 10.0.0.100 10.0.0.200;  # IP range for clients
       option routers 10.0.0.1;       # Ubuntu server IP acting as gateway
       option subnet-mask 255.255.255.0;
       option broadcast-address 10.0.0.255;
       option domain-name-servers 10.0.0.1;  # No external DNS, Ubuntu server will serve DNS
       next-server 10.0.0.1;  # TFTP server on Ubuntu
       filename "pxelinux.0";  # Boot file for PXE clients
   }
   ```

3. **Restart the DHCP service** to apply any changes:
   ```bash
   sudo systemctl restart isc-dhcp-server
   ```

#### 2.2 **Ensure TFTP Server is Set Up**
1. **Check the TFTP server configuration**. Ensure the TFTP root directory has the necessary boot files.
   - The TFTP server should already be installed as per previous instructions, but confirm that the required files (`pxelinux.0`, `vmlinuz`, and `initrd.img`) are in place:
   ```bash
   sudo ls /srv/tftp
   ```
   - Ensure that **`pxelinux.0`**, **`ldlinux.c32`**, and the kernel/initrd files for Expunge are in the directory.

2. **Verify the TFTP configuration** for serving boot files:
   ```bash
   sudo nano /etc/default/tftpd-hpa
   ```
   - Make sure the configuration points to the correct TFTP root directory:
   ```bash
   TFTP_DIRECTORY="/srv/tftp"
   TFTP_OPTIONS="--secure"
   ```

3. **Restart the TFTP server**:
   ```bash
   sudo systemctl restart tftpd-hpa
   ```

### Step 3: **Test the Network Boot on Client Devices**

1. **Power on the client devices** connected to the unmanaged gigabit switch.

2. **Ensure PXE Boot is enabled** on each client:
   - Go into the BIOS/UEFI settings of each client device and ensure that **Network Boot (PXE)** is enabled.
   - Set PXE as the first boot option in the boot order.

3. **Boot the clients**:
   - When the clients boot, they should send a **DHCP request** to the Ubuntu server via the switch, receive an IP address, and then download the necessary PXE boot files from the server.
   - The clients should then boot into **Expunge** or the Expunge Wiping Menu, depending on how you’ve configured the PXE boot menu.

### Step 4: **Verify the Expunge Boot Process**

- If the setup is correct, the client devices should automatically load the **Expunge Wiping System** via PXE without the need for external networks or routers.
- The Ubuntu server should handle all booting, DHCP, and file-serving tasks in this isolated environment.

### Step 5: **Monitor and Troubleshoot**

1. **Check the DHCP server logs**:
   ```bash
   sudo journalctl -u isc-dhcp-server
   ```

2. **Check the TFTP server logs**:
   ```bash
   sudo journalctl -u tftpd-hpa
   ```

3. **Check client connections**:
   - Ensure that all devices are properly connected to the unmanaged switch.
   - Verify that the client devices are requesting IP addresses and downloading boot files correctly.

### Final Notes:
- This setup works on a fully **isolated network** (no router or internet connection).
- You can add more clients by connecting them to the gigabit switch and ensuring they are configured for PXE boot.
- Make sure no external devices (like routers or internet connections) are connected to this subnet to keep it isolated.

By following these instructions, your network switch will allow client devices to boot directly into Expunge via PXE boot from the Ubuntu server, all within an isolated network.


