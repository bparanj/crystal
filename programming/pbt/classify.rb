require 'rantly'
require 'rantly/property'
require 'rantly/shrinks'

# Initialize counters for classifications
classification_counts = Hash.new(0)

100.times do
  Rantly { integer }.tap do |val|
    # Define classification criteria
    if val.even?
      classification_counts[:even] += 1
    else
      classification_counts[:odd] += 1
    end

    # Example property test
    # Replace this with actual property logic
    puts "Value is unexpectedly large!" if val > 100_000
  end
end

# Output classification results
puts "Classification Counts:"
classification_counts.each do |category, count|
  puts "#{category}: #{count}"
end
