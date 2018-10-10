# Python Program to Check Number is Divisible by 11

number = int(input(" Please Enter any Positive Integer : "))

if((number % 11 == 0) ):
    print("Given Number {0} is Divisible by 11".format(number))
else:
    print("Given Number {0} is Not Divisible by 11".format(number))