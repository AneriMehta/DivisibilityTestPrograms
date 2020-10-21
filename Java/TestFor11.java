import java.util.Scanner;

public class TestFor11 {
   public static void main(String args[]) {
      Scanner scan = new Scanner(System.in);
      System.out.println("Enter a number :");
      String num = scan.nextLine();
      int digitSumEve = 0;
      int digitSumOdd = 0;
     
     for(int i = 0; i<num.length(); i++) {
         if(i%2 == 0) {
            digitSumEve = digitSumEve + num.charAt(i)-'0';
         } else {
            digitSumOdd = digitSumOdd + num.charAt(i)-'0';
         }
      }
      int res = digitSumOdd-digitSumEve;
      if(res % 11 == 0) {
         System.out.println("Given number is divisible by 11");
      } else {
         System.out.println("Given number is not divisible by 11");
      }
   }
}