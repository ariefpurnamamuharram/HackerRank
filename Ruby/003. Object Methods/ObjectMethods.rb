# Object Methods.
# ---
# Each of object in Ruby may have methods associate with it

def odd_or_even(number)
  # Check number if its even.
  number.even?
end

(0..gets.to_i).each do |i|
  puts odd_or_even(gets.to_i)
end
