require 'rantly'
require 'rantly/property'
require 'rantly/shrinks'

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, _next = nil)
    @val = val
    @next = _next
  end
end

# Converts an array to a linked list
def array_to_list(arr)
  head = ListNode.new(arr.first)
  current = head
  arr[1..].each do |val|
    current.next = ListNode.new(val)
    current = current.next
  end
  head
end

# Converts a linked list to an integer
def list_to_int(list)
  num = 0
  multiplier = 1
  while list
    num += list.val * multiplier
    list = list.next
    multiplier *= 10
  end
  num
end

def add_two_numbers(l1, l2)
  result = ListNode.new
  first = l1
  second = l2
  current = result
  carry = 0

  while (first || second || carry != 0)
    if first
      x = first.val
    else
      x = 0 
    end
 
    if second
      y = second.val 
    else
      y = 0
    end
 
    digit = x + y + carry
    carry = digit / 10

    node = ListNode.new(digit % 10)
    current.next = node
    current = current.next 
    first = first.next if first
    second = second.next if second
  end

  result.next
end

100.times do
  l1 = array_to_list(array = Rantly.new.array(5) { range(0, 9) })
  l2 = array_to_list(Rantly.new.array(5) { range(0, 9) })

  result = add_two_numbers(l1, l2)
  p result
  # Sum Validation
  expected_sum = list_to_int(l1) + list_to_int(l2)
  result_sum = list_to_int(result)
  raise 'Error' unless (expected_sum == result_sum)

  # Non-negative Values and Less than 10
  current = result
  while current
    raise 'Error' unless (current.val >= 0 && current.val < 10)
    current = current.next
  end

  # Length
  max_length = [list_to_int(l1).digits.count, list_to_int(l2).digits.count].max
  result_length = list_to_int(result).digits.count
  raise 'Error' unless (result_length == max_length || result_length == max_length + 1)
end