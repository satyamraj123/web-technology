
import java.util.Scanner;

public class qno10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        scanner.close();
        String s = String.valueOf(n);
        char[] a = s.toCharArray();
        int len = a.length;
        for (int i = 0; i < a.length; i++) {
            for (int j = i + 1; j < a.length; j++) {
                if (a[i] == a[j]) {
                    len = len - 1;
                    a[i] = 'z';
                }
            }
        }
        System.out.println("Number of dissimilar digits are: " + len);
    }
}
