#!/usr/bin/env ruby

string = ARGV[0]

if string.match(/School/)
  puts "Match found!"
else
  puts "Match not found :("
end
