"""Function's default is to check the divisibility by 4.
It can be extended to check divisibility by other number by passing the number as a second argument""" 
def test_divisibility(number, divider = 4):
    if type(number) in [int, float] and type(divider) in [int, float] : #Checking the valid datatype
        if number % divider == 0: #if divisible, remainder will be zero
            return True
        else:
            return False
    else:
        return "Please provide a valid input."
