## Fibonacci

Computing Fibonacci numbers efficiently often involves iterative or memoized solutions for performance reasons. However, expressing this in a concise, one-liner format across different languages, especially in a way that emphasizes efficiency, can be challenging due to syntax and language capabilities. The most efficient one-liners typically use recursion with memoization or iterative approaches, but for the sake of simplicity and brevity, here are concise examples for each language, focusing on clarity and directness rather than optimizing for performance.

Note: These solutions are not always the most efficient in terms of execution time, especially for large Fibonacci numbers, due to the limitations of expressing the solution as a one-liner and without explicit memoization or iterative optimization.

1. **JavaScript** (Recursive, not optimized for large numbers)
   ```javascript
   const fib = n => n < 2 ? n : fib(n - 1) + fib(n - 2);
   ```

2. **Python** (Using tuple unpacking)
   ```python
   fib = lambda n, a=0, b=1: a if n == 0 else fib(n-1, b, a+b)
   ```

3. **Java** (Using Stream API, Java 8+)
   ```java
   int fib(int n) { return java.util.stream.Stream.iterate(new int[]{0, 1}, f -> new int[]{f[1], f[0] + f[1]}).limit(n).reduce((a, b) -> b).get()[0]; }
   ```

4. **C#** (Using local function)
   ```csharp
   int Fib(int n) => n < 2 ? n : Fib(n - 1) + Fib(n - 2);
   ```

5. **C++** (Using lambda, C++11+)
   ```cpp
   auto fib = [](int n) { int a=0, b=1; while(n--) { auto temp = a; a = b; b += temp; } return a; };
   ```

6. **TypeScript** (Similar to JavaScript)
   ```typescript
   const fib = (n: number): number => n < 2 ? n : fib(n - 1) + fib(n - 2);
   ```

7. **PHP**
   ```php
   function fib($n) { return $n < 2 ? $n : fib($n - 1) + fib($n - 2); }
   ```

8. **Swift**
   ```swift
   func fib(_ n: Int) -> Int { return n < 2 ? n : fib(n-1) + fib(n-2) }
   ```

9. **Ruby**
   ```ruby
   fib = ->(n) { n < 2 ? n : fib.call(n-1) + fib.call(n-2) }
   ```

10. **Kotlin**
    ```kotlin
    fun fib(n: Int): Int = if (n < 2) n else fib(n - 1) + fib(n - 2)
    ```

11. **Go**
    ```go
    func fib(n int) int { if n < 2 { return n } return fib(n-1) + fib(n-2) }
    ```

12. **Rust**
    ```rust
    fn fib(n: u32) -> u32 { match n { 0 | 1 => n, _ => fib(n-1) + fib(n-2), } }
    ```

13. **R**
    ```r
    fib <- function(n) ifelse(n < 2, n, fib(n - 1) + fib(n - 2))
    ```

14. **Dart**
    ```dart
    int fib(int n) => n < 2 ? n : fib(n - 1) + fib(n - 2);
    ```

15. **Scala**
    ```scala
    def fib(n: Int): Int = if (n < 2) n else fib(n-1) + fib(n-2)
    ```

16. **Perl**
    ```perl
    sub fib { my $n = shift; $n < 2 ? $n : fib($n - 1) + fib($n - 2) }
    ```

17. **Lua**
    ```lua
    function fib(n) return n < 2 and n or fib(n - 1) + fib(n - 2) end
    ```

18. **Haskell**
    ```haskell
    fib n = if n < 2 then n else fib (n-1) + fib (n-2)
    ```

19. **Objective-C** (Using block, not traditional one-liner)
    ```objc
    int (^fib)(int) = ^int(int n) { return n < 2 ? n : fib(n-1) + fib(n-2); };
    ```

20. **MATLAB**
    ```matlab
    fib = @(n) n < 2 * n : fib(n-1) + fib(n-2);
    ```

Each solution captures the essence of computing Fibonacci numbers in the respective programming language, highlighting different syntactic and functional approaches. For applications requiring efficiency, especially with larger Fibonacci numbers, iterative solutions or those employing memoization techniques are recommended.
