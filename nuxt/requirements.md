## High Level Requirements

- Setup SPA frontend using Nuxt
- Setup backend using Rails
- Setup Supabase for magic link authentication
- Setup NuxtUI for styling
- Protect pages with middleware

### How to hide the credentials on the frontend?

Only PUBLIC_ variables are exposed to the client. These are not sensitive and exposed to the client only. The environment variables related to Supabase:

PUBLIC_SUPABASE_URL
PUBLIC_SUPABASE_ANON_KEY

are safe. The db password: 

SUPABASE_DB_PASSWORD

should not be prefixed with PUBLIC and should not be stored in Git.
