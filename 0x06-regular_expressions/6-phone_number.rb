#!/usr/bin/env ruby
# Regular expression that matches School
puts ARGV[0].scan(/^\d{10,10}$/).join
