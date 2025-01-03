## Vue Frontend + Go Backend

An example showing how to implement the serverless functions in Go for Vercel, using Vue.js on the frontend and Vercel KV (Upstash Redis) for persistence.

- Vercel KV is backed by Upstash Redis. To access it from Go, you’ll use the environment variables `VERCEL_REDIS_URL` and `VERCEL_REDIS_TOKEN`.
- You’ll write two serverless functions in Go: `api/save.go` and `api/load.go`.
- Each function starts an HTTP server and handles requests using `http.HandleFunc`. Vercel’s Go runtime will invoke this handler for each request.
- The frontend remains the same Vue.js application that calls `/api/save` and `/api/load`.

### Prerequisites

- Make sure the `VERCEL_REDIS_URL` and `VERCEL_REDIS_TOKEN` environment variables are set in your Vercel project (you can set them in the Vercel dashboard).
- Have Go installed locally for building and testing.
- Use the Redis Go client (e.g., `github.com/redis/go-redis/v9`).

### Project Structure

```
project/
  src/
    App.vue
    main.js
  public/
    index.html
  api/
    save.go
    load.go
  go.mod
  go.sum
  package.json
  vercel.json
```

### go.mod

Initialize a Go module:

```bash
go mod init example.com/project
go get github.com/redis/go-redis/v9
```

### `vercel.json`

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "installCommand": "npm install",
  "routes": [
    { "src": "/api/save", "dest": "api/save.go" },
    { "src": "/api/load", "dest": "api/load.go" },
    { "src": "/(.*)", "dest": "/index.html" }
  ]
}
```

The `vercel.json` file is created and maintained by the developer. It’s not automatically generated by Vercel. Instead, you add it to your project’s root directory to configure how Vercel builds and serves your application. By defining routes, redirects, environment variables, and other settings in `vercel.json`, you control aspects of the deployment process and runtime behavior on Vercel’s platform.

### Backend (Go Serverless Functions)

**Common Code for Redis Client (optional):**  
You can create a `redis.go` file in `api/` if you want to share code, or just inline it. For simplicity, we’ll inline it in each function.

**`api/save.go`:**
```go
package main

import (
	"encoding/json"
	"io"
	"log"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/redis/go-redis/v9"
	"golang.org/x/net/context"
)

type saveRequest struct {
	Text string `json:"text"`
}

type saveResponse struct {
	Code string `json:"code"`
}

func main() {
	// Prepare Redis client
	redisURL := os.Getenv("VERCEL_REDIS_URL")
	redisToken := os.Getenv("VERCEL_REDIS_TOKEN")
	if redisURL == "" || redisToken == "" {
		log.Fatal("Redis environment variables not set")
	}

	opt, err := redis.ParseURL(redisURL)
	if err != nil {
		log.Fatal(err)
	}
	opt.Password = redisToken
	rdb := redis.NewClient(opt)

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			w.WriteHeader(http.StatusMethodNotAllowed)
			json.NewEncoder(w).Encode(map[string]string{"error": "Method not allowed"})
			return
		}

		body, err := io.ReadAll(r.Body)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": "Invalid body"})
			return
		}

		var req saveRequest
		if err := json.Unmarshal(body, &req); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": "Invalid JSON"})
			return
		}

		text := req.Text
		if len(text) == 0 {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": "Empty text"})
			return
		}

		rand.Seed(time.Now().UnixNano())
		code := strconv.Itoa(rand.Intn(9000) + 1000)

		ctx := context.Background()
		if err := rdb.Set(ctx, code, text, 0).Err(); err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(map[string]string{"error": "Could not store document"})
			return
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(saveResponse{Code: code})
	})

	log.Fatal(http.ListenAndServe(":3000", nil))
}
```

**`api/load.go`:**

```go
package main

import (
	"context"
	"encoding/json"
	"log"
	"net/http"
	"os"

	"github.com/redis/go-redis/v9"
)

