receiving
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

ZERO
---Z
--ZE
-ZER
ZERO
ERO
RO
O

KeyBoard
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
      } else {
        System.out.print(str.substring(K, len));
        K += 1;
      }
      System.out.println();
    }
  }
}
