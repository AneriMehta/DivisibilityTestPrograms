#include<stdio.h>
int main()
{
	int num;
	printf("Enter a number: ");
	scanf("%d"&num);
	if(num%3==0)
	{
		printf("%d is divisible by 3",num);
	}
	else
	{
		printf("%d is not divisible by 3",num);
	}
	return 0;
}