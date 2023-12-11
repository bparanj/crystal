Securing Ruby on Rails API Endpoints with Supabase Magic Link Authentication in a Nuxt 3 Application

Integrating Supabase authentication with a Ruby on Rails backend to secure your API endpoints involves a few steps. The general idea is to use the token provided by Supabase when a user logs in with the magic link and then verify this token on your Rails backend. Here's how you can approach this:

### 1. **Frontend: Send the Supabase Auth Token**

When a user logs in using the magic link feature of Supabase in your Nuxt 3 app, Supabase provides an authentication token. You need to send this token to your Rails backend with each API request. This is typically done through an HTTP header.

In your Nuxt 3 app, after a successful login, you can access the user's session token using Supabase's JavaScript client and include it in the headers of your API requests:

```javascript
const { data, error } = await this.$supabase.auth.signInWithOtp({ email });

if (data) {
  const token = data.session.access_token;
  // Use this token in your API request headers
}
```

When making an API request, include the token in the Authorization header:

```javascript
fetch('https://your-rails-api-endpoint.com/data', {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  method: 'GET',
  // other settings...
});
```

### 2. **Backend: Verify the Token in Rails**

On your Rails backend, you need to verify the Supabase token for each protected API request. You can do this by decoding the JWT (JSON Web Token) sent from the frontend and validating it against the public key from Supabase.

- First, install a JWT decoding library in your Rails application, such as the [`jwt` gem](https://github.com/jwt/ruby-jwt).

  Add to your Gemfile:
  ```ruby
  gem 'jwt'
  ```

  And then run `bundle install`.

- Create a middleware or a before action in your Rails controller to authenticate API requests:

  ```ruby
  class ApiAuthentication
    def initialize(app)
      @app = app
    end

    def call(env)
      begin
        auth_header = env['HTTP_AUTHORIZATION']
        token = auth_header.split(' ').last
        decoded_token = JWT.decode(token, supabase_public_key, true, { algorithm: 'RS256' })
        
        # Continue the request
        @app.call(env)
      rescue
        # Handle the error, e.g., return an unauthorized status
        [401, {'Content-Type' => 'text/plain'}, ['Unauthorized']]
      end
    end

    private

    def supabase_public_key
      # Fetch the public key from Supabase or store it in your environment variables
    end
  end
  ```

- Register this middleware in your Rails application.

### 3. **Handling CORS**

Ensure your Rails backend is configured to handle Cross-Origin Resource Sharing (CORS) requests since your Nuxt.js frontend will be making requests from a different origin. You can use the [`rack-cors` gem](https://github.com/cyu/rack-cors) for this.

### 4. **Environment Variables**

- Store the Supabase public key and other sensitive details in environment variables instead of hardcoding them in your application.

### 5. **Secure Communication**

- Always use HTTPS to ensure the security of data transmitted between the frontend and backend.

By following these steps, you can secure your Ruby on Rails API endpoints to ensure that only logged-in users (authenticated via Supabase in your Nuxt.js frontend) can access them. This setup leverages the JWT token provided by Supabase to maintain a secure and consistent authentication flow between your frontend and backend.