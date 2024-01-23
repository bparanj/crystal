require_relative 'venice'

# input(Array, Integer)
property_reverse = -> (array) { array.reverse.reverse == array }

check_reverse_property(property_reverse) 

