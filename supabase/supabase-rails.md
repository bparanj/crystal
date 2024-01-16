In your scenario, where Supabase is used solely for authentication and you have a separate Rails backend for application-related APIs, the process of distinguishing new users from existing ones involves coordination between Supabase and your Rails backend. Here's a general workflow:

1. **User Authentication with Supabase**:
   - Users authenticate via Supabase using Magic Link.
   - Once authenticated, Supabase provides a JWT (JSON Web Token) or some form of authentication token.

2. **Token Verification in Rails Backend**:
   - When the user is redirected back to your application after authentication, your Rails backend should verify the Supabase token.
   - Implement a middleware or a similar mechanism in Rails to decode and verify the JWT from Supabase to ensure the authenticity of the request.

3. **Check User Existence in Rails Database**:
   - Once the token is verified, extract the user's unique identifier (like an email or user ID) from the token.
   - Check in your Rails application's database to see if a user with this identifier already exists.
   - If the user exists, they are an existing user. If not, they are a new user.

4. **Handling New Users**:
   - For new users, create a corresponding user record in your Rails application's database. You can store additional user-related information here.
   - You might want to trigger additional onboarding processes or initial setup flows for new users at this point.

5. **API Interaction**:
   - For subsequent API requests, the frontend should send the Supabase token along with the request.
   - Your Rails backend should validate this token for each API call to ensure that the request is authenticated.

6. **Synchronizing User Data (Optional)**:
   - If needed, you can synchronize user data between Supabase and your Rails backend periodically or based on certain triggers.
   - This might involve updating user profiles, preferences, or any other relevant data.

7. **Security and Privacy Considerations**:
   - Ensure that the token exchange and user data handling are secure.
   - Follow best practices for JWT validation and user data management.

This approach allows you to leverage Supabase for user authentication while maintaining your application's core data and logic in your Rails backend. It requires careful handling of authentication tokens and user data synchronization to ensure a seamless and secure user experience.