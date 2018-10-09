# first 10 multiples of 7 including 0
multiples = [0,7,14,21,28,35,42,49,54,63,70]

#funtion to test divisibility
def isDivisibleBy7(num):
    if num<0:
        if abs(num) == 7:
            return True
        return False

    if num in multiples:
        return True

    elif (num <= 70):
        return False
    # Recur for ( num / 10 - 2 * num % 10 )
    return isDivisibleBy7(int(num / 10) - 2 * (num - int(num / 10)*10))

#test for first 100 values
for i in range(0,100):
    if isDivisibleBy7(i) == True:
        print(i," is divisible by 7")
