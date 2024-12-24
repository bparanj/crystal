password hashes were stored in /etc/passwd file, now it is stored in /etc/shadow How does this prevent users from cracking password hashes? How is this new directory secure in Debian

The shift from storing password hashes in `/etc/passwd` to `/etc/shadow` significantly enhances security. Here's how:

### **Why the Change?**
1. **Access Control**:
   - **`/etc/passwd`**: This file is world-readable, meaning any user on the system can read it. While it contains essential user account information, having password hashes here would expose them to all users, making it easier for malicious actors to attempt cracking them.
   - **`/etc/shadow`**: This file is only readable by the root user. By moving password hashes here, it restricts access to these hashes, making it much harder for unauthorized users to obtain them.

### **How It Prevents Cracking**:
1. **Limited Access**:
   - Since only the root user can read `/etc/shadow`, it significantly reduces the risk of password hashes being exposed to non-privileged users. This means that even if a user gains access to the system, they cannot easily obtain the password hashes to attempt offline cracking.

2. **Enhanced Security Measures**:
   - **Password Aging and Policies**: `/etc/shadow` also allows for more detailed password policies, such as password aging, expiration, and account lockout after a certain number of failed attempts². These measures add additional layers of security.

### **Security in Debian**:
- **Permissions**: By default, Debian sets strict permissions on `/etc/shadow`, ensuring that only the root user can read or modify it.
- **Security Updates**: Debian regularly updates its security policies and tools to protect against new vulnerabilities, ensuring that the system remains secure.

By moving password hashes to `/etc/shadow`, Debian and other Linux distributions enhance the overall security of the system, making it much harder for attackers to crack passwords.
