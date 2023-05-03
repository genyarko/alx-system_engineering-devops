#!/usr/bin/env ruby
# This script parses a log message and extracts the sender, receiver, and flags information.

input_string = ARGV[0]
regex_pattern = /(?<sender>[^,]+),(?<receiver>[^,]+),(?<flags>[^\s]+)/

match_data = input_string.match(regex_pattern)

if match_data
  puts "Sender: #{match_data[:sender]}"
  puts "Receiver: #{match_data[:receiver]}"
  puts "Flags: #{match_data[:flags]}"
else
  puts "No match found."
end
