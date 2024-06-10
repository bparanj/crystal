Yes, HTTP/2 is enabled by default in Caddy.

Caddy automatically enables HTTP/2 for all HTTPS connections without requiring any additional configuration. When a client that supports HTTP/2 connects to Caddy over HTTPS, Caddy will automatically negotiate and upgrade the connection to HTTP/2.

This means that if you have configured Caddy to serve HTTPS traffic (by specifying the HTTPS port or using automatic HTTPS with Let's Encrypt), it will automatically use HTTP/2 for those connections when possible.

HTTP/2 brings several benefits, such as:

1. Multiplexing: HTTP/2 allows multiple requests and responses to be sent over a single connection simultaneously, reducing latency and improving performance.

2. Header Compression: HTTP/2 uses HPACK compression for headers, reducing the overhead of redundant header information.

3. Server Push: HTTP/2 enables the server to proactively send resources to the client before they are requested, further improving performance.

4. Binary Framing: HTTP/2 uses a binary framing protocol, which is more efficient and less error-prone compared to the textual protocol used in HTTP/1.1.

Caddy takes advantage of these HTTP/2 features out of the box, providing improved performance and efficiency for your web applications.

It's important to note that HTTP/2 requires HTTPS. If you are serving traffic over plain HTTP (port 80), Caddy will use HTTP/1.1 for those connections. However, it is generally recommended to use HTTPS for all connections, not only for security reasons but also to take advantage of the benefits of HTTP/2.

If you want to explicitly disable HTTP/2 in Caddy for some reason, you can do so by adding the `http2 disable` directive to your Caddyfile:

```
:443 {
    # ...
    http2 disable
    # ...
}
```

However, disabling HTTP/2 is rarely necessary, and it is recommended to keep it enabled to leverage its performance benefits.
