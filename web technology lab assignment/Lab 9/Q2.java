import java.util.Scanner;

class Q2 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String 1: ");
        String s9 = sc.nextLine();
        System.out.println("Enter String 2: ");
        String s = sc.nextLine();

        String s1 = s9 + " " + s + " ";
        System.out.println("Concatenated String: " + s1);
        System.out.println("String after split: \n");
        int l = s1.indexOf(" ");
        String s2 = s1.substring(0, l);
        s1 = s1.substring(l + 1);
        int l1 = s1.indexOf(" ");
        String s3 = s1.substring(0, l1);
        s1 = s1.substring(l1 + 1);
        int l2 = s1.indexOf(" ");
        String s4 = s1.substring(0, l2);
        s1 = s1.substring(l2 + 1);
        int l3 = s1.indexOf(" ");
        String s5 = s1.substring(0, l3);
        s1 = s1.substring(l3 + 1);

        System.out.println(s2);
        System.out.println(s3);
        System.out.println(s4);
        System.out.println(s5);

    }
}