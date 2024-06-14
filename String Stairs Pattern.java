The program must accept a string S containing only alphabets as the input. The program must print the string S for (L*2)-1 times (where L is the length of the string S) based on the following conditions.

- In line 1, the program must print L-1 hyphens and the first alphabet in S.

- In line 2, the program must print L-2 hyphens and the first two alphabets in S.

- Similarly, the program prints the first L lines as the output.

- In line L+1, the program must print the string S except the first alphabet.

- In line L+2, the program must print the string S except the first two alphabets. - Similarly, the program prints the remaining lines as the output.
  
Example1 Input/Output :
Input:
receiving
Output:
--------r
-------re
------rec
-----rece
----recei
---receiv
--receivi
-receivin
receiving
eceiving
ceiving
eiving
iving
ving
ing
ng
g
Explanation:
The length of the given string receiving is 9. So the pattern contains (9*2)-1 lines.
In line 1, 8 hyphens and the first alphabet in S are printed.
In line 2, 7 hyphens and the first two alphabets in S are printed. 
In line 3, 6 hyphens and the first three alphabets in S are printed.
Similarly, the first 9 lines are printed.
--------r
-------re
------rec
-----rece
----recei
---receiv
--receivi
-receivin
receiving
In line 10, the string S is printed except the first alphabet.
In line 11, the string S is printed except the first two alphabets.
In line 12, the string S is printed except the first three alphabets. Similarly, the remaining lines are printed.
eceiving
ceiving
eiving
iving
ving
ing
ng
g
  
Example2 Input/Output:
Input:
ZERO
Output:
---Z
--ZE
-ZER
ZERO
ERO
RO
O

Example Input/Output3:
Input:
KeyBoard
Output:
-------K
------Ke
-----Key
----KeyB
---KeyBo
--KeyBoa
-KeyBoar
KeyBoard
eyBoard
yBoard
Board
oard
ard
rd
d
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.next();
    int len = str.length();
    int end = str.length() - 1;
    int K = 1;
    for (int i = 0; i < len * 2; i++) {
      if (i < len) {
        for (int j = 0; j < len; j++) {
          if (j < end) {
            System.out.print("-");
          } else {
            break;
          }
        }
        System.out.print(str.substring(0, i + 1));
        end--;
      } 
      else {
        System.out.print(str.substring(K, len));
        K += 1;
      }
      if(i<len*2)
         System.out.println();
    }
  }
}
