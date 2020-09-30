def test_for_9(quotient):
    """Divisibility test to check if the quotient is 
    a multiple of 9, without using the modulo operator.
    This can be done, by checking if the digit sum, 
    is 9, once it gets to be a single digit."""
    digit_sum = int(quotient)   # Takes the given number and convert into int
    while digit_sum > 9:    # Checks if the number provided by user is greater than 9
        digits = str(digit_sum) # Convert digits into string for individual purpose
        total = 0
        for digit in digits:    # For loop to use individual digit for digit sum
            total += int(digit) # Adds each digit to get digit sum
        digit_sum = total
    if digit_sum == 9: # If loop for digit sum == 9
        return True
    else:
        return False

# Test to check that the function behaves properly
for i in range(100):
    print("{} divisible by 9 {}".format(i, test_for_9(i)))
