defmodule ExercisesTest do
  use ExUnit.Case
  use PropCheck

  property "exercise 2: a sample" do
    forall {start, count} <- {integer(), non_neg_integer()} do
      list = Enum.to_list(start..(start + count))
      count + 1 == length(list) and increments(list)
    end
  end

  def increments([head | tail]), do: increments(head, tail)

  defp increments(_, []), do: true

  defp increments(n, [head | tail]) when head == n + 1,
    do: increments(head, tail)

  defp increments(_, _), do: false
end