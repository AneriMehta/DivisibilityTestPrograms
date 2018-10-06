#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
  int n;
  int I;
  cout <<"enter the value of n : ";
  cin>>n;
  if (n%5==0)
  {
    cout<< endl <<"it is divisible by 5" << endl ;
  }
  else
  {
    cout<< endl <<"it is NOT divisible by 5" << endl ;
  }
  return 0;
}
