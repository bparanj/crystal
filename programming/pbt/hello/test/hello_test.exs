defmodule HelloTest do
  use ExUnit.Case
	use PropCheck
	
  doctest Hello

  test "greets the world" do
    assert Hello.hello() == :world
  end
	
	property "always works" do
		forall type <- term() do
			boolean(type)
		end
	end
	
	def boolean(_) do
		true
	end
end
