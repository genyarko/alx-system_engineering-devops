#!/usr/bin/env ruby
# This script checks if a string contains a 10 digit phone number.

input_string = ARGV[0]
if input_string.match(/^\d{10}$/)
  puts "Match found!"
else
  puts "No match found."
end
