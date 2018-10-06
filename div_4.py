import sys

number=0
if(len(sys.argv) < 2):
    number=input("Choose a number: ")
else:
    number = sys.argv[1]

if (int(number) % 4 == 0):
    print("This is divisible by 4!")
else:
    print("This is not divisible by 4.")