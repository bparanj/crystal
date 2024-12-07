Below is an example Go program that uses the official Go Redis client to connect to the Vercel KV (Upstash Redis) instance using `VERCEL_REDIS_URL` and `VERCEL_REDIS_TOKEN`, sends a PING command, and checks for a PONG response. This ensures that not only are the environment variables correct, but the connection to Redis is functional.

**Prerequisites:**
- Add the Go Redis client library to your project:
  ```bash
  go get github.com/redis/go-redis/v9
  ```

**Example Code (`main.go`):**
```go
package main

import (
	"context"
	"fmt"
	"net/http"
	"os"

	"github.com/redis/go-redis/v9"
)

func handler(w http.ResponseWriter, r *http.Request) {
	redisURL := os.Getenv("VERCEL_REDIS_URL")
	redisToken := os.Getenv("VERCEL_REDIS_TOKEN")

	if redisURL == "" || redisToken == "" {
		http.Error(w, "Missing VERCEL_REDIS_URL or VERCEL_REDIS_TOKEN environment variables.", http.StatusInternalServerError)
		return
	}

	// Parse the provided Redis URL
	opt, err := redis.ParseURL(redisURL)
	if err != nil {
		http.Error(w, fmt.Sprintf("Failed to parse Redis URL: %v", err), http.StatusInternalServerError)
		return
	}

	// Set the token as password for Upstash Redis
	opt.Password = redisToken

	// Create the Redis client
	client := redis.NewClient(opt)
	defer client.Close()

	ctx := context.Background()

	// Send PING to check connectivity and authentication
	pong, err := client.Ping(ctx).Result()
	if err != nil {
		http.Error(w, fmt.Sprintf("Redis PING failed: %v", err), http.StatusInternalServerError)
		return
	}

	// If we got PONG, then environment variables and connection are correct
	fmt.Fprintf(w, "Successfully connected to Redis!\nPING -> %s\n", pong)
}

func main() {
	http.HandleFunc("/", handler)
	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}
	fmt.Printf("Listening on port %s...\n", port)
	http.ListenAndServe(":"+port, nil)
}
```

**What This Does:**
- Reads `VERCEL_REDIS_URL` and `VERCEL_REDIS_TOKEN` from environment variables.
- Uses the `go-redis` library to create a Redis client configured with the given URL and token.
- Sends a PING command to verify connectivity and authentication.
- Prints "Successfully connected to Redis!" and the PONG response if successful.
- Returns an error otherwise.

**How to Verify:**
1. Ensure `VERCEL_REDIS_URL` and `VERCEL_REDIS_TOKEN` are set in your Vercel project settings.
2. Deploy this code to Vercel.
3. Access the deployed URL.  
   - If successful, you’ll see a message that includes “PING -> PONG”.
   - If there’s an error, it will be printed on the page.

This approach ensures that the environment variables are correct, the connection is established, and that basic Redis commands work as expected.