func main() {
	redisURL := os.Getenv("VERCEL_REDIS_URL")
	redisToken := os.Getenv("VERCEL_REDIS_TOKEN")
	if redisURL == "" || redisToken == "" {
		log.Fatal("Redis environment variables not set")
	}

	opt, err := redis.ParseURL(redisURL)
	if err != nil {
		log.Fatal(err)
	}
	opt.Password = redisToken
	rdb := redis.NewClient(opt)

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		code := r.URL.Query().Get("code")
		if len(code) != 4 {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": "Invalid code"})
			return
		}

		ctx := context.Background()
		text, err := rdb.Get(ctx, code).Result()
		if err == redis.Nil {
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(map[string]string{"error": "Document not found"})
			return
		} else if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(map[string]string{"error": "Could not load document"})
			return
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(map[string]string{"text": text})
	})

	log.Fatal(http.ListenAndServe(":3000", nil))
}
```

### Frontend

The frontend code communicates with `/api/save` and `/api/load`.

**`src/App.vue`**:

```vue
<template>
  <div style="max-width:600px; margin:20px auto; font-family:Arial,sans-serif;">
    <h1>Document Sharing with Vercel KV (Go backend)</h1>

    <section style="margin-bottom:30px;">
      <h2>Create a Document</h2>
      <textarea v-model="inputText" rows="10" cols="50" placeholder="Enter your document text..."></textarea>
      <br><br>
      <button @click="saveDocument">Save Document</button>
      <p>{{ saveMessage }}</p>
    </section>

    <section>
      <h2>Load a Document</h2>
      <input type="text" v-model="loadCode" placeholder="4-digit code" maxlength="4" />
      <button @click="loadDocument">Load Document</button>
      <div v-if="loadedText">
        <h3>Document Content:</h3>
        <pre>{{ loadedText }}</pre>
      </div>
      <p v-else-if="loadMessage">{{ loadMessage }}</p>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const inputText = ref('')
const saveMessage = ref('')
const loadCode = ref('')
const loadMessage = ref('')
const loadedText = ref('')

async function saveDocument() {
  const text = inputText.value.trim()
  if (!text) {
    saveMessage.value = "Please enter some text before saving."
    return
  }

  try {
    const res = await fetch('/api/save', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ text })
    })
    const data = await res.json()
    if (res.ok) {
      saveMessage.value = "Document saved! Your code: " + data.code
      inputText.value = ''
    } else {
      saveMessage.value = "Error: " + (data.error || 'Unknown error')
    }
  } catch (err) {
    saveMessage.value = "Network error: " + err.message
  }
}

async function loadDocument() {
  loadedText.value = ''
  loadMessage.value = ''
  const code = loadCode.value.trim()

  if (code.length !== 4 || isNaN(code)) {
    loadMessage.value = "Please enter a valid 4-digit code."
    return
  }

  try {
    const res = await fetch('/api/load?code=' + encodeURIComponent(code))
    const data = await res.json()
    if (res.ok) {
      loadedText.value = data.text
    } else {
      loadMessage.value = "Error: " + (data.error || 'Unknown error')
    }
  } catch (err) {
    loadMessage.value = "Network error: " + err.message
  }
}
</script>
```

### Build and Deploy

1. Build the Vue app:
   ```bash
   npm run build
   ```
   This creates a `dist` folder.

2. Deploy to Vercel:
   ```bash
   vercel
   ```
   Vercel detects the static build and Go functions. Make sure your `VERCEL_REDIS_URL` and `VERCEL_REDIS_TOKEN` are configured in the project’s environment variables on Vercel.

### Notes

- Vercel’s Go runtime will run your Go programs as serverless functions. You need to ensure the code is written to listen on `:3000` and handle requests as shown.
- The KV store is accessed via Upstash Redis credentials.
- This approach moves the backend logic to Go.

## Vue Frontend + Node Backend 

An example of how to rewrite the file sharing program using Vue.js for the frontend and Vercel KV for persistence in the backend. This setup allows you to store and retrieve documents by their generated 4-digit code. The code will run on Vercel, using serverless functions for the API routes and the KV store for persistence.

### Overview

- **Frontend (Vue.js):** A simple SPA where users can create documents and retrieve them by entering a 4-digit code.
- **Backend (Serverless Functions on Vercel):** Two endpoints:
  - `api/save`: Accepts text, generates a 4-digit code, and stores the text in Vercel KV.
  - `api/load`: Given a code, retrieves the stored text from Vercel KV.

### Prerequisites

- A Vercel account.
- Install Vercel CLI: `npm i -g vercel`
- Vercel KV enabled on your account.

### Project Structure

```
project/
  src/
    App.vue
    main.js
  public/
    index.html
  api/
    save.js
    load.js
  package.json
  vercel.json
```

### `vercel.json`

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "installCommand": "npm install",
  "routes": [
    { "src": "/api/save", "dest": "api/save.js" },
    { "src": "/api/load", "dest": "api/load.js" },
    { "src": "/(.*)", "dest": "/index.html" }
  ]
}
```

