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

## Use Before Action Instead of Middleware

To convert your `ApiAuthentication` middleware into a `before_action` in the `ApplicationController` of a Ruby on Rails app, you can follow these steps. This will allow you to execute the authentication logic before each controller action:

1. **Remove the Middleware Class**: Since we are integrating the logic directly into the controller, the separate middleware class (`ApiAuthentication`) is no longer needed.

2. **Define a Private Method in ApplicationController**: Incorporate the authentication logic into a private method within `ApplicationController`.

3. **Use `before_action` to Invoke the Method**: Set up a `before_action` callback to call this method before each controller action.

Here's the updated `ApplicationController`:

```ruby
class ApplicationController < ActionController::API
  before_action :authenticate_request

  private

  def authenticate_request
    begin
      auth_header = request.headers['Authorization']
      token = auth_header.split(' ').last if auth_header
      decoded_token = JWT.decode(token, supabase_public_key, true, { algorithm: 'RS256' })

      # You might want to set a current_user or similar here, based on decoded_token
      # For example:
      # user_id = decoded_token[0]['sub']
      # @current_user = User.find(user_id)
      
      # If no exception is raised, the request continues normally
    rescue JWT::DecodeError
      render json: { errors: ['Not Authenticated'] }, status: :unauthorized
    end
  end

  def supabase_public_key
    # Fetch the public key from Supabase or store it in your environment variables
    ENV['SUPABASE_PUBLIC_KEY']
  end
end
```

In this setup:

- The `authenticate_request` method attempts to decode the JWT token from the `Authorization` header of the incoming request.
- If the token is invalid or absent, a `JWT::DecodeError` is raised, and the request is responded to with a `401 Unauthorized` status.
- You can modify the `rescue` block to handle other types of JWT exceptions as necessary.
- You can also set a `@current_user` or similar variable based on the decoded token, which can then be used in your controller actions.
- The `supabase_public_key` method fetches the public key, which you need to verify the JWT.

This approach centralizes your authentication logic and makes it easy to manage and apply across your application. Remember to handle any exceptions appropriately to ensure that unauthorized access is effectively prevented.
