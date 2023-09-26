import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System .in);
		String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		String lower = "abcdefghijklmnopqrstuvwxyz";
		String number = "0123456789";
		String specialchars = "<>,.?/}[}]+_-)(*&^%$#@!";
		String combination = upper+lower+specialchars+number;
		Random r = new Random();
		int length;
		System.out.print("Enter the Password length to be : ");
		length = sc.nextInt();
		char[] password = new char[length];
		for(int i=0;i<length;i++)
		{
		    password[i] = combination.charAt(r.nextInt(combination.length()));
		}
		System.out.print("Generated Password is : " + new String(password));
	}
}
