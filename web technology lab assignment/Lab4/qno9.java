import java.util.Scanner;

public class qno9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        scanner.close();
        String s = String.valueOf(n);
        char[] a = s.toCharArray();
        int sum = 0;
        for (int i = 0; i < a.length; i++) {
            sum = sum + Character.getNumericValue(a[i]);
        }
        System.out.println(n + " > " + sum);
    }
}
