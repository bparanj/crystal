Implement the feature such that the following is displayed on the screen:
IP Configuration

Configuration Method: DHCP
Local IP              10.20.20.44
Subnet Mask           255.255.255.0
Default gateway       10.20.20.1
Primary DNS Server    10.2.2.4
VPN connected         Yes
Internet connected    Yes
Last sync 8 minutes ago

To implement a feature that displays specific network configuration details (such as IP, subnet, gateway, DNS, VPN status, and internet connection), follow these steps to set up a script that collects and displays the information on your Ubuntu server:

### Step 1: **Install Necessary Tools**

Ensure you have the tools required to gather the network information:
```bash
sudo apt update
sudo apt install net-tools openvpn curl
```

- **net-tools** provides the `ifconfig` and `route` commands to gather network interface information.
- **openvpn** is needed to check VPN status (if you’re using OpenVPN).
- **curl** is used to check internet connectivity.

### Step 2: **Create a Script for Displaying IP Configuration**

1. **Create the script** that will collect the IP configuration and display it in the required format:
```bash
sudo nano /usr/local/bin/show-ip-config.sh
```

2. **Add the following content** to the script:
```bash
#!/bin/bash

# Gather network details
local_ip=$(hostname -I | awk '{print $1}')
subnet_mask=$(ifconfig | grep -A 1 'inet ' | grep -oP 'netmask \K\S+')
default_gateway=$(ip route | grep default | awk '{print $3}')
primary_dns=$(nmcli dev show | grep 'IP4.DNS' | awk '{print $2}' | head -n 1)

# Check VPN connection status
vpn_status=$(ip route | grep -q "10.8.0.0" && echo "Yes" || echo "No")  # Adjust IP range as per your VPN

# Check Internet connection
internet_status=$(curl -s --head http://www.google.com | head -n 1 | grep "200 OK" > /dev/null && echo "Yes" || echo "No")

# Last sync (just a static example, should be based on your sync logic)
last_sync="8 minutes ago"

# Display the configuration
echo "IP Configuration"
echo ""
echo "Configuration Method: DHCP"
echo "Local IP              $local_ip"
echo "Subnet Mask           $subnet_mask"
echo "Default Gateway       $default_gateway"
echo "Primary DNS Server    $primary_dns"
echo "VPN connected         $vpn_status"
echo "Internet connected    $internet_status"
echo "Last sync             $last_sync"
```

3. **Make the script executable**:
```bash
sudo chmod +x /usr/local/bin/show-ip-config.sh
```

### Step 3: **Run the Script Automatically on Boot**

To ensure the script runs and displays the configuration after boot:

1. **Modify the `profile` to run the script after login**:

```bash
sudo nano /etc/profile.d/show-ip-config.sh
```

2. **Add the following line** to automatically run the script upon login:
```bash
/usr/local/bin/show-ip-config.sh
```

3. **Make it executable**:
```bash
sudo chmod +x /etc/profile.d/show-ip-config.sh
```

### Step 4: **Test the Script**

Reboot the server and verify that after login, you see something like this on the screen:

```
IP Configuration

Configuration Method: DHCP
Local IP              10.20.20.44
Subnet Mask           255.255.255.0
Default Gateway       10.20.20.1
Primary DNS Server    10.2.2.4
VPN connected         Yes
Internet connected    Yes
Last sync             8 minutes ago
```

### Explanation:
- **`hostname -I`**: Retrieves the local IP address.
- **`ifconfig`**: Extracts the subnet mask.
- **`ip route`**: Retrieves the default gateway and VPN status.
- **`nmcli`**: Provides DNS information.
- **`curl`**: Checks for internet connectivity by making an HTTP request.
- **VPN Status**: Based on a search for a VPN IP range in the routing table.

You can adjust the specific logic for detecting VPN connections or syncing depending on your environment.

To implement this feature with the specific information you've requested, we'll modify our previous script to display a more detailed and formatted IP Configuration screen. Here's how to do it:

1. Modify the IP Configuration menu script:

```bash
sudo nano /usr/local/bin/ip-config-menu.sh
```

Replace the content with the following:

```bash
#!/bin/bash

# Function to check internet connectivity
check_internet() {
    ping -c 1 8.8.8.8 > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "Yes"
    else
        echo "No"
    fi
}

# Function to check VPN connectivity
check_vpn() {
    # This is a placeholder. Replace with actual VPN check logic
    if ip link show | grep -q tun0; then
        echo "Yes"
    else
        echo "No"
    fi
}

# Function to get last sync time
get_last_sync() {
    # This is a placeholder. Replace with actual sync check logic
    echo "8 minutes ago"
}

# Function to display IP information
display_ip_info() {
    clear
    echo "IP Configuration"
    echo "================="
    echo
    echo "Configuration Method: DHCP"
    
    # Get network information
    local_ip=$(ip -4 addr show | grep -v "127.0.0.1" | grep "inet" | awk '{print $2}' | cut -d/ -f1 | head -n1)
    subnet_mask=$(ip -4 addr show | grep -v "127.0.0.1" | grep "inet" | awk '{print $2}' | cut -d/ -f2 | head -n1)
    subnet_mask=$(ipcalc -m $local_ip/$subnet_mask | grep Netmask | awk '{print $2}')
    default_gateway=$(ip route | grep default | awk '{print $3}')
    primary_dns=$(grep nameserver /etc/resolv.conf | awk '{print $2}' | head -n1)
    
    echo "Local IP              $local_ip"
    echo "Subnet Mask           $subnet_mask"
    echo "Default gateway       $default_gateway"
    echo "Primary DNS Server    $primary_dns"
    echo "VPN connected         $(check_vpn)"
    echo "Internet connected    $(check_internet)"
    echo "Last sync             $(get_last_sync)"
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

2. Make sure the script is executable:

```bash
sudo chmod +x /usr/local/bin/ip-config-menu.sh
```

3. Install `ipcalc` if it's not already installed:

```bash
sudo apt update
sudo apt install ipcalc
```

4. The rest of the setup remains the same as in the previous answer, including the systemd service files and the boot delay.

5. If you want to customize the VPN check or sync time logic, you'll need to modify the `check_vpn()` and `get_last_sync()` functions in the script to reflect your actual setup.

After implementing these changes and rebooting the system, you should see a screen that closely matches the format you specified, with real-time information about the network configuration.

Some of the information (like VPN connectivity and last sync time) might require additional logic or integration with other systems to provide accurate data. The script provided here uses placeholder logic for these items, which you'll need to replace with actual checks based on your specific setup.

This script assumes a DHCP configuration. If you need to support both DHCP and static IP configurations, you'll need to add logic to detect the configuration method and display the appropriate information.

