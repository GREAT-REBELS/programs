The program must accept an integer matrix of size RxC as the input. The program must print YES if every row and every column of the matrix is a palindrome. Else the program must print NO as the output.

Example Input/Output 1:
Input:
4 4
1 2 2 1
2 3 3 2
2 3 3 2
1 2 2 1
Output:
YES
Explanation:
In the given 4x4 matrix, every row and every column is a palindrome.
So YES is printed.

Example Input/Output 2:
Input:
3 5
2 4 3 4 2
3 7 8 7 3
5 6 1 6 5
Output:
NO
  
Example Input/Output 3:
Input:
5 4
67 77 77 67
48 74 74 48
53 95 95 53
48 74 74 48
67 77 77 67
Output:
YES
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
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
    int col = 0, row = 0;
    while (row < R || col < C) {
      if (row < R) {
        for (int left = 0, right = C - 1; left < C / 2; left++, right--) {
          if (mat[row][left] != mat[row][right]) {
            System.out.print("NO");
            return;
          }
        }
      }
      if (col < C) {
        for (int top = 0, bottom = R - 1; top < R / 2; top++, bottom--) {
          if (mat[top][col] != mat[bottom][col]) {
            System.out.print("NO");
            return;
          }
        }
      }
      row++;
      col++;
    }
    System.out.print("YES");
  }
}
