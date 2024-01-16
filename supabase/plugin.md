## 1. Set Up Supabase Project

See [magic-link](./magic-link.md)

## 2. Initialize Supabase in Nuxt.js
See [magic-link](./magic-link.md)


Create supabaseClient.js in plugins directory.

```javascript
import { defineNuxtPlugin } from '#app';
import { createClient } from '@supabase/supabase-js';

export default defineNuxtPlugin((nuxtApp) => {
	const runtimeConfig = useRuntimeConfig()	
  const supabase = createClient(runtimeConfig.public.supabaseUrl, runtimeConfig.public.supabaseAnonKey);

  return {
    provide: {
      supabase: supabase
    }
  };
});
```

## Register the Plugin

To register a new plugin in your Nuxt.js configuration file (`nuxt.config.ts`), add a `plugins` array to the configuration object.

```javascript
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
	ssr: false,
	plugins: ['~/plugins/supabaseClient.js'],
  runtimeConfig: {
	    // The private keys which are only available within server-side
	    apiSecret: '123',
	    // Keys within public, will be also exposed to the client-side
	    public: {
	      supabaseUrl: process.env.PUBLIC_SUPABASE_URL,
				supabaseAnonKey: process.env.PUBLIC_SUPABASE_ANON_KEY	
	    }
	  }	
})
```

## Create a Login Page

In pages/login.vue:

```javascript
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
        let { error } = await this.$supabase.auth.signInWithOtp({
          email: this.email
        })
        if (error) {
            console.log('Error:', error.message);
        }
        else {
            console.log('Magic link sent to your email!');
        }
      }
    }
  }
</script>
```
