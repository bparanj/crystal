require 'rantly'
require 'set'

# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    n = s.size
    seen = Set.new
    left = 0
    right = 0
    result = 0

    while (right < n)
       unless seen.include?(s[right])
          seen.add(s[right]) 
          result = [result, seen.size].max
          right += 1
       else
         seen.delete(s[left])
         left += 1  
       end
    end
    result
end

100.times do
  str = Rantly { string } # Generate a random string without specifying length
  puts str
  result = length_of_longest_substring(str)
  
  raise "Result out of expected bounds: #{result} for string '#{str}'" unless result >= 0 && result <= str.length
  
  # Non-negativity
  raise 'failed' unless length_of_longest_substring(str) >= 0 

  # Upper Bound
  raise 'failed' unless length_of_longest_substring(str) <= str.length 

  # Idempotency
  first_call = length_of_longest_substring(str)
  second_call = length_of_longest_substring(str)
  raise 'failed' unless first_call == second_call

  # Substrings
  substrings = (0...str.length).flat_map { |l| (l...str.length).map { |r| str[l..r] } }
  valid_substrings = substrings.select { |sub| sub.chars.uniq.length == sub.length }
  max_valid_length = valid_substrings.map(&:length).max || 0
  raise 'failed' unless length_of_longest_substring(str) >= max_valid_length

  # Invariance Under Permutation
  if str.chars.uniq == str.chars
    permutations = str.chars.permutation.to_a.map(&:join)
    lengths = permutations.map { |perm| length_of_longest_substring(perm) }
    raise 'failed' unless lengths.uniq.length == 1 
  end
  
end

puts "All tests passed."


