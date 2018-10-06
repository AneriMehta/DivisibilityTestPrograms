def test_for_9(quotient):
    """Divisibility test to check if the quotient is 
    a multiple of 9, without using the modulo operator.
    This can be done, by checking if the digit sum, 
    is 9, once it gets to be a single digit."""
    digit_sum = int(quotient)
    while digit_sum > 9:
        digits = str(digit_sum)
        total = 0
        for digit in digits:
            total += int(digit)
        digit_sum = total
    if digit_sum == 9:
        return True
    else:
        return False

# Test to check that the function behaves properly
for i in range(100):
    print("{} divisible by 9 {}".format(i, test_for_9(i)))
