/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package isdivisibleby4;
import java.util.*;
/**
 *
 * @author A
 */
public class IsDivisibleby4 {

    // Function to find that number  
    // is divisible by 4 or not 
    static boolean check(String str) 
    { 
        int n = str.length(); 
       
        // Empty string 
        if (n == 0) 
           return false; 
       
        // If there is single digit 
        if (n == 1) 
           return ((str.charAt(0)-'0')%4 == 0); 
       
        // If number formed by last two digits is 
        // divisble by 4. 
        int last = str.charAt(n-1) - '0'; 
        int second_last = str.charAt(n-2) - '0'; 
        return ((second_last*10 + last) % 4 == 0); 
    } 
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.println("Enter a number");
        Scanner x = new Scanner(System.in);
        String str = x.nextLine(); 
        if(check(str)) 
            System.out.println("Yes"); 
        else
            System.out.println("No"); 
    }
    
}
