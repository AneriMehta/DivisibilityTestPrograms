#!/usr/bin/python3

def reminder(divisor):
    return (25 - divisor * (25 // divisor))

divisor = int(input("give any number: "))

result = reminder(divisor)

if result == 0:
    print ("This number is divided by 25")
else:
    print ("not divided by 25")

