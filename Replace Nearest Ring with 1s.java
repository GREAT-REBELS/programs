The program must accept a matrix of size RxC containing 0s, 1s and exactly one X as the input. The program must find the full ring near to X with at least one 0. Then the program must modify the matrix by 
replacing all Os in the full ring with 1s. Finally, the program must print the modified matrix as the output. If there is no such full ring near to X, the program must print the given matrix as it is.

Example Input/Output 1:
Input:
5 6
0 1 1 1 0 1
1 1 0 1 1 0
0 1 1 X 0 1
0 0 1 0 0 1
0 0 0 1 1 0
Output:
0 1 1 1 0 1
1 1 1 1 1 0
0 1 1 X 1 1
0 0 1 1 1 1
0 0 0 1 1 0
Explanation:
The full ring near to X with at least one 0 is highlighted below.
0 1 1 1 0 1
1 1 '0' '1' '1' 0
0 1 '1' X '0' 1
0 0 '1' '0' '0' 1
0 0 0 1 1 0
After replacing Os in the full ring with 1s, the matrix becomes
0 1 1 1 0 1
1 1 1 1 1 0
0 1 1 X 1 1
0 0 1 1 1 1
0 0 0 1 1 0
Example Input/Output 2:

Input:
8 7
1 0 0 1 0 0 0
0 1 1 0 1 1 0
1 1 1 1 1 1 1
1 1 X 1 0 1 0
1 1 1 1 1 1 0
0 1 1 0 1 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0
Output:
1 0 0 1 0 0 0
1 1 1 1 1 1 0
1 1 1 1 1 1 1
1 1 X 1 1 1 0
1 1 1 1 1 1 0
1 1 1 1 1 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0
Explanation:
The full ring near to X with at least one 0 is highlighted below.
1 0 0 1 0 0 0
'0' '1' '1' '0' '1' 1 0
'1' 1 1 1 '1' 1 1
'1' 1 X 1 '0' 1 0
'1' 1 1 1 '1' 1 0
'0' '1' '1' '0' '1' 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0
After replacing Os in the full ring with 1s, the matrix becomes
1 0 0 1 0 0 0
1 1 1 1 1 1 0
1 1 1 1 1 1 1
1 1 X 1 1 1 0
1 1 1 1 1 1 0
1 1 1 1 1 0 1
0 0 1 0 0 0 1
0 1 1 1 1 1 0

Example Input/Output 3:
Input:
3 4
1 0 1 0
X 0 1 0
0 0 0 0
Output:
1 0 1 0
X 0 1 0
0 0 0 0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int R = sc.nextInt();
    int C = sc.nextInt();
    char[][] mat = new char[R][C];
    int strtRow = 0, endRow = 0, strtCol = 0, endCol = 0;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        mat[i][j] = sc.next().charAt(0);
        if (mat[i][j] == 'X') {
          strtRow = i - 1;endRow = i + 1;strtCol = j - 1;endCol = j + 1;
        }
      }
    }
    int flg = 0;
    while (strtRow >= 0 && strtCol >= 0 && endRow < R && endCol < C) {
      for (int i = strtRow; i <= endRow; i++) {
        for (int j = strtCol; j <= endCol; j++) {
          if (mat[i][j] == '0') {
            mat[i][j] = '1';
            flg = 1;
          }
        }
      }
      if (flg == 1) {
        break;
      }
      strtRow -= 1;endRow += 1;strtCol -= 1;endCol += 1;
    }
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        System.out.print(mat[i][j] + " ");
      }
      System.out.println();
    }
  }
}
