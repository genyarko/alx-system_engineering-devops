#!/usr/bin/env ruby
# This script checks if a string starts with "h", ends with "n", and has any single character in between.

input_string = ARGV[0]
if input_string.match(/^h.n$/)
  puts "Match found!"
else
  puts "No match found."
end
