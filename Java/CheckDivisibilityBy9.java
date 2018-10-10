// Java program to find if a number is
// divisible by 9 or not
package isdivisibleby9;
import java.util.*;

class TestFor9
{
    // Function to find that number
    // is divisble by 9 or not
    static boolean check(String str)
    {
        // Compute sum of digits
        int n = str.length();
        int digitSum = 0;
        for (int i=0; i<n; i++)
            digitSum += (str.charAt(i)-'0');

        // Check if sum of digits is divisible by 9.
        return (digitSum % 9 == 0);
    }

    // main function
    public static void main (String[] args)
    {
        System.out.println("Enter the number");
        Scanner x = new Scanner(System.in);
        String str = x.nextLine();
        if(check(str))
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}


