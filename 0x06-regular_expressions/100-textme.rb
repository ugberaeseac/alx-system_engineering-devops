#!/usr/bin/env ruby
# Regular expression that matches sender, receiver and flags
# of a Textme log file
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
