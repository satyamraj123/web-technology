import java.util.*;

public class Q1 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a name : ");
        String s = sc.nextLine();
        String[] arr = s.split(" ", 2);
        System.out.println("New name = " + arr[0] + " Kumar " + arr[1]);
    }
}