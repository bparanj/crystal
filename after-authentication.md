
emailRedirectTo

The emailRedirectTo parameter is used to specify where to redirect the user to after authentication when using passwordless sign-ins or third-party providers. By default, the user will be redirected to the SITE_URL, but you can modify the SITE_URL or add additional redirect URLs to the allow list. Once you've added necessary URLs to the allow list, you can specify the URL you want the user to be redirected to in the emailRedirectTo parameter.

Here is an example of using emailRedirectTo with the signUp function:

```js
supabase.auth.signUp({
  email: 'jon@example.com',
  password: 'sup3rs3cur3',
  options: {
    emailRedirectTo: 'http://localhost:3000/auth/callback',
  },
})
```

If you intend to use server-side rendering, you might want the email link to redirect the user to a server-side endpoint to check if they are authenticated before returning the page. However, the default email link will redirect the user after verification to the redirect URL with the session in the query fragments. Since the session is returned in the query fragments by default, you won't be able to access it on the server-side.

You can customize the email link in the email template to redirect the user to a server-side endpoint successfully. For example:

```html
<a href="https://api.example.com/v1/authenticate?token_hash={{ .TokenHash }}&type=invite&redirect_to={{ .RedirectTo }}"
    >Accept the invite
  </a>
```

When the user clicks on the link, the request will hit https://api.example.com/v1/authenticate and you can grab the token_hash, type and redirect_to query parameters from the URL. Then, you can call the verifyOtp method to get back an authenticated session before redirecting the user back to the client. Since the verifyOtp method makes a POST request to Supabase Auth to verify the user, the session will be returned in the response body, which can be read by the server. For example:

```
const { token_hash, type } = Object.fromEntries(new URLSearchParams(window.location.search))
const { data: { session }, error } = await supabase.auth.verifyOtp({ token_hash, type })

// subsequently redirect the user back to the client using the redirect_to param
// ...
```

If you are being redirected to the wrong URL when using the redirectTo option, you must set the exact URL in the Redirect URL's setting. For more information on formats for redirect URL settings, see the documentation here: https://supabase.com/docs/guides/auth/overview#redirect-urls-and-wildcards

How to retrieve the user session on the client side after the user clicks on the email for siginwithOTP call in supabase?

After a user clicks on the magic link in their email for the `signInWithOtp` call with Supabase, you can retrieve the user session on the client side by listening for changes in the authentication state. Supabase provides a way to detect when a user's authentication state changes, which includes when they log in via a magic link.

Here’s how you can handle it in a typical client-side application (like a Nuxt.js SPA):

### 1. **Set Up an Auth State Change Listener**

When your application initializes, set up a listener to detect changes in the authentication state. This can be done in your main app component or a dedicated authentication component.

For example, in a Vue component:

```javascript
<script setup>
import { onMounted } from 'vue';
import { useSupabase } from 'path/to/your/supabaseClient';

const supabase = useSupabase();

onMounted(() => {
  supabase.auth.onAuthStateChange((event, session) => {
    if (event === 'SIGNED_IN') {
      console.log('User signed in!', session.user);
      // Handle the logged-in user, e.g., redirect or fetch user data
    }
    if (event === 'SIGNED_OUT') {
      console.log('User signed out!');
      // Handle sign out
    }
  });
});
</script>
```

In this example, `useSupabase` is a hypothetical utility to get the Supabase client instance. Replace it with how you actually access your Supabase client in your app.

### 2. **Handling the Auth State in Nuxt.js**

If you're using Nuxt.js, consider setting up the listener in a layout or page where it makes the most sense for your application, like in a layout that wraps around all your pages.

### 3. **Store the User Session**

Upon successful sign-in, you might want to store the user session (or relevant parts of it) in your application's state, like in a Vuex store, Pinia store, or a reactive Vue variable. This allows you to access the user information across your application.

### 4. **Redirect or Update UI**

Once you detect that the user is signed in, you may want to redirect them to a specific route in your application or update the UI to reflect their signed-in status.

### 5. **Handle Page Refreshes**

Remember that if the page is refreshed, you'll need to check if the user is still logged in. Supabase provides methods to retrieve the current session, which can be used to check the user's sign-in status on page load.

```javascript
const currentSession = supabase.auth.session();
if (currentSession) {
  // User is signed in
}
```

### 6. **Security Considerations**

Always handle user data securely and ensure that sensitive information is not exposed to the client side more than necessary.

By following these steps, you can effectively retrieve and manage the user session in your client-side application after the user authenticates using the magic link from Supabase.
