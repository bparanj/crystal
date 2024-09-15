Provide instructions for implementing this feature:

Plug-in an Ethernet cable connected to your main network (i.e. the internet) to the
Ubuntu server's WAN port. When the server boots, it will send a DHCP request as it attempts to connect online. 
NOTE: This must be a non-proxy connection to the internet and will fail if you use the following subnets:
172.18.0.0/16 - This is the network where the Expunge clients connect 172.19.0.0/19 - This network allows the Expunge to communicate with our portal through a VPN connection for remote updates and assistance

To implement the feature where the Ubuntu server connects to the internet via the WAN port using DHCP while avoiding specific subnets (`172.18.0.0/16` and `172.19.0.0/19`), follow the steps below:

### 1. **Ensure the WAN port is correctly connected**
   - Plug an Ethernet cable connected to the main network (internet) into the WAN port of your Ubuntu server.

### 2. **Configure the Server for DHCP**
   - **Edit the Network Configuration File**:
     For Ubuntu 24.04, you may be using **Netplan** to manage network configurations.
     1. Open the network configuration file for the WAN interface. This file is  located in `/etc/netplan/`. It will have a `.yaml` extension, such as `00-installer-config.yaml` or `01-netcfg.yaml`.
        ```bash
        sudo nano /etc/netplan/00-installer-config.yaml
        ```

     2. In the file, make sure your WAN interface (e.g., `eth0` or `enp3s0`) is set to use DHCP for automatic IP configuration:
        ```yaml
        network:
          version: 2
          ethernets:
            eth0:  # Replace this with the correct WAN interface name
              dhcp4: true
              dhcp4-overrides:
                route-metric: 100
              dhcp6: false
        ```

     3. **Apply the changes**:
        After modifying the configuration, apply it using:
        ```bash
        sudo netplan apply
        ```

### 3. **Avoid Conflicting Subnets**
   To ensure the server does not use the restricted subnets (`172.18.0.0/16` and `172.19.0.0/19`), configure the routing table to reject those subnets.

   1. **Create Routing Rules**:
      You need to add specific routes to block the usage of these subnets. Use the `ip route` command to add rules that discard any traffic destined for those subnets:
      ```bash
      sudo ip route add blackhole 172.18.0.0/16
      sudo ip route add blackhole 172.19.0.0/19
      ```

   2. **Persist Routing Rules**:
      To ensure these routes persist after a reboot, add them to the network configuration or create a script that runs on boot.
      
      Option 1: Add them to the `/etc/netplan/` YAML file:
      ```yaml
      network:
        version: 2
        ethernets:
          eth0:
            dhcp4: true
            routes:
              - to: 172.18.0.0/16
                type: blackhole
              - to: 172.19.0.0/19
                type: blackhole
      ```
      Option 2: Create a script in `/etc/network/if-up.d/` to add these routes automatically on boot:
      ```bash
      sudo nano /etc/network/if-up.d/block_expunged_subnets
      ```
      Add the following content to the script:
      ```bash
      #!/bin/bash
      ip route add blackhole 172.18.0.0/16
      ip route add blackhole 172.19.0.0/19
      ```
      Save the file and make it executable:
      ```bash
      sudo chmod +x /etc/network/if-up.d/block_expunged_subnets
      ```

### 4. **Ensure Non-Proxy Connection**
   Ensure no proxy configurations are set in the system's environment variables or network configuration files that might route the traffic through a proxy.
   - Check for proxy configurations:
     ```bash
     env | grep -i proxy
     ```
   - If any proxy settings are found and should not be used, unset them:
     ```bash
     unset http_proxy
     unset https_proxy
     unset ftp_proxy
     ```

### 5. **Restart the Server**
   After applying the network and routing configurations, restart the server to ensure all settings take effect:
   ```bash
   sudo reboot
   ```

### 6. **Verify the Configuration**
   - **Check DHCP Assignment**:
     Once the server reboots, verify that the WAN port received an IP address via DHCP:
     ```bash
     ip addr show eth0  # Replace 'eth0' with your WAN interface
     ```
   - **Check the Routing Table**:
     Confirm the routing table has the blackhole routes for the restricted subnets:
     ```bash
     ip route
     ```
   - **Check Internet Connectivity**:
     Test the connection to the internet to ensure there is no proxy and the network is working:
     ```bash
     ping -c 4 google.com
     ```

These instructions will configure your Ubuntu server to obtain an IP address via DHCP from the WAN interface, while ensuring that it does not communicate over the restricted subnets (`172.18.0.0/16` and `172.19.0.0/19`).

To implement this feature on your Ubuntu 24.04 Server, we'll need to configure the network interface for DHCP on the WAN port while avoiding the specified subnets. Here's a step-by-step guide:

1. Identify the network interface:
   First, determine which network interface corresponds to the WAN port:

   ```bash
   ip a
   ```

   Look for the interface name (e.g., eth0, enp3s0) that corresponds to your WAN port.

2. Configure the network interface:
   Edit the Netplan configuration file. On Ubuntu 24.04, it's  located at `/etc/netplan/00-installer-config.yaml`:

   ```bash
   sudo nano /etc/netplan/00-installer-config.yaml
   ```

3. Add the following configuration, replacing `<interface_name>` with your  WAN interface name:

   ```yaml
   network:
     version: 2
     ethernets:
       <interface_name>:
         dhcp4: true
         dhcp4-overrides:
           use-routes: true
           use-dns: true
         dhcp6: false
         optional: true
         routes:
           - to: 172.18.0.0/16
             via: 0.0.0.0
             table: 200
           - to: 172.19.0.0/19
             via: 0.0.0.0
             table: 200
         routing-policy:
           - from: 172.18.0.0/16
             table: 200
           - from: 172.19.0.0/19
             table: 200
   ```

   This configuration:
   - Enables DHCP for IPv4
   - Disables IPv6
   - Adds routes to push traffic for the specified subnets to a separate routing table (200)

4. Save the file and exit the editor.

5. Apply the network configuration:

   ```bash
   sudo netplan apply
   ```

6. Create a script to handle the routing table:
   Create a new file `/etc/networkd-dispatcher/routable.d/50-custom-routes`:

   ```bash
   sudo nano /etc/networkd-dispatcher/routable.d/50-custom-routes
   ```

   Add the following content:

   ```bash
   #!/bin/sh
   ip route add prohibit 172.18.0.0/16 table 200
   ip route add prohibit 172.19.0.0/19 table 200
   ```

   This script adds "prohibit" routes for the specified subnets to routing table 200.

7. Make the script executable:

   ```bash
   sudo chmod +x /etc/networkd-dispatcher/routable.d/50-custom-routes
   ```

8. Reboot the system to ensure all changes take effect:

   ```bash
   sudo reboot
   ```

After rebooting, your Ubuntu server should:
- Request an IP address via DHCP on the WAN port
- Avoid using the specified subnets (172.18.0.0/16 and 172.19.0.0/19) for internet connectivity
- Be ready to connect to the internet through a non-proxy connection

To verify the configuration:
1. Check your IP address and routing:
   ```bash
   ip a
   ip route
   ```
2. Ensure you can connect to the internet:
   ```bash
   ping 8.8.8.8
   ```
3. Verify that traffic to the specified subnets is not routed:
   ```bash
   traceroute 172.18.0.1
   traceroute 172.19.0.1
   ```
   These should fail or show that the traffic is not routed.

If you encounter any issues or need to make adjustments, you can modify the Netplan configuration and reapply it, or edit the routing script as necessary.
