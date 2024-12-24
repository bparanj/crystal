Nginx offers several modules for performing authentication checks. Here are some of the most commonly used ones:

1. **ngx_http_auth_basic_module**: This module allows you to limit access to resources using HTTP Basic Authentication. It validates the username and password provided by the client³.

    ```nginx
    location /secure {
        auth_basic "Restricted Area";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
    ```

2. **ngx_http_auth_request_module**: This module enables client authorization based on the result of a subrequest. If the subrequest returns a 2xx response code, access is allowed⁴.

    ```nginx
    location / {
        auth_request /auth;
    }

    location = /auth {
        proxy_pass http://auth-server;
    }
    ```

3. **ngx_http_auth_jwt_module**: This module allows for JSON Web Token (JWT) authentication. It verifies the JWT provided by the client and grants access based on the token's validity³.

4. **Third-Party Modules**: There are also third-party modules like `ngx_http_auth_pam_module` for PAM authentication and `ngx_http_auth_ldap_module` for LDAP authentication.
