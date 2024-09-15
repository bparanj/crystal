To verify that Caddy has enabled HTTP/2, you can use various methods,  browser developer tools, command-line tools like `curl`, or online tools. HTTP/2 is designed to improve the efficiency, speed, and security of web server communications. Since Caddy automatically enables HTTP/2 for HTTPS sites (where the protocol is supported and enabled by default), verifying its activation is straightforward.

### Using Browser Developer Tools

1. **Open your website** in a web browser that supports HTTP/2 (most modern browsers do).
2. **Open the Developer Tools**. You can usually do this by right-clicking on the page and selecting "Inspect" or "Inspect Element", or by pressing `F12` or `Ctrl+Shift+I` (Cmd+Option+I on Mac).
3. **Go to the Network tab** and reload your website to capture the network requests.
4. **Click on any request** made to your Caddy server,  the initial document request.
5. **Look for the Protocol column** or in the headers section for the selected request. You might need to enable the Protocol column in some browsers by right-clicking on the column headers and selecting "Protocol" from the list.
6. Verify that the protocol is listed as **HTTP/2**.

### Using Curl

`curl` is a command-line tool used for transferring data with URLs. To check for HTTP/2 support:

1. Open a terminal.
2. Run the following command, replacing `yourwebsite.com` with your site's URL:

   ```sh
   curl -I --http2 https://yourwebsite.com
   ```

3. Look for a line starting with `HTTP/2 200` in the response, which indicates that the server supports HTTP/2 and the connection was successful.

### Using Online Tools

Several online tools can test for HTTP/2 support, such as [HTTP/2 Test](https://tools.keycdn.com/http2-test) or [SSL Labs' SSL Test](https://www.ssllabs.com/ssltest/). These tools provide detailed reports about your website's SSL/TLS configuration and HTTP/2 support. Simply enter your website's URL, and the tool will test and report whether HTTP/2 is enabled.

### Verifying Directly from Caddy

You can also check Caddy's configuration or logs for indications that HTTP/2 is enabled. Caddy's default behavior is to enable HTTP/2 for all HTTPS sites, but checking the configuration or logs can provide explicit confirmation.

- **Configuration**: Ensure there's no configuration explicitly disabling HTTP/2 in your Caddyfile.
- **Logs**: Caddy's logs may provide information about the protocols used for connections. You can check the logs for mentions of HTTP/2.

### Key Takeaway

Verifying HTTP/2 support in Caddy can be done through browser inspection, command-line tools, or online services. Since Caddy enables HTTP/2 by default for HTTPS connections, most Caddy-served sites should support HTTP/2 unless explicitly disabled.
