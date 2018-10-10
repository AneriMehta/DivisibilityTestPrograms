// Java program to find if a number 
// is divisible by 16 or not 
package isdivisibleby16;
import java.io.*; 
import java.util.*;
  
class IsDivisibleby16 { 
    // Function to find that 
    // number divisible by 16 or not 
    static boolean check(String str) 
    { 
        int n = str.length(); 
       
        // Empty string 
        if (n == 0 && n == 1) 
            return false; 
       
        // If there is double digit 
        if (n == 2) 
            return (((str.charAt(n-2)-'0')*10 + 
                     (str.charAt(n-1)-'0'))%16 == 0); 
       
        // If there is triple digit 
        if(n == 3) 
             return ( ((str.charAt(n-3)-'0')*100 + 
                       (str.charAt(n-2)-'0')*10 + 
                       (str.charAt(n-1)-'0'))%16 == 0); 
       
       
        // If number formed by last 
        // four digits is divisible by 16. 
        int last = str.charAt(n-1) - '0'; 
        int second_last = str.charAt(n-2) - '0'; 
        int third_last = str.charAt(n-3) - '0'; 
        int fourth_last = str.charAt(n-4) - '0'; 
        return ((fourth_last*1000 + third_last*100 
                + second_last*10 + last) % 16 == 0); 
    } 
       
    // Driver code 
    public static void main(String args[]) 
    { 
        System.out.println("Enter the number");;
        Scanner x=new Scanner(System.in);
        String str = x.nextLine(); 
        if(check(str)) 
            System.out.println("Yes"); 
        else
            System.out.println("No "); 
    } 
} 