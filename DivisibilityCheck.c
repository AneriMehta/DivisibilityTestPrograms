#include <stdio.h>
void main(){
int n,check;
printf("Enter the Number:");
scanf("%d",&n);
printf("Enter the number to check divisibility with:");
scanf("%d",&check);
if(n%check==0)
printf("%d is Divisible by %d",n,check);
else
printf("Not Divisible");
}
