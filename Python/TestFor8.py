def test_for_8(num):

    flag = 0
    for j in range(3):
        num,mod = divmod(num,2)
        flag = flag + mod

    if flag == 0:
        return True
    else:
        return False


# Test to check that the function behaves properly
for i in range(100):
    print("{} divisible by 8 {}".format(i, test_for_8(i)))
