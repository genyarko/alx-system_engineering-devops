#!/usr/bin/env ruby
# This script checks if a string contains a certain pattern.

input_string = ARGV[0]
if input_string.match(/hbt{2,5}n/)
  puts "Match found!"
else
  puts "No match found."
end
