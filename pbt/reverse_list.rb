require_relative 'venice'

property_reverse = -> (array) { array.reverse.reverse == array }

check_reverse_property(property_reverse) 

