`nmap` (Network Mapper) is a powerful tool used for network discovery and security auditing. It can scan large networks or single hosts to discover available hosts, services, operating systems, firewalls, and other characteristics. Here's a basic guide on how to use `nmap`:

### 1. Installing Nmap

First, ensure `nmap` is installed on your system.

- **On Ubuntu/Debian:**
  ```bash
  sudo apt-get update
  sudo apt-get install nmap
  ```
- **On CentOS/RHEL:**
  ```bash
  sudo yum install nmap
  ```
- **On Fedora:**
  ```bash
  sudo dnf install nmap
  ```
- **On macOS** (using Homebrew):
  ```bash
  brew install nmap
  ```

### 2. Basic Scanning

- **Scan a Single IP or Hostname:**
  ```bash
  nmap [target]
  ```
  Replace `[target]` with the IP address or hostname you wish to scan.

- **Scan Multiple IPs/Hosts:**
  ```bash
  nmap [target1] [target2] [target3]
  ```
  You can list several targets separated by spaces.

- **Scan a Range of IPs:**
  ```bash
  nmap [start_range]-[end_range]
  ```
  Example: `nmap 192.168.1.1-20` scans IPs from 192.168.1.1 to 192.168.1.20.

- **Scan a Subnet:**
  ```bash
  nmap [subnet]
  ```
  Example: `nmap 192.168.1.0/24` scans the entire 192.168.1.x subnet.

### 3. Scan Types

- **Perform a Quick Scan:**
  ```bash
  nmap -T4 -F [target]
  ```
  The `-T4` flag speeds up the scan, and `-F` tells `nmap` to only scan the 100 most common ports.

- **Scan Specific Ports:**
  ```bash
  nmap -p [port(s)] [target]
  ```
  Example: `nmap -p 22,80,443 example.com` scans ports 22, 80, and 443 on `example.com`.

- **Scan All Ports:**
  ```bash
  nmap -p- [target]
  ```
  Scans all 65535 ports.

### 4. Detecting OS and Services

- **Enable OS and Version Detection:**
  ```bash
  nmap -A [target]
  ```
  The `-A` option enables OS detection, version detection, script scanning, and traceroute.

### 5. Output Formats

`nmap` can generate results in various formats:

- **Normal Output to a File:**
  ```bash
  nmap [target] -oN [outputfile.txt]
  ```
- **XML Output:**
  ```bash
  nmap [target] -oX [outputfile.xml]
  ```
- **Grepable Output:**
  ```bash
  nmap [target] -oG [outputfile.txt]
  ```

### Security Considerations

Using `nmap` can trigger alarms in security systems and may be considered hostile or illegal on networks you do not own or have permission to test. Always obtain explicit permission before scanning networks.

This overview covers the basics of using `nmap`. `nmap` has a wide range of options and capabilities, so consider referring to the official documentation or the `nmap` man page (`man nmap`) for more advanced features and techniques.
