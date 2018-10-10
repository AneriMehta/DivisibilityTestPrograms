def check_if_divisible(num):
    """
    checks if a number is dividable by 25 by dividing the number by 25,
    making the result an integer and see if the integer result multiplied by 25
    is the same as the original number
    """
    if num == int((num/25))*25:
        return True
    else:
        return False

for i in range(100):
    print("{} divisible by 25 {}".format(i, check_if_divisible(i)))
