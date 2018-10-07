def Test_for_2(number):
    if int(str(number)[-1]) in [2, 4, 6, 8, 0] and number not in [0, 1]:
        return True
    else:
        return False


def Test_for_3(number):
    if sum([int(i) for i in str(number)]) in [i for i in range(3, 100, 3)]:
        return True
    else:
        return False


def Test_for_4(number):
    if int(str(number)[-2:]) in [i for i in range(4, 100, 4)]:
        return True
    else:
        return False


def Test_for_5(number):
    if int(str(number)[-1]) in [0, 5] and number != 0:
        return True
    else:
        return False

def Test_for_6(number):
    if Test_for_2(number) and Test_for_3(number):
        return True
    else:
        return False

def main():
    for i in range(100):
        print("{} divisible by 2 {}".format(i, Test_for_2(i)))
        print("{} divisible by 3 {}".format(i, Test_for_3(i)))
        print("{} divisible by 4 {}".format(i, Test_for_4(i)))
        print("{} divisible by 5 {}".format(i, Test_for_5(i)))
        print("{} divisible by 6 {}".format(i, Test_for_6(i)))
        




if __name__ == "__main__":
    main()
