The encryption element used to mutually derive encryption keys is typically **Diffie-Hellman key exchange**. This cryptographic method allows two parties to securely exchange cryptographic keys over a public channel without actually transmitting the keys themselves.

### How it works:
- Both parties agree on a large prime number and a base (generator).
- Each party generates a private key and a corresponding public key.
- They exchange public keys and then use their private key to compute a shared secret (encryption key).
  
This shared secret can then be used as the basis for encryption (such as for AES or other symmetric encryption algorithms), enabling secure communication. Variants like **Elliptic Curve Diffie-Hellman (ECDH)** are also widely used due to their enhanced security and efficiency.

Diffie-Hellman is commonly used in protocols like **TLS** and **VPNs** to establish secure connections.
