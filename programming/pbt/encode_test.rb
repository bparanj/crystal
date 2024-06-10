require 'rantly'
require 'rantly/rspec_extensions'

def encode(string)
  string
    .chars
    .chunk{|i| i}
    .map {|kind, array| [kind, array.length]}
end

def decode(char_counts)
  char_counts
    .map{|char, count| char * count}
    .join
end

describe 'Encoding and Decoding' do
  it 'returns the original string after encoding and decoding' do
    property_of {
      Rantly { string }
    }.check { |original_string|
      p original_string
      encoded_string = encode(original_string)
      decoded_string = decode(encoded_string)
      expect(decoded_string).to eq(original_string)
    }
  end
end
