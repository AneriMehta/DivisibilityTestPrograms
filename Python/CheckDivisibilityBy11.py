def check(st) : 
    n = len(st)  
  
    # Compute sum of even and odd digit 
    # sums 
    oddDigSum = 0
    evenDigSum = 0
    for i in range(0,n) : 
        # When i is even, position of digit is odd 
        if (i % 2 == 0) : 
            oddDigSum = oddDigSum + ((int)(st[i])) 
        else: 
            evenDigSum = evenDigSum + ((int)(st[i])) 
      
      
    # Check its difference is divisble by 11 or not 
    return ((oddDigSum - evenDigSum) % 11 == 0) 
  
# Driver code 
st = input('Input to test for divisibility by 11: ')
if(check(st)) : 
    print( "Yes") 
else :  
    print("No ") 
      