This configuration rewrites API calls to the serverless functions and serves the built Vue app for all other routes.

### Backend (Serverless Functions)

**Install Vercel KV package:**
```bash
npm install @vercel/kv
```

**`api/save.js`:**
```js
import { kv } from '@vercel/kv'

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  let body = ''
  await new Promise((resolve) => {
    req.on('data', chunk => body += chunk)
    req.on('end', resolve)
  })

  const data = JSON.parse(body)
  const text = (data.text || '').trim()

  if (!text) {
    return res.status(400).json({ error: 'Empty text' })
  }

  const code = String(Math.floor(Math.random() * 9000) + 1000)
  await kv.set(code, text)
  return res.status(200).json({ code })
}
```

**`api/load.js`:**
```js
import { kv } from '@vercel/kv'

export default async function handler(req, res) {
  const { query } = req
  const code = query.code

  if (!code || code.length !== 4) {
    return res.status(400).json({ error: 'Invalid code' })
  }

  const doc = await kv.get(code)
  if (!doc) {
    return res.status(404).json({ error: 'Document not found' })
  }

  return res.status(200).json({ text: doc })
}
```

### Frontend

**Install Vue and Vite:**
```bash
npm create vite@latest my-vue-app --template vue
cd my-vue-app
npm install
```

Move `api` and `vercel.json` files into this project’s root directory.

**`src/App.vue`:**

```vue
<template>
  <div style="max-width:600px; margin:20px auto; font-family:Arial,sans-serif;">
    <h1>Document Sharing with Vercel KV</h1>

    <section style="margin-bottom:30px;">
      <h2>Create a Document</h2>
      <textarea v-model="inputText" rows="10" cols="50" placeholder="Enter your document text..."></textarea>
      <br><br>
      <button @click="saveDocument">Save Document</button>
      <p>{{ saveMessage }}</p>
    </section>

    <section>
      <h2>Load a Document</h2>
      <input type="text" v-model="loadCode" placeholder="4-digit code" maxlength="4" />
      <button @click="loadDocument">Load Document</button>
      <div v-if="loadedText">
        <h3>Document Content:</h3>
        <pre>{{ loadedText }}</pre>
      </div>
      <p v-else-if="loadMessage">{{ loadMessage }}</p>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const inputText = ref('')
const saveMessage = ref('')
const loadCode = ref('')
const loadMessage = ref('')
const loadedText = ref('')

async function saveDocument() {
  const text = inputText.value.trim()
  if (!text) {
    saveMessage.value = "Please enter some text before saving."
    return
  }

  try {
    const res = await fetch('/api/save', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ text })
    })
    const data = await res.json()
    if (res.ok) {
      saveMessage.value = "Document saved! Your code: " + data.code
      inputText.value = ''
    } else {
      saveMessage.value = "Error: " + (data.error || 'Unknown error')
    }
  } catch (err) {
    saveMessage.value = "Network error: " + err.message
  }
}

async function loadDocument() {
  loadedText.value = ''
  loadMessage.value = ''
  const code = loadCode.value.trim()

  if (code.length !== 4 || isNaN(code)) {
    loadMessage.value = "Please enter a valid 4-digit code."
    return
  }

  try {
    const res = await fetch('/api/load?code=' + encodeURIComponent(code))
    const data = await res.json()
    if (res.ok) {
      loadedText.value = data.text
    } else {
      loadMessage.value = "Error: " + (data.error || 'Unknown error')
    }
  } catch (err) {
    loadMessage.value = "Network error: " + err.message
  }
}
</script>
```

**`src/main.js`:**
```js
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

**`public/index.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Document Sharing</title>
</head>
<body>
  <div id="app"></div>
  <!-- Vite will inject built assets here after npm run build -->
</body>
</html>
```

### Build and Deploy

1. Build the Vue app:
   ```bash
   npm run build
   ```
   This creates a `dist` folder with your compiled app.

2. Deploy to Vercel:
   ```bash
   vercel
   ```
   Follow the prompts. Vercel will:
   - Serve `dist` folder as static content.
   - Serve `api/save.js` and `api/load.js` as serverless functions.
   - Use Vercel KV to store and retrieve documents by code.

Vercel KV is a managed key-value store. The data you store with `kv.set()` will persist and be accessible as long as you have Vercel KV configured. This allows your documents to remain available across deployments and requests, unlike in-memory or ephemeral storage solutions.
