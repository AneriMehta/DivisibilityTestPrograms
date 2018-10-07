import java.util.Scanner;
class NumberDivisibleBy25
{
  public static void main(String ar[])
  {
	  
		// your code
        Scanner scanner=new Scanner(System.in);
        long realNum =scanner.nextLong();
        long num =realNum; 
         if(num > 0)
        {
              checkDivisiblityBy25(num,realNum);
        }
        else 
        {
             num=-(num);
             checkDivisiblityBy25(num,realNum);
            
        }
        
	}

	static void checkDivisiblityBy25(long number,long realNum)
	{
	    
	    long rem1=number%10;
	    long number1=number/10;
	    long rem2=number1%10;
	    long lastTwoDigit=(10*rem2+rem1);
	    if(lastTwoDigit==25||lastTwoDigit==50||lastTwoDigit==75||lastTwoDigit==00)
	    {
	       System.out.println("Number "+realNum+" is divisible by 25");
	    }
	    else
	    {
	       System.out.println("Number "+realNum+" is not divisible by 25"); 
	    }
	}
  
  
}
