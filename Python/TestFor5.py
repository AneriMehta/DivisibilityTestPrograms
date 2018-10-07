def test_for_5(quotient):
    """Divisibility test to check if the quotient is 
    a multiple of 5, without using the modulo operator.
    This can be done, by checking if the final digit is 
    either 0 or 5"""
    last_digit = int(str(quotient)[-1])
    if last_digit in [0, 5]:
        return True
    else:
        return False


# Test to check that the function behaves properly
for i in range(100):
    print("{} divisible by 5 {}".format(i, test_for_5(i)))