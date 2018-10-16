
def isDivisibleBy9(n): 
	"""Divisibility test to check if the quotient is 
	a multiple of 9, without using the modulo operator.
	According https://www.geeksforgeeks.org/divisibility-9-using-bitwise-operators/
	take bitwise operations."""

	# Base cases 
	if (n == 0 or n == 9): 
		return True
	if (n < 9): 
		return False

	# If n is greater than 9, 
	# then recur for [floor(n / 9) - n % 8] 
	return isDivisibleBy9((int)(n>>3) - (int)(n&7)) 

# Driver code 

# Let us print all multiples 
# of 9 from 1 to 100
# using above method 

for i in range(100):
	if (isDivisibleBy9(i)):
		print("{} divisible by 9 {}".format(i, isDivisibleBy9(i)))
