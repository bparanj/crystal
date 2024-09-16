If we wanted to allow everybody access to an HTTP server running on port 80 on Debian, how would we write the rule to add to our nftables.conf?

To allow everyone access to an HTTP server running on port 80 using nftables on Debian, you can add the following rule to your `nftables.conf` file:

```nft
table inet filter {
    chain input {
        type filter hook input priority 0; policy accept;
        
        # Allow HTTP traffic on port 80
        tcp dport 80 accept
    }
}
```

This configuration does the following:
1. **Defines a table** named `filter` in the `inet` family, which applies to both IPv4 and IPv6.
2. **Creates a chain** named `input` with a filter type, hooked into the input path with a priority of 0, and sets the default policy to accept.
3. **Adds a rule** to accept TCP traffic destined for port 80.

Make sure to reload the nftables configuration after making changes:

```bash
sudo nft -f /etc/nftables.conf
```

This will apply the new rules.
