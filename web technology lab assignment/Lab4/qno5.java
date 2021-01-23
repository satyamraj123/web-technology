import java.util.Arrays;
import java.util.Scanner;

public class qno5 {
    public static void main(String[] args) {
        int n = 1;
        System.out.println("Enter the amount of charachters you want to sort: ");
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        char[] a = new char[n];
        System.out.println("Enter the " + n + " charachters: ");
        for (int i = 0; i < n; i++) {
            a[i] = scanner.next().charAt(0);
        }
        scanner.close();
        Arrays.sort(a);
        for (int i = 0; i < n; i++) {
            System.out.print(a[i] + ",");
        }

    }
}
