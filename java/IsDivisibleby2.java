import java.util.*;
class Main {
    public static void main(String arg[]) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter Number");
        String n = in.nextLine();
        int l = n.length();
        if (n.charAt(l - 1) == '2' || n.charAt(l - 1) == '4' || n.charAt(l - 1) == '6' || n.charAt(l - 1) == '8' || n.charAt(l - 1) == '0')
            System.out.println("Number is divisible by 2");
        else
            System.out.println("Not Divisible by 2");
    }
}

