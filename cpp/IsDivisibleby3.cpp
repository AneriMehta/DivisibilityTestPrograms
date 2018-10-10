// This file 'IsDivisibleby3.cpp' details a C++17 program to find whether a 
//  user-input number is divisible by 3, without the use of standard modulo
//  operator.

#include <iostream>
#include <cstdlib>

int main()
{
    int num = 0;
    std::cout <<  "Enter a number: " << std::endl;
    std::cin >> num;
    
    int remainder = num - 3 * (num / 3);
    remainder == 0 ? std::cout << "Yes, Divisible by 3.\n" : std::cout << "No, not divisible by 3.\n";
    
    return 0;
}