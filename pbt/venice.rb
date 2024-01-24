def input(type, size = 100)
  @type = type
  @size = size
end

def random_input
  Rantly(rand(1..20)) { range(-100, 100) } if @type == Array
end

def check_reverse_property(function)
  @size.times do |n|
    array = random_input

    if function.call(array)
      puts "OK. #{@size} tests passed"
      return true
    else
      puts "Falsified after #{n+1} times"
      print array
      return false
    end
  end
end