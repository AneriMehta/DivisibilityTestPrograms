using namespace std; 
  
// Function to find that number divisible 
// by 25 or not. 
bool isDivisibleBy25(string str) 
{ 
    // If length of string is single digit then 
    // it's not divisible by 25 
    int n = str.length(); 
    if (n == 1) 
        return false; 
  
    return ( (str[n-1]-'0' == 0  && 
              str[n-2]-'0' == 0) || 
   ((str[n-2]-'0')*10 + (str[n-1]-'0'))%25 == 0 ); 
} 
  
// Driver code 
int main() 
{ 
    string str = "76955"; 
    isDivisibleBy25(str)?  cout << "Yes" : 
                           cout << "No "; 
    return 0; 
} 
