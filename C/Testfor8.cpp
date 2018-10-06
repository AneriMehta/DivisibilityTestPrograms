// C++ program to check whether the number is divisible by 8 or not using bitwise operator  
  
// function 
int divby8(int n) 
{ 
    return (((n >> 3) << 3) == n); 
} 

int main() 
{ 
    int n;
    cout << "Enter the number";
    cin >> n;
    if (divby8(n)) 
        cout << "Divisible by 8." << endl; 
    else
        cout << "Not divisible by 8." << endl; 
    return 0; 
} 
