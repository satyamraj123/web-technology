import java.util.Scanner;

public class qno3 {

    public static void main(String[] args) {
        // String s, str1, str2;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the string:");
        String s = scanner.nextLine();
        scanner.close();
        StringBuffer str1 = new StringBuffer(s);
        StringBuffer str2 = new StringBuffer(s);
        str1.reverse();
        // System.out.println("Original String is:" + str2);
        // System.out.println("Reverse String is:" + str1);
        if (String.valueOf(str1).compareTo(String.valueOf(str2)) == 0)
            System.out.println("Given String is a palindrome");
        else
            System.out.println("Given String is Not a palindrome");
    }
}
