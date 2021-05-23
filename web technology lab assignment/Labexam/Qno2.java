import java.io.*;
import java.util.*;

public class Qno2{
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(new File("file.txt"));
            StringBuilder input = new StringBuilder(new String(""));
            while (sc.hasNext()) {
                input.append(sc.nextLine()).append("\n");
            }
            System.out.println("Input is -");
            System.out.println(input.toString());
            String output = input.toString().replace('#', '*');
            output = output.replace('\n', '/');
            System.out.println("Output is -");
            System.out.println(output.toString());

            FileOutputStream fout = new FileOutputStream("second.txt");
            fout.write(output.getBytes());
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}