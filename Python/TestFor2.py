def Test_for_2(number):
    if int(str(number)[-1]) in [2, 4, 6, 8, 0] and number not in [0, 1]:
        return True
    else:
        return False
        
for i in range(100):
    print("{} divisible by 2 {}".format(i, Test_for_2(i)))
