# Python code to find highest
# K-digit number divisible by X

def answer(X, K):

    # Computing MAX
    MAX = pow(10, K) - 1

    #returning ans
    return (MAX - (MAX % X))

X = int(input("Enter Digit:"));
K = int(input("Enter Digit:"));

print(answer(X, K));
