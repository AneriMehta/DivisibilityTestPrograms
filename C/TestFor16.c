#include <stdio.h>
#include <stdlib.h>


int main(int argc, char **argv)
{
    // check for at one argument
    if (argc != 2)
    {
        printf("Usage ./TestFor16 <number>\n");
        return 1;
    }
    int result = atoi(argv[1]);
    
    // adding all the number together
    if ((result & 15) == 0)
        printf("%s is divisible by 16\n", argv[1]);
    else
        printf("%s is not divisible by 16\n", argv[1]);
}


