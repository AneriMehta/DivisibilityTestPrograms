import java.io.*;
import java.util.*;

class TestFor8
{
    public static void main(String args[])
    {
        Scanner x =new Scanner(System.in);
        int num=0;
        System.out.print("Enter a number..:");
        int n = x.nextInt();
        int n2 = n;
        int temp =(int) n2 / 8;
        for(int i=1;i<=temp;i++)
        {
            num=num+8;
        }
        if(num == n2)
        {
            System.out.println(n2 +" is divisible by 8!!");
        }
        else
        {
            System.out.println(n2 +" is Not divisible by 8!!");
        }
    }
}