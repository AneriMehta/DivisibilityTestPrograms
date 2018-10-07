using namespace std; 

int check(string str) 
{ 
    // Compute sum of digits 
    int n = str.length(); 
    int digitSum = 0; 
    for (int i=0; i<n; i++) 
        digitSum += (str[i]-'0'); 
 
    return (digitSum % 9 == 0); 
} 

int main() 
{ 
    string str = "99333"; 
    check(str)?  cout << "Yes" : cout << "No "; 
    return 0; 
} 
