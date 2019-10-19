# Function to check if the given number
# is divisible by sum of its digits
def isDivisible(n):

    temp = n

    # Find sum of digits
    sum = 0;
    while (n):

        k = n % 10;
        sum += k;
        n /= 10;

    # check if sum of digits divides n
    if (temp % sum == 0):
        return "YES";

    return "NO";

# Driver Code
n = int(input("Enter number:"));

print(isDivisible(n));
