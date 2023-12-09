
Initialize

```js
import { createClient } from '@supabase/supabase-js'
const supabaseUrl = 'https://uvjlmwflhjajykozmvca.supabase.co'
const supabaseKey = process.env.SUPABASE_KEY
const supabase = createClient(supabaseUrl, supabaseKey)
```

Client API Keys

const SUPABASE_KEY = 'SUPABASE_CLIENT_API_KEY'


const SUPABASE_URL = "https://uvjlmwflhjajykozmvca.supabase.co"
const supabase = createClient(SUPABASE_URL, process.env.SUPABASE_KEY);

Log In With Magic Link Via Email

let { data, error } = await supabase.auth.signInWithOtp({
  email: 'someone@email.com'
})
