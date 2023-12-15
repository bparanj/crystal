
Instructions to get Supabase magic link to work with Nuxt.

## Pre-Requisites

Node version: v21.2.0
NPM version: 10.2.4

## Steps

1. Create a Nuxt.js project

```js
npx nuxi@latest init zea
```

2. Install the dependencies and run the development server:

```
cd zea
npm install
npm run dev -- -o
```

3. Setup Home and Login tabs [Nuxt Tabs](./nuxt-links.md)

4. [Setup Supabase](./supabase-setup.md)

5. Set Site URL to http://localhost:3000/auth in Supabase URL Configuration tab under Authentication. 

6. Setup SPA, turn off the ssr flag (SPA Setup)(./spa-setup.md)

5. Setup [Environment Variables](./env-variables.md) for Supabase client.

6. Setup [Supabase client plugin](./plugin.md)

7. Run the app and test the passwordless login feature.

8. After the user clicks the magic link sent to their email, handle [Auth Callback](auth-callback.md) [Integrating with Rails Backend](./integrating-with-backend.md)

9. Protect the [member area](./protected-pages.md)

- Identify users in the backend: [Save User Profile](identify-users-backend.md)
- How will the Rails backend know that the user is already logged in using Supabase? See [Securing Rails API](./securing-rails-api.md) [Rails Backend](./supabase-rails.md)

## Troubleshooting

- [Errors and Resolution](./troubleshooting.md)