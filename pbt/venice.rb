def input(type, cases = 100)
  @type = type
  @cases = cases
end

def random_input
  if @type == Array
    arrays = (0..20).map do |size|
      Array.new(size) { rand(-100..100) }
    end  
  end
end

def check_reverse_property(function)
  @cases.times do |n|
    array = random_input

    if function.call(array)
      puts "OK. #{@cases} tests passed"
      return true
    else
      puts "Falsified after #{n+1} times"
      print array
      return false
    end
  end
end
