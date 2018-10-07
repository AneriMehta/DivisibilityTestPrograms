def test_for_25(quotient):
    """Divisibility test to check if the quotient is 
    a multiple of 25, without using the modulo operator.
    This can be done, by checking if the final digit is 
    one of 00, 25, 50, or 75"""
    last_two_digits = str(quotient)[-2:]
    if last_two_digits in ["00", "25", "50", "75"] or last_two_digits == "0":
        return True
    else:
        return False


# Test to check that the function behaves properly
for i in range(400):
    print("{} divisible by 25 {}".format(i, test_for_25(i)))