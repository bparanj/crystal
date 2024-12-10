Steps to create a basic “Hello World” application in Go:

**Prerequisites:**
- [Install Go](https://go.dev/dl/) if you haven’t already, and ensure it’s in your system’s PATH.  
- Run `go version` in your terminal to confirm that Go is installed correctly.

**Steps:**

1. **Create a Project Directory:**
   Choose a directory where you’d like to store your Go code.
   ```bash
   mkdir hello-go
   cd hello-go
   ```

2. **Initialize a Go Module:**
   A Go module helps manage dependencies and code organization. Run:
   ```bash
   go mod init example.com/hello-go
   ```
   Replace `example.com/hello-go` with any module path (it could be something like `github.com/<your-username>/hello-go`). This command creates a `go.mod` file.

3. **Create a Go Source File:**
   Inside your project directory, create a file named `main.go`:
   ```bash
   touch main.go
   ```
   Open `main.go` in your favorite text editor and add:
   ```go
   package main

   import "fmt"

   func main() {
       fmt.Println("Hello, World!")
   }
   ```

   - `package main`: Defines the main package, which tells Go this is an executable program.
   - `func main()`: The `main` function is the entry point of a Go program.
   - `fmt.Println("Hello, World!")`: Prints “Hello, World!” to the console.

4. **Build the Application (Optional):**
   You can compile the application by running:
   ```bash
   go build
   ```
   This creates an executable named `hello-go` (on Linux/Mac) or `hello-go.exe` (on Windows). Running this executable will print “Hello, World!”.
   
   Alternatively, you can skip build and just run the code directly.

5. **Run the Application:**
   ```bash
   go run main.go
   ```
   The output should be:
   ```
   Hello, World!
   ```

**Summary:**

- You created a directory for your project.
- Initialized a Go module.
- Wrote a small `main.go` file with a main function.
- Ran `go run` to execute your program and print “Hello, World!”.
