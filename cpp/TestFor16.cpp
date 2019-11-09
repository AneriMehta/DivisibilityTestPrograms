#include <iostream>

using namespace std;

int main(){
  int number, rest;
  cout << "Write a number: " << endl;
  cin >> number;
  
  rest = number%16;
  
  if (rest == 0){
    cout << "The number " << number << " is divisible by 16" << endl;
  } else {
    cout << "The number " << number << " is not divisible by 16" << endl;
  }
  
  return 0;
}
