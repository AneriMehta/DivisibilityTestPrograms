''' We check the sum of all digits in a number 
If the sum is > 9 (two or more digits) we repeat the process
until we get a single digit.
	If the sum < 9 it is not divisible by 9
	If it == 9, it is divisible by 9
'''
def test_9(number):
	if number == 0:
		return True
	else:
		return True if separate_and_add(number) == 9 else False


'''
Here we turn the number being checked into a string
then we move through each column and sum them up
If the total at this point is two digits, we call this
function again with the current sum
When we have a one digit sum, we return the sum
'''
def separate_and_add(number):
	check_number = str(number)
	total = 0
	for place in range(len(check_number)):
		total+= (int(check_number[place]))
		if total > 9 :
			total = separate_and_add(total)
	return total





# Test to check that the function behaves properly
for number in range(1000):
	print(f'{number} divisible by 9: {test_9(number)}')
