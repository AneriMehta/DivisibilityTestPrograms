def is_divisible_by?(num, divisor)
  (num - divisor * (num / divisor)) == 0
end

puts "Enter a number: "
num = Integer(gets.chomp)
divisor = 25

if is_divisible_by?(num, divisor)
  puts "Number is divisible by #{divisor}"
else
  puts "Number is NOT divisible by #{divisor}"
end
