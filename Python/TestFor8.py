def testfor8(imput):
    if type(imput) is not int:
        print('Wrong imput, imput is not divisible by 8')
        return False
    if imput % 8 == 0:
        print(str(imput), 'is divisible by 8')
    else:
        print(str(imput), 'is not divisible by 8')
