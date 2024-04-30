Example Input/Output 1:
Input:
eat 
4
Output:
***e
at**
*###
####

Example Input/Output 2:
Input:
abcdefghijklmnopqrst
5
Output:
****a
bc***
**def
ghij*
klmno
  
Example Input/Output 3:
Input:
abcDEfG
7
Output:
******a
bc*****
****DEf
G###***
**#####
######*
#######
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.next();
    int N = sc.nextInt();
    int k = 0;
    for (int i = 0; i < N; i++) {
      if (i % 2 == 0) {
        for (int j = 0; j < N; j++) {
          if (j >= N - i - 1) {
            System.out.print((k < str.length()) ? str.charAt(k++) : '#');
          } else {
            System.out.print('*');
          }
        }
      } else {
        for (int j = 0; j < N; j++) {
          if (j <= i) {
              System.out.print((k < str.length()) ? str.charAt(k++) : '#');
          } else {
            System.out.print('*');
          }
        }
      }
      System.out.println();
    }
  }
}
