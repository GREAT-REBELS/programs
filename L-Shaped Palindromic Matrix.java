The program must accept a character matrix of size NxN containing only alphabets as the input. The program must print the palindromic string values formed by concatenating the alphabets in the L-shaped layers of
the matrix as the output.
Note: The palindromic string values are case sensitive.
Example Input/Output 1:
Input:
5
m R m B a
a a A o B
I C d A M
A E C A R
Y A l a m

Output:
malAYAlam
RaCECAR
BoB
a

Explanation:
The string values formed by concatenating the characters in the L-shaped layers of the matrix
are given below.
malAYAlam
RaCECAR
mAdAM
BoB
a
The palindromic string values in the above string values are
malAYAlam
RaCECAR
BoB

Example Input/Output 2:
Input:
6
d E s R T X
e V E a i T
t l v d a r
a T E n E s
T A T I V E
t r a t e d

Output:
detartrated
EVITATIVE
TIT
X

Example Input/Output 3:
Input:
4
a F k N
c M m u
Q V M A
d i c a

Output: 
N
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    char mat[][] = new char[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        mat[i][j] = sc.next().charAt(0);
      }
    }
    int R = N - 1, C = 0;
    while (R != 0) {
      String word = "";
      for (int i = 0; i <= R; i++) {
        word += mat[i][C];
      }
      for (int j = C + 1; j < N; j++) {
        word += mat[R][j];
      }
      if (isPlanidrome(word)) {
        System.out.println(word);
      }
      C++;
      R--;
    }
    System.out.print(mat[R][C]);
  }
  static boolean isPlanidrome(String word) {
    int strt = 0, end = word.length() - 1;
    while (strt <= end) {
      if (word.charAt(strt) != word.charAt(end)) {
        return false;
      }
      strt++;
      end--;
    }
    return true;
  }
}
