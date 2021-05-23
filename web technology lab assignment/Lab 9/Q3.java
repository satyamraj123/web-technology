import java.util.*;
import java.lang.*;
import java.io.*;
class Q3
{
	public static void main(String args[])
	{
		Scanner in=new Scanner(System.in);
    String s,s1,s2,up,low;
    System.out.println("Enter a string");
    StringBuffer sb = new StringBuffer();
    s=in.nextLine();
    sb.append(s);
    for (int i=0;i<sb.length();i++) 
    {
      Character c = sb.charAt(i);
      if (Character.isLowerCase(c))
          sb.replace(i, i + 1,Character.toUpperCase(c) + "");
      else{
            for (int j=0;j<sb.length();j++) 
            {
              Character d = sb.charAt(i);
              if (Character.isUpperCase(d))
                sb.replace(i, i + 1,Character.toLowerCase(d) + "");
            }
          }
    }
    System.out.println("The string after changing the case is: " +sb +" \n\n");
    for (int i=0;i<sb.length();i++) 
    {
      Character c = sb.charAt(i);
      if (Character.isLowerCase(c))
          sb.replace(i, i + 1,Character.toUpperCase(c) + "");
      else{
            for (int j=0;j<sb.length();j++) 
            {
              Character d = sb.charAt(i);
              if (Character.isUpperCase(d))
                sb.replace(i, i + 1,Character.toLowerCase(d) + "");
            }
          }
    }
    System.out.println("The string after reversing is: "+sb.reverse()+" \n\n");
    sb.reverse();
		System.out.println("Enter the second string for comparison:");
		s1=in.nextLine();
    System.out.print("After the comparison we came to know that ");
    if(s.equalsIgnoreCase(s1))
        System.out.println("the strings are same\n\n");
    else
        System.out.println("the strings are not same\n\n");
    System.out.println("Enter the string to be inserted into first string:");
    StringBuffer sg = new StringBuffer();
    s2=in.nextLine();
    sg.append(s2);
    int n;
    System.out.println("Enter the position where you have to insert the string: ");
    n=in.nextInt();
		System.out.println("The string after insertion of another string is: " +sb.insert(n,sg));
    in.close();
	}
}