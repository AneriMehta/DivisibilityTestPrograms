#include<iostream>
using namespace std;

int check(string str)
{
    int n = str.length();

    // Compute sum of even and odd digit
    int oddDigSum = 0, evenDigSum = 0;
    for (int i=0; i<n; i++)
    {
        // When i is even, position of digit is odd
        if (i%2 == 0)
            oddDigSum += (str[i]-'0');
        else
            evenDigSum += (str[i]-'0');
    }
    // Check its difference is divisble by 11 or not
    return ((oddDigSum - evenDigSum) % 11 == 0);
}
int main()
{
    string str;
    cout << "Enter number: " ;
    cin >> str ;
    check(str)?  cout << "Number divisible by 11" : cout << "Number not divisible by 11";
    return 0;
}
