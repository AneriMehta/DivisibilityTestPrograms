#include<bits/stdc++.h>
using namespace std;

int main(){ 		//Program to check if is divisible for 9 in C++
				
	int number,sum = 0;
	cout << "Type a Number" << "\n";
	cin >> number;
	
	do{
		sum += number % 10;
		number = number/10;

	}while(number);

	if(sum % 9)
		cout << "Not Divisible for 9\n";
	else cout << "Divisible for 9\n";

	return 0;
}

