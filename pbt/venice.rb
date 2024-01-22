def random_array
  Array.new(rand(1..20)) { rand(-100..100) }
end

def check_reverse_property(function)
  100.times do
    array = random_array
    print array
    unless function.call(array)
      puts "Test failed"
      return false
    end
  end
  puts "Test passed" 
  true
end