#!/usr/bin/python3
'''
  Divisibility testing of 5 without modulo operator
'''  
n = int(input("Enter any integer: "))
lastdigit = int(repr(n)[-1])
if lastdigit == 0:
    print("This number is divided by 5")
elif lastdigit == 5:
    print("This number is divided by 5")
else:
    print("Not divided by 5")


