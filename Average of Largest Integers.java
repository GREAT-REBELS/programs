The program must accept an integer matrix of size RxC as the input. The program must print the average of the largest integer in each row and the average of the largest integer in each column with the precision 
up to two decimal places as the output. 
  
Example Input/Output 1:
Input:
3 3
53 66 72
59 10 79
73 35 25
Output:
74.67
72.67
Explanation:
The largest integer in the 1st row is 72.
The largest integer in the 2nd row is 79. The largest integer in the 3rd row is 73.
So the average of 72, 79 and 73 is printed with the precision up to two decimal places (74.67).
The largest integer in the 1st column is 73.
The largest integer in the 2nd column is 66.
The largest integer in the 3rd column is 79.
So the average of 73, 66 and 79 is printed with the precision up to two decimal places (72.67).

Example Input/Output 2:
Input:
4 5
29 61 62 89 86
57 57 21 15 85
67 49 37 30 12
30 31 52 35 37
Output:
73.25
73.00
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
    int row = 0, col = 0;
    int rowSum = 0, colSum = 0;
    while (row < R || col < C) {
      int maxVal = Integer.MIN_VALUE;
      if (row < R) {
        for (int i = 0; i < C; i++) {
          maxVal = Math.max(maxVal, mat[row][i]);
        }
        rowSum += maxVal;
        row += 1;
      }
      maxVal = Integer.MIN_VALUE;
      if (col < C) {
        for (int j = 0; j < R; j++) {
          maxVal = Math.max(maxVal, mat[j][col]);
        }
        colSum += maxVal;
        col += 1;
      }
    }
    System.out.printf("%.2f\n", rowSum / (R * 1.0));
    System.out.printf("%.2f", colSum / (C * 1.0));
  }
}
