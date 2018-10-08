"""
A simple script to check if a given number is divisible by 25
without using the modulo function.

Takes a given number and returns a message if the number is dividable or not

__author__ = RayPatterson77
__email_ == ray.patterson@riseup.net
"""


def check_input(num):
    """
    check if the input is a valid integer.
    does the number positive if it's negative

    returns the value if it is, raises ValueError if not
    """
    try:
        num = int(num)
        if num < 0:
            num = num * -1
        return num
    except ValueError as e:
        print('%s is not a valid integer:' % (num))
        raise e


def check_if_dividable(num):
    """
    checks if a number is dividable by 25 by dividing the number by 25,
    making the result an integer and see if the integer result multiplied by 25
    is the same as the original number
    """
    if num == int((num/25))*25:
        print('%s is dividable by 25' % (num))
    else:
        print('%s is not dividable by 25' % (num))


def main():
    user_input = input('Please enter a (integer) number... ')
    number = check_input(user_input)
    check_if_dividable(number)


if __name__ == '__main__':
    main()
