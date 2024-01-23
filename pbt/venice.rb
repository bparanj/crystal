def input(type, size = 100)
  @type = type
  @size = size
end

def random_input
  Array.new(rand(1..20)) { rand(-100..100) if @type == Array }
end

def check_reverse_property(function)
  @size.times do
    array = random_input
    print array
    unless function.call(array)
      puts "Test failed"
      return false
    end
  end
  puts "OK. 100 Tests passed" 
  true
end