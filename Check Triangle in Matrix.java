The program must accept an integer matrix of size NxN and an integer K as the input. The program must print YES if the top(must start from the first row) of the matrix contains a triangle with the integer K in its
border. Else the program must print NO as the output. 
Note: The value of N is always odd.

Example Input/Output 1:
Input:
7 3
8 5 3 3 6 7 4
4 0 3 0 3 4 3
3 3 7 5 9 3 4
3 3 3 3 3 3 3
7 4 7 6 5 0 4
2 8 4 2 8 9 9
4 6 5 4 8 7 3
Output:
YES
Explanation:
In the top of the given 7x7 matrix, a triangle with the integer 3 in its border is highlighted below.
8 5 3 '3' 6 7 4
4 0 '3' 0 '3' 4 3
3 '3' 7 5 9 '3' 4
'3' '3' '3' '3' '3' '3' '3'
7 4 7 6 5 0 4
2 8 4 2 8 9 9
4 6 5 4 8 7 3
So YES is printed as the output.

Example Input/Output 2:
Input:
5 0
7 8 0 4 7
1 0 5 0 8
0 0 1 0 0
4 5 8 6 3
0 1 3 7 3
Output:
NO
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = sc.nextInt();
    int mat[][] = new int[N][N];

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        mat[i][j] = sc.nextInt();
      }
    }

    for (int i = 0; i < N; i++) {
      if (mat[0][i] == K) {
        if (chkTriangle(mat, i, N, K)) {
          System.out.print("YES");
          return;
        }
      }
    }

    System.out.print("NO");
  }

  static boolean chkTriangle(int[][] mat, int pos, int N, int ele) {
    int strt = pos - 1, end = pos + 1;
    int D = 1;
    while (strt >= 0 && end < N) {
      if (mat[D][strt] == ele && mat[D][end] == ele) {
        strt--;
        end++;
        D += 1;
      } else {
        return false;
      }
    }
    for (int i = 1; i < N - 1; i++) {
      if (mat[D - 1][i] != ele) {
        return false;
      }
    }

    return true;
  }
}
