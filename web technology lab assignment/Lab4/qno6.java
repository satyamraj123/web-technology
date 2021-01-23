import java.util.Scanner;

public class qno6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter marks : ");
        int marks = scanner.nextInt();
        scanner.close();
        System.out.print("Your grade : ");
        if (marks >= 90) {
            System.out.println("O");
        } else if (marks >= 80) {
            System.out.println("E");
        } else if (marks >= 70) {
            System.out.println("A");
        } else if (marks >= 60) {
            System.out.println("B");
        } else if (marks >= 50) {
            System.out.println("C");
        } else if (marks >= 40) {
            System.out.println("D");
        } else if (marks >= 30) {
            System.out.println("F");
        }

    }
}
