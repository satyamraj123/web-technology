import java.util.Scanner;

public class qno4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the charachter:");
        char s = scanner.next().charAt(0);
        scanner.close();
        boolean b1 = false;
        b1 = Character.isUpperCase(s);
        if (b1) {
            System.out.println(s + "->" + Character.toLowerCase(s));
        } else {
            System.out.println(s + "->" + Character.toUpperCase(s));
        }
    }
}
