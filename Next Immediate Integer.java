The program must accept an integer N as the input. The program must print the next immediate integer that has all the digits in N as the output. If there is no such next immediate integer then the program
must print -1 as the output.
  
Example Input/Output 1:
Input: 2586
Output: 2658
Explanation: The next immediate integer that has all the digits in 2586 is 2658. Hence the output is 2658
  
Example Input/Output 2:
Input:
3111
Output:
-1
  
Example Input/Output 3:
Input:
101
Output:
110
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.nextLine();
    String limit = "9".repeat(str.length());
    boolean flg = false;
    char arr1[] = str.toCharArray();
    for (int i = Integer.valueOf(str) + 1; i <= Integer.valueOf(limit) + 1; i++) {
      char arr2[] = String.valueOf(i).toCharArray();
      Arrays.sort(arr1);
      Arrays.sort(arr2);
      if (Arrays.equals(arr1, arr2)) {
        System.out.print(i);
        flg = true;
        break;
      }
    }
    if (!flg) {
      System.out.print("-1");
    }
  }
}
