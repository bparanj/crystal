Securing sensitive credentials using environment variables is crucial in any web application. In Nuxt.js, you can manage these variables using a `.env` file and access them safely in your code. Here's how to do it for your Supabase integration:

### 1. **Setting Up Environment Variables**

1. **Create a `.env` File**: In the root of your Nuxt.js project, create a file named `.env`.

2. **Add Supabase Credentials**:
   
   Open the `.env` file and add your Supabase URL and anon key. Make sure not to commit this file to your version control system (e.g., Git).

   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_ANON_KEY=your_supabase_anon_key
   ```

3. **Update `.gitignore`**:

   Ensure that your `.env` file is listed in your `.gitignore` file to prevent it from being committed to your Git repository.

   ```
   .env
   ```

### 2. **Configuring Nuxt.js to Use Environment Variables**

1. **Install `@nuxtjs/dotenv`** (if Nuxt version < 2.13):

   For older versions of Nuxt.js, you might need to install a package to handle environment variables:

   ```bash
   npm install @nuxtjs/dotenv
   ```

   And register it in your `nuxt.config.js`:

   ```javascript
   modules: [
     '@nuxtjs/dotenv'
   ],
   ```

   For Nuxt.js 2.13 and later, you don't need to install this package as Nuxt.js can automatically read `.env` files.

2. **Access Environment Variables in Nuxt.js**:

   Modify your Supabase initialization (`plugins/supabaseClient.js`) to use the environment variables:

   ```javascript
   import { createClient } from '@supabase/supabase-js'

   const supabaseUrl = process.env.SUPABASE_URL;
   const supabaseAnonKey = process.env.SUPABASE_ANON_KEY;

   export const supabase = createClient(supabaseUrl, supabaseAnonKey)
   ```

### 3. **Using Environment Variables in Components**

When you need to use these variables in your components, you can access them directly using `process.env`. For instance, in your login method:

```javascript
async loginWithEmail() {
  let { data, error } = await this.$supabase.auth.signInWithOtp({
    email: this.email
  })
  if (error) console.log('Error:', error.message);
  else console.log('Magic link sent to your email!');
}
```

In this example, `this.$supabase` is already configured with your environment variables, so no additional changes are needed in the component.

### 4. **Deploy and Test**

- When deploying, make sure to set these environment variables in your deployment environment. For example, if you are using Vercel, Netlify, or similar platforms, they provide ways to set environment variables through their dashboard.

### Security Note

- **Do Not Expose Sensitive Information**: Never expose sensitive keys or credentials in your client-side code. Supabase anon key is intended for client-side use but ensure that other sensitive keys (like service role keys) are kept secure and not exposed in the frontend.

By following these steps, you'll securely integrate Supabase with your Nuxt.js application using environment variables, protecting sensitive information effectively.