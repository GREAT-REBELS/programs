The program must accept an integer matrix of size RxC and an integer X as the input. The program must replace the integers with asterisks (*) in the north-east, south-east, south-west and north-west directions
of X(including X) in the matrix. Then the program must print the modified matrix as the output.
Note: The integer X has occurred only once in the RxC integer matrix.
  
Example Input/Output 1:
Input:
5 4
14 13 46 24
33 35 30 18
12 22 23 27
31 21 26 44
47 10 36 49
22
Output:
14 13 46 * 
* 35 * 18
12 * 23 27
* 21 * 44
47 10 36 *
Explanation:
The integers in the north-east, south-east, south-west and north-west directions of 22 are highlighted in the 5x4 matrix.
14 13 46 '24'
'33' 35 '30' 18
12 '22' 23 27
'31' 21 '26' 44
47 10 36 '49'
So those integers are replaced with asterisks (*) in the matrix.
Hence the output is
14 13 46 * 
* 35 * 18
12 * 23 27
* 21 * 44
47 10 36 49

Example Input/Output 2:
Input:
4 4
31 73 29 87
77 44 66 46
90 9 10 43
3 1 39 34
10
Output:
* 73 29 87
77 * 66 *
90 9 * 43
3 * 39 *
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int R = sc.nextInt();
    int C = sc.nextInt();
    int mat[][] = new int[R][C];
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        mat[i][j] = sc.nextInt();
      }
    }
    int X = sc.nextInt();
    int row = -1, col = -1;
    chk:
      for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
          if (mat[i][j] == X) {
            row = i;
            col = j;
            break chk;
          }
        }
      }
    int D1 = row, D2 = col, D3 = col;
    while (D1 >= 0) {
      if (D2 >= 0) {
        mat[D1][D2--] = -1;
      }
      if (D3 < C) {
        mat[D1][D3++] = -1;
      }
      D1 --;
    }
    D1 = row;
    D2 = col;
    D3 = col;
    while (D1 < R) {
      if (D2 >= 0) {
        mat[D1][D2--] = -1;
      }
      if (D3 < C) {
        mat[D1][D3++] = -1;
      }
      D1 ++;
    }
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        System.out.print(mat[i][j] == -1 ? "*" : mat[i][j] + " ");
      }
      System.out.println();
    }
  }
}
