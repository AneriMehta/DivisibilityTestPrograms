/*input
5
*/
import java.io.*;
import java.util.*;

class DivisibleByThree
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int num=0;
        System.out.println("Enter a number..:");
        int n = sc.nextInt();
        int n2=n;
        int sumD=0;
        while(n2>0)
        {
            sumD+=n2%10;
            n2/=10;
        }
        System.out.println();
        if(sumD%3==0)
        {
            System.out.println(n +" is divisible by 3!!");
        }
        else
        {
            System.out.println(n +" is Not divisible by 3!!");
        }
    }
}