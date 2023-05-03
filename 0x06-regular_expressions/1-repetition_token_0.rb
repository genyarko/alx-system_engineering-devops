#!/usr/bin/env ruby

input_string = ARGV[0]
if input_string.match(/hbt{2,5}n/)
  puts "Match found!"
else
  puts "No match found."
end
