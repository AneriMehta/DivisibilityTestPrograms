def reminder(num, divisor):
    return (num - divisor * (num // divisor))


while True:

    print("(enter 'q' to quit anytime)")

    num = input("Enter number for divisibility test: ")
    if num == 'q':
        break
    else:
        num = int(num)

    divisor = input("give divisor to divide the number: ")
    if divisor == 'q':
        break
    else:
        divisor = int(divisor)

    result = reminder(num, divisor)

    if result == 0:
        print("The number {} is divisible by {}\n".format(num, divisor))
    else:
        print("The number {} is not divisible by {}\n".format(num, divisor))
