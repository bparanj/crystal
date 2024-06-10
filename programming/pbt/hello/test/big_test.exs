defmodule BigTest do
  use ExUnit.Case
	use PropCheck

	property "finds biggest element" do
		forall x <- non_empty(list(integer())) do
			biggest(x) == List.last(Enum.sort(x))
		end
	end
	
	def biggest([head | tail]) do
		biggest(tail, head)
	end
	
	defp biggest([], max) do
		max
	end
	
	defp biggest([head | tail], max) when head >= max do
		biggest(tail, head)
	end
	
	defp biggest([head | tail], max) when head < max do
		biggest(tail, max)
	end
end
