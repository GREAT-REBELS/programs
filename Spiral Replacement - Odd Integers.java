The program must accept an integer matrix of size NxN and a string S as the input. The program must traverse the matrix spirally in the anti-clockwise direction and replace all the odd integers with the alphabets 
in S. If the number of odd integers is greater than the length of S, the program starts replacing the odd integers with the alphabets in S circularly(i.e, after the last character, start replacing from the first 
character in S). Finally, the program must print the modified matrix as the output.

Example Input/Output 1:
Input:
3
7 8 9
6 3 4
1 5 7
rock

Output:
r 8 r
6 o 4
o c k
Explanation:
In the given 3x3 matrix, the odd integers are highlighted below.
7 8 9
6 3 4
1 5 7
The number odd integers in the matrix is 6 which is greater than the length of the string rock. Therefore, when traversing the matrix spirally in the anti-clockwise direction, the odd integers and their
replacement characters are given below.
7->r
1->o
5->c
7-> k
9 -> r (after the last character, start replacing from the first character in S)
3->0
So the matrix becomes
1 8 г
6 o 4
o c k

Example Input/Output 2:
Input:
6
12 23 32 2 6 89 
31 55 45 15 87 91 
63 74 32 44 98 86
23 43 56 88 98 45
43 44 46 88 67 54
ENVIRONMENT

output:
12 E 34 4 6 M
E N I V N N
N 74 32 44 98 86
V T 56 R E 54
134 56 88 98 Ο
34 44 46 88 R 54
  
Example Input/Output 3:
Input:
2
65 71
23 16
Apple

Output:
A p
p 16
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    String mat[][] = new String[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        mat[i][j] = sc.next();
      }
    }
    String str = sc.next();
    int len = str.length();
    int D = 0;
    int minRow = 0;
    int minCol = 0;
    int maxRow = N - 1;
    int maxCol = N - 1;
    while (minRow <= maxRow) {
      for (int i = minRow; i <= maxRow; i++) {
        mat[i][minCol] = (Integer.parseInt(mat[i][minCol]) % 2 == 1) ? str.charAt((D++) % len) + "" : mat[i][minCol];
      }
      for (int j = N - maxCol; j < maxCol; j++) {
        mat[maxRow][j] = (Integer.parseInt(mat[maxRow][j]) % 2 == 1) ? str.charAt((D++) % len) + "" : mat[maxRow][j];
      }
      for (int k = maxRow; k >= N - maxRow; k--) {
        mat[k][maxCol] = (Integer.parseInt(mat[k][maxCol]) % 2 == 1) ? str.charAt((D++) % len) + "" : mat[k][maxCol];
      }
      for (int l = maxCol; l >= N - maxCol; l--) {
        mat[minRow][l] = (Integer.parseInt(mat[minRow][l]) % 2 == 1) ? str.charAt((D++) % len) + "" : mat[minRow][l];
      }
      minRow++;
      minCol++;
      maxRow--;
      maxCol--;
    }

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        System.out.print(mat[i][j] + " ");
      }
      System.out.println();
    }
  }
}
