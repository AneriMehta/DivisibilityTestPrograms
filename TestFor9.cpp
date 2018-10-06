#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if((int)(n/9) * 9 == n) {
        printf("Yes.");
    } else  printf("No.");
    return 0;
}
