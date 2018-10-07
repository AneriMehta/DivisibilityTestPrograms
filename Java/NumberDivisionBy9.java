import java.util.*;
import java.lang.*;
import java.io.*;
class NumberDivisionBy9{
  public static void main (String[] args) throws java.lang.Exception
	{
		// your code
        Scanner scanner=new Scanner(System.in);
        long num =scanner.nextLong();
        long sum=0;
        if(num > 0)
        {
             sum =getTheSumOfNumberOfDigit(num);
             checkDivisiblityByNine(sum,num);
        }
        else 
        {
            num=-(num);
            sum =getTheSumOfNumberOfDigit(num);
            num=-(num);
            checkDivisiblityByNine(sum,num);
            
        }
        
	}

	static long getTheSumOfNumberOfDigit(long number){
		long temp=0;
		 while(number>0)
		 {
			 temp=temp+number%10;
			 number=number/10;
	     }
		 return temp;
	}
	static void checkDivisiblityByNine(long sumOfDigitsOfNumber,long number)
	{
	    
	    if(sumOfDigitsOfNumber%9==0)
	    {
	       System.out.println("Number "+number+" is divisible by 9");
	    }
	    else
	    {
	       System.out.println("Number "+number+" is not divisible by 9"); 
	    }
	}
   
}
