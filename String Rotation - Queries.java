String Rotation - Queries
The program must accept a string S and Q queries as the input. Each query contains an alphabet D and an integer M. The alphabet D represents a direction (L or R). The integer M represents a magnitude. 
  For each query, the program must modify the string S based on the conditions.
- If the direction is L, then the program must rotate the string S by M positions in the clockwise direction.
- If the direction is R, then the program must rotate the string S by M positions in the anticlockwise direction.
After processing each query, the program must print the first character in the modified string as the output.

Example Input/Output 1:
Input:
carriage
3
L3
R2
L2
Output:
rar
Explanation:
Here the string is carriage.
The first query is L 3, so the string carriage is rotated by 3 positions in the clockw The string becomes riagecar.
Click the button
The second query is R 2, so the string riagecar is rotated by 2 positions in the ant direction. The string becomes arriagec.
The third query is L 2, so the string arriagec is rotated by 2 positions in the clock
Go Full Screen
The string becomes riagecar.
The accumulated first characters are rar.
Hence the output is rar
  
Example Input/Output 2:
Input:
enormous
4
R4
L1
R7
L4
Output:
mouo
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	String str = sc.nextLine();
	int N = sc.nextInt();
	while(N!=0){
	    char ch = sc.next().charAt(0);
	    int T=sc.nextInt();
	    if(ch=='L'){
	        str=str.substring(T,str.length())+str.substring(0,T);
	    }
	    else{
	         str=str.substring(str.length()-T,str.length())+str.substring(0,str.length()-T);
	    }
	    System.out.println(str.charAt(0));
	    N--;
	}
	}
}
