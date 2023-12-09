To implement the "Login With Magic Link" feature using Supabase in a Nuxt.js app, you'll need to follow a series of steps. This process involves setting up Supabase for authentication and integrating it with your Nuxt.js application. Here's a simplified guide:

### 1. Set Up Supabase Project

1. **Create a Supabase Account**: Go to the [Supabase website](https://supabase.io/) and sign up or log in.
2. **Create a New Project**: Fill in the details like project name, database password, and region.
3. **Retrieve API Keys**: Once the project is set up, note down the `URL` and `anon public` API keys from the project's API settings.

### 2. Initialize Supabase in Nuxt.js

1. **Install Supabase**: In your Nuxt.js project, run:

   ```bash
   npm install @supabase/supabase-js
   ```

2. **Initialize Supabase**: Create a file, e.g., `supabaseClient.js` in your `plugins` directory:

   ```javascript
   import { createClient } from '@supabase/supabase-js'

   const supabaseUrl = 'YOUR_SUPABASE_URL';
   const supabaseAnonKey = 'YOUR_SUPABASE_ANON_KEY';

   export const supabase = createClient(supabaseUrl, supabaseAnonKey)
   ```

3. **Configure Nuxt**: Update `nuxt.config.js` to include the plugin:

   ```javascript
   export default {
     plugins: ['~/plugins/supabaseClient.js'],
   }
   ```

### 3. Implement Magic Link Authentication

1. **Create a Login Page**: Create a new page for login (e.g., `login.vue`) in your `pages` directory.
2. **Set Up a Form**: Include an input field for the email address and a button to send the magic link.

   ```html
   <template>
     <div>
       <input v-model="email" type="email" placeholder="Your email" />
       <button @click="loginWithEmail">Send Magic Link</button>
     </div>
   </template>

   <script>
   export default {
     data() {
       return {
         email: '',
       }
     },
     methods: {
       async loginWithEmail() {
         const { error } = await this.$supabase.auth.signIn({
           email: this.email,
         })
         if (error) console.log('Error:', error.message);
         else console.log('Check your email for the login link!');
       }
     }
   }
   </script>
   ```

3. **Handle Magic Link**: When the user clicks the link in their email, they will be redirected to your site. You can handle this in the Nuxt.js `mounted` lifecycle hook or in a specific callback route.

### 4. Handling User Session

1. **Create a State**: In your store or component, create a state variable to hold the user's session data.
2. **Session Persistence**: Use the `onAuthStateChanged` method to check for the user's session.

   ```javascript
   mounted() {
     this.$supabase.auth.onAuthStateChange((event, session) => {
       if (session) {
         // User logged in, handle the session
         console.log('Session:', session)
       } else {
         // User logged out
       }
     })
   }
   ```

3. **Protect Routes**: You can use Nuxt's middleware to protect routes that require authentication.

### 5. Deploy and Test

1. **Deploy Your App**: Once everything is set up, deploy your Nuxt.js application.
2. **Test the Flow**: Test the magic link authentication by entering an email, receiving the link, and ensuring the login process works correctly.

### Additional Considerations

- **Security**: Always ensure you handle user data securely and comply with privacy laws.
- **Custom Domain for Emails**: Configure a custom email domain in Supabase for a more professional look.
- **User Experience**: Provide clear instructions and feedback during the login process.

By following these steps, you'll have implemented a "Login With Magic Link" feature in your Nuxt.js application using Supabase. This modern authentication method enhances security and user experience.