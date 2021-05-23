import java.util.*;
public class Q4
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter name 1 : ");
        String s1=sc.nextLine();
        System.out.print("Enter name 2 : ");
        String s2=sc.nextLine();
        int n1 = s1.lastIndexOf(" ");
        int n2 = s2.lastIndexOf(" ");
        System.out.println("Swapped name 1 = "+s1.substring(0,n1) + s2.substring(n2));
        System.out.println("Swapped name 2 = "+s2.substring(0,n2) + s1.substring(n1));
    }
}