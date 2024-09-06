Yes, there are a few ways to map a changing DHCP IP address on a home network to a domain name that can be accessed by other devices on the same network. Here are a couple of approaches:

1. Use mDNS (Multicast DNS):
   Many modern operating systems support mDNS, which allows devices to be addressed by a local domain name without needing a centralized DNS server. This is often referred to as "Zero-configuration networking" or "Bonjour" (Apple's implementation).

   - On Linux and macOS, this is typically built-in.
   - On Windows, you may need to install Bonjour Print Services.

   With mDNS, devices can be accessed using a ".local" domain, like "mycomputer.local".

2. Set up a local DNS server:
   You can set up a small DNS server on your network that can dynamically update DNS records based on DHCP leases. This is a more advanced solution but provides more control.

   ```bash
# Install dnsmasq (Ubuntu/Debian)
   sudo apt-get update
   sudo apt-get install dnsmasq

   # Configure dnsmasq
   sudo nano /etc/dnsmasq.conf

   # Add these lines to the configuration:
   domain-needed
   bogus-priv
   expand-hosts
   domain=home.lan
   local=/home.lan/
   dhcp-range=192.168.1.50,192.168.1.150,12h
   dhcp-option=option:router,192.168.1.1
   dhcp-option=option:dns-server,192.168.1.1

   # Restart dnsmasq
   sudo systemctl restart dnsmasq

   # Configure your router to use this machine as the DHCP server
   
```

   This example uses dnsmasq, which can serve as both a DHCP and DNS server. It will assign IP addresses and automatically create DNS entries for the devices.

3. Use Dynamic DNS (DDNS) with your router:
   Some routers support DDNS services, which can update a public domain name with your current IP address. While this is typically used for external access, some routers allow local resolution of this domain name.

4. Static DHCP leases:
   Instead of using truly dynamic IP addresses, you could configure your router to always assign the same IP to specific devices based on their MAC address. Then you could manually maintain a hosts file on each device or use a simple local DNS server.

The best solution depends on your specific needs, network setup, and technical comfort level. The mDNS solution is probably the simplest if your devices support it, while setting up a local DNS server gives you the most control and flexibility.

Using mDNS on a Mac is quite straightforward, as macOS has built-in support for this technology through its implementation called Bonjour. Here's how you can use mDNS on your Mac:

1. Set up your Mac's name:
   
   - Go to System Preferences (or System Settings on newer macOS versions)
   - Click on "Sharing"
   - At the top, you'll see a field labeled "Computer Name". This is the name that will be used for mDNS.
   - If you want to change it, just type in a new name.

2. Using mDNS to connect:

   - Once your Mac's name is set, other devices on the network can reach it using `<computername>.local`
   - For example, if your Mac's name is "MyMacBook", other devices can reach it using "MyMacBook.local"

3. Finding other mDNS devices:

   - Your Mac will automatically discover other mDNS-enabled devices on the network.
   - These devices will show up in Finder under the "Network" section.
   - You can also use the `ping` command in Terminal to test connectivity, like:
     ```
     ping MyMacBook.local
     ```

4. Using mDNS for services:

   - Many applications on macOS use mDNS automatically. For example:
     - File sharing will be available at `afp://MyMacBook.local` or `smb://MyMacBook.local`
     - Screen sharing can be initiated to `vnc://MyMacBook.local`

5. Troubleshooting:

   If you're having issues with mDNS:
   - Ensure your firewall isn't blocking mDNS traffic (UDP port 5353)
   - Try flushing your DNS cache:
     ```
     sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
     ```

6. Advanced usage:

   For developers or advanced users, macOS provides command-line tools for working with mDNS:
   
   

   ```bash
# Discover mDNS services
   dns-sd -B _services._dns-sd._udp

   # Browse for a specific service type (e.g., AirPlay)
   dns-sd -B _airplay._tcp

   # Resolve a specific service
   dns-sd -R "My Service" _http._tcp . 80 path=/mypath

   # Lookup a hostname
   dns-sd -G v4v6 MyMacBook.local

   # Publish a service
   dns-sd -P "My Web Server" _http._tcp . 80 MyMacBook.local /path
   
```

   These commands allow you to discover, browse, resolve, and publish mDNS services from the Terminal.

mDNS on macOS is designed to work out of the box, so in most cases, you don't need to do anything special to use it. Just make sure your devices are on the same local network, and you should be able to reach your Mac using its `.local` address from other devices that support mDNS.

mDNS is for local network use only. It won't work over the internet or between different subnets without additional configuration.

If mDNS is set up correctly and you're running a Python SimpleHTTPServer on your computer, other devices on your local network should be able to access it using `mycomputer.local:8000` in their web browsers, assuming a few conditions are met:

1. mDNS is working correctly on both the server (your computer) and the client devices.
2. The Python SimpleHTTPServer is running and bound to the correct network interface.
3. Your computer's firewall (if active) allows incoming connections on port 8000.

Let's break this down step-by-step:

1. Ensure mDNS is working:
   - On your computer (the server), make sure the computer name is set correctly.
   - On a client device, try pinging your computer using `ping mycomputer.local` to verify mDNS resolution is working.

2. Start the Python SimpleHTTPServer:
   
   

   ```python
# For Python 3.x
   python3 -m http.server 8000

   # For Python 2.x
   python -m SimpleHTTPServer 8000

   # To bind to all interfaces explicitly (may be necessary in some cases):
   python3 -m http.server 8000 --bind 0.0.0.0
   
```

   Run this command in the directory you want to serve. By default, it will bind to all network interfaces.

3. Check your firewall:
   - On macOS, go to System Preferences > Security & Privacy > Firewall.
   - Ensure Python is allowed to accept incoming connections.

4. Access from other devices:
   - On another device on the same network, open a web browser.
   - Enter the address: `http://mycomputer.local:8000`
   - You should see a directory listing or the index.html file if one exists in the served directory.

Troubleshooting:
1. If `mycomputer.local` doesn't work, try using the IP address of your computer instead.
2. Ensure all devices are on the same local network and subnet.
3. Some older devices or browsers might not support mDNS. In this case, you'll need to use the IP address.
4. If you're using a virtual machine or some network configurations, you might need to set up port forwarding.

This setup is for local network use only. It won't make your server accessible from the internet unless you set up port forwarding on your router (which isn't recommended for security reasons unless you know what you're doing).
