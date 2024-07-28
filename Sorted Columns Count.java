The program must accept an integer matrix of size RxC as the input. The program must print the count of columns in the matrix where the integers are sorted in descending order as the output

Example Input/Output 1:
Input:
5 4
12 100 67 89
61 88 59 79
86 35 46 65
37 30 25 36
32 25 13 32
Output: 
3
Explanation:
In the given 5x4 matrix, the integers in the 2nd, 3rd and 4th columns are sorted in descending order.
So 3 is printed as the output.

Example Input/Output 2:
Input:
4 4
31 73 29 87
77 44 66 46
10 44 9 90
3 1 39 34
Output: 
2
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    int res = 0;
    for (int i = 0; i < C; i++) {
      int flg = 1;
      for (int j = 0; j < R-1; j++) {
        if (mat[j][i] < mat[j+1][i]){
          flg = 0;
          break;
        }
      }
      if (flg == 1)
        res += 1;
    }
    System.out.print(res);
  }
}
