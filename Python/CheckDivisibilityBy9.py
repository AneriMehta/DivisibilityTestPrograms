def find_sum_of_digits(Number):
    Sum=0
    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum

def count_no_of_digits(Number):
    count=0
    while(Number>0):
        Number = Number //10
        count = count+1
    return count  
    

def check_divisibility(Number):
    Sum = find_sum_of_digits(Number)
    noOfDigits = count_no_of_digits(Sum)
    if (noOfDigits == 1):
        if(Sum == 9):
            print("\n Divisible by 9")
        else:
            print("\n NOT Divisible by 9")
    else:
        check_divisibility(Sum)
        
if __name__ == "__main__":
    Number = int(input('Input to test for divisibility by 9: '))
    check_divisibility(Number)
