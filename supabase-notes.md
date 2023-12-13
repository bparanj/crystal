## URL Details

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

