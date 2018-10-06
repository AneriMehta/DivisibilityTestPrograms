#include<iostream>
using namespace std;
 
int r(int n, int d) {  
    if (d == 0) { 
        cout<<"Error";
        return -1; 
    } 
  
    if (d < 0)
        d*=-1;
    if (n < 0)
        n*=-1;
   
    int i = 1; 
    int p = 0; 
    while (p <= n) 
    { 
        p = d * i; 
        i++; 
    } 
   
    return n - (p - d);
}                      

int main(){

    long long x;
    cin>>x;
    if(r(x,9))==0){
        cout<<"YES"
    }
    else 
        cout<<"NO";
    return 0;
}
