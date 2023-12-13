In Nuxt, handling the authentication callback with Supabase can be achieved in a similar way, but you'll typically integrate it within the Nuxt context and use Nuxt-specific hooks and methods. Here's how you can adapt your Vue component script to a Nuxt environment:

### Step 1: Create a Supabase Plugin (if not already created)

First, ensure you have a Supabase plugin set up in your Nuxt project. This plugin initializes the Supabase client and makes it available throughout your application.

Create a file named `supabaseClient.js` in the `plugins` directory:

```javascript
// plugins/supabaseClient.js
import { defineNuxtPlugin } from 'nuxt/app';
import { createClient } from '@supabase/supabase-js';

export default defineNuxtPlugin(nuxtApp => {
  const supabaseUrl = process.env.PUBLIC_SUPABASE_URL;
  const supabaseAnonKey = process.env.PUBLIC_SUPABASE_ANON_KEY;

  const supabase = createClient(supabaseUrl, supabaseAnonKey);

  nuxtApp.provide('supabase', supabase);
});
```

In your `nuxt.config.js`, include the plugin:

```javascript
// nuxt.config.js
export default defineNuxtConfig({
  plugins: ['~/plugins/supabaseClient.js'],
  // ... other configurations
});
```

### Step 2: Handle Auth State Change in Nuxt

In a Nuxt page or component, you can handle the authentication state change like this:

```vue
<script setup>
import { useNuxtApp, onMounted } from '#app';

const { $supabase } = useNuxtApp();

onMounted(() => {
  $supabase.auth.onAuthStateChange((event, session) => {
    if (event === 'SIGNED_IN') {
      console.log('User signed in!', session.user);
      // Redirect or fetch user data
      // For redirecting in Nuxt, you might use `useRouter` from 'vue-router'
    }
    if (event === 'SIGNED_OUT') {
      console.log('User signed out!');
      // Handle sign out
    }
  });
});
</script>
```

### Additional Considerations:

1. **Routing**: For redirecting users after login or logout, use Nuxt's `useRouter`:

   ```javascript
   const router = useRouter();
   router.push('/dashboard'); // Redirect to dashboard after login
   ```

2. **Global State**: Consider using a store (like Pinia or Vuex) if you need to manage the user's authentication state globally.

3. **Server-Side Rendering**: If you're using Nuxt in SSR mode, make sure that the Supabase auth state change listener is only added in client-side code to avoid SSR issues.

By following these steps, you can effectively integrate Supabase's authentication state handling into your Nuxt application.