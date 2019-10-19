# Python Program to find numbers divisible by thirteen from a list using anonymous function
my_list = []

size = int(input("Enter size of list: \t"))

for n in range(size):
    numbers = int(input("Enter any number: \t"))
    my_list.append(numbers) # for adding num to list
x = int(input("\nEnter the number for division: "))


# Take a list of numbers

# use anonymous function to filter
result = list(filter(lambda y: (y % x == 0), my_list))

# display the result
print("Numbers divisible by entered number is",result)
