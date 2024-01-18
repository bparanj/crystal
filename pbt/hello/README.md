# Hello

```
brew install elixir
```


```
elixir --version
Erlang/OTP 26 [erts-14.2.1] [source] [64-bit] [smp:8:8] [ds:8:8:10] [async-threads:1] [jit] [dtrace]

Elixir 1.16.0 (compiled with Erlang/OTP 26)
```

mix new hello  
cd hello

hello/mix.exs:

```elixir
  defp deps do
    [
			{:propcheck, "~> 1.4.1", only: [:test, :dev]}
    ]
  end
```

```
mix deps.get
```

```
mix test
```

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `hello` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:hello, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at <https://hexdocs.pm/hello>.

