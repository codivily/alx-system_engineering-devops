#!/usr/bin/env ruby
# This script match the a string argument to a regular expression.

if ARGV.length > 0
  puts ARGV[0].scan(/School/).join("")
end

