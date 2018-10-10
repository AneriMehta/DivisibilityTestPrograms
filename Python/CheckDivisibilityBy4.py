def test_for_4(quotient):
    """Divisibility test to check if the quotient is 
    a multiple of 4, without using the modulo operator.
    This can be done, checking if the last two digits
    of the number are also a multiple of 4"""
    last_two_digits = int(str(quotient)[-2:])
    if last_two_digits in [4*i for i in range(25)]:
        return True
    else:
        return False


# Test to check that the function behaves properly
for i in range(300):
    print("{} divisible by 4 {}".format(i, test_for_4(i)))