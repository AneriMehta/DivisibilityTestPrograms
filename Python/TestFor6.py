def Test_for_2(number):
    if int(str(number)[-1]) in [2, 4, 6, 8, 0] and number not in [0, 1]:
        return True
    else:
        return False

def Test_for_3(number):
    if sum([int(i) for i in str(number)]) in [i for i in range(3, 162, 3)]:
        return True
    else:
        return False

def Test_for_6(number):
    if Test_for_2(number) and Test_for_3(number):
        return True
    else:
        return False

for i in range(100):
    print("{} divisible by 6 {}".format(i, Test_for_6(i)))
