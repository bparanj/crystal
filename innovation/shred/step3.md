Provide instructions to implement this on Ubuntu server:
Connect the power cable and boot the Ubuntu server. Normal boot time is about 5 minutes. You will see the IP Configuration menu once the appliance has completely booted.

To implement this feature on an Ubuntu server, we'll need to create a custom boot process that displays an IP Configuration menu after the system has fully booted. Here's a step-by-step guide to achieve this:

1. Create a systemd service to run our custom script:

```bash
sudo nano /etc/systemd/system/ip-config-menu.service
```

Add the following content:

```
[Unit]
Description=IP Configuration Menu
After=network.target

[Service]
ExecStart=/usr/local/bin/ip-config-menu.sh
Type=idle
StandardInput=tty
StandardOutput=tty
TTYPath=/dev/tty1

[Install]
WantedBy=multi-user.target
```

2. Create the script for the IP Configuration menu:

```bash
sudo nano /usr/local/bin/ip-config-menu.sh
```

Add the following content:

```bash
#!/bin/bash

# Function to display IP information
display_ip_info() {
    clear
    echo "IP Configuration Menu"
    echo "====================="
    echo
    ip -4 addr show | grep -v "127.0.0.1" | grep "inet" | awk '{print $NF, $2}'
    echo
    echo "Press any key to refresh, or 'q' to quit."
}

# Main loop
while true; do
    display_ip_info
    read -n 1 -s key
    if [[ $key == "q" ]]; then
        break
    fi
done

# Clear screen before exiting
clear
```

3. Make the script executable:

```bash
sudo chmod +x /usr/local/bin/ip-config-menu.sh
```

4. Enable and start the service:

```bash
sudo systemctl enable ip-config-menu.service
sudo systemctl start ip-config-menu.service
```

5. To simulate the 5-minute boot time and ensure all services are loaded before showing the IP Configuration menu, create a delay script:

```bash
sudo nano /usr/local/bin/boot-delay.sh
```

Add the following content:

```bash
#!/bin/bash
sleep 300  # 5 minutes in seconds
systemctl start ip-config-menu.service
```

Make it executable:

```bash
sudo chmod +x /usr/local/bin/boot-delay.sh
```

6. Create a systemd service for the boot delay:

```bash
sudo nano /etc/systemd/system/boot-delay.service
```

Add the following content:

```
[Unit]
Description=Boot Delay for IP Configuration Menu
After=network.target

[Service]
ExecStart=/usr/local/bin/boot-delay.sh
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

7. Enable the boot delay service:

```bash
sudo systemctl enable boot-delay.service
```

8. To make sure the IP Configuration menu appears on the main console, edit the GRUB configuration:

```bash
sudo nano /etc/default/grub
```

Find the line starting with `GRUB_CMDLINE_LINUX_DEFAULT` and change it to:

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash console=tty1"
```

Update GRUB:

```bash
sudo update-grub
```

9. Reboot the system:

```bash
sudo reboot
```

After implementing these steps:

1. The Ubuntu server will boot normally.
2. After about 5 minutes (simulating the normal boot time), the IP Configuration menu will appear on the main console (tty1).
3. The menu will display the IP configuration for all network interfaces.
4. Users can press any key to refresh the information or 'q' to quit the menu.

This setup provides a simple IP Configuration menu that appears after boot, allowing users to easily view the network configuration of the Ubuntu server.

To implement the scenario where the **Ubuntu server** shows an **IP Configuration menu** after booting, follow these instructions:

### Step 1: **Connect Power and Boot the Server**
   - Plug in the power cable and connect the necessary peripherals (if needed for manual control). 
   - Turn on the server by pressing the power button.
   - The normal boot time is estimated to be around **5 minutes**.

### Step 2: **Set Up Automatic IP Configuration Display on Boot**

This step involves configuring the server to display an IP configuration menu once it has completely booted.

#### 2.1 **Install Necessary Packages**:
   To display network information (IP configuration) upon booting, you can use a script or a tool such as `net-tools` or `ifconfig` (though `ip` command is the more modern alternative in Ubuntu).

   ```bash
   sudo apt update
   sudo apt install net-tools
   ```

#### 2.2 **Create a Startup Script to Show IP Configuration**:

   - Create a script that will run automatically after boot and display the IP configuration of the server:
   
     ```bash
     sudo nano /etc/systemd/system/ipconfig-display.service
     ```

   - Add the following content to the file:

     ```bash
     [Unit]
     Description=Display IP Configuration at boot
     After=network-online.target
     Wants=network-online.target

     [Service]
     ExecStart=/usr/bin/ip addr show
     Type=oneshot
     RemainAfterExit=yes

     [Install]
     WantedBy=multi-user.target
     ```

   - This script will display the IP address details once the network is online.

#### 2.3 **Enable the Startup Service**:

   - After creating the script, you need to enable and start it as a systemd service:

     ```bash
     sudo systemctl daemon-reload
     sudo systemctl enable ipconfig-display.service
     sudo systemctl start ipconfig-display.service
     ```

#### 2.4 **Set Up a Simple IP Display on Login (Optional)**:

   - Another approach is to display the IP configuration on the login screen (console) after booting. This can be done by adding a script to `/etc/profile.d/`:

     ```bash
     sudo nano /etc/profile.d/show-ip.sh
     ```

   - Add this content to display the IP information each time you log in:
   
     ```bash
     #!/bin/bash
     echo "IP Configuration:"
     ip addr show
     ```

   - Make the script executable:
   
     ```bash
     sudo chmod +x /etc/profile.d/show-ip.sh
     ```

#### 2.5 **Reboot and Verify**:
   - After completing the steps, reboot the server:
   
     ```bash
     sudo reboot
     ```

   - After about **5 minutes**, you should see the IP configuration displayed either automatically or after logging in via the console.

This approach ensures that the IP configuration will be visible after booting the server, which is useful in headless or remote environments.
