import java.util.*;

public class hi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter USN : ");
        String s = sc.nextLine();
        if (s.length() == 10 && up(s) && (s.charAt(0) == '1' || s.charAt(0) == '2')
                && (s.substring(5, 7).equals("CS") || s.substring(5, 7).equals("IS") || s.substring(5, 7).equals("ES")
                        || s.substring(5, 7).equals("ME"))
                && Character.isDigit(s.charAt(7)) && Character.isDigit(s.charAt(8)) && Character.isDigit(s.charAt(9)))
            System.out.println(s + " is a valid USN");
        else
            System.out.println(s + " is an invalid USN");

        sc.close();
    }

    static boolean up(String s) {
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLowerCase(c))
                return false;
        }
        return true;
    }
}
