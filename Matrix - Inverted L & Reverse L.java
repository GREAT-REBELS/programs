The program must accept an integer matrix of size NxN as the input. The program must print the layers of the matrix based on the following condition. For each layer of the matrix, the program must print the 
integers from the top-right comer to the bottom-left corner (both inclusive) in the anticlockwise direction. Then the program must print the integers from the top-right comer to the bottom-left corner 
(both exclusive) in the clockwise direction.

Boundary Condition(s): 2<=N<=50
Input Format:
The first line contains N.
The next N lines, each contains N integer values separated by a space.
  
Output Format: 
The first N lines, each contains the integer value(s) separated by a space.

Example Input/Output 1:
Input:
4
69 50 96 12
65 66 11 94 
52 76 21 37
77 38 63 49
  
Output:
12 96 50 69 65 52 77 38
94 37 49 63
11 66 76
21

Example Input/Output 2:

Input:
5
36 99 61 86 95
38 55 63 58 15
64 39 84 35 43
14 89 21 34 96
68 73 28 22 37

Output:
95 86 61 99 36 38 64 14 68
15 43 96 37 22 28 73
58 63 55 39 89
35 34 21
84
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int mat[][] = new int[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        mat[i][j] = sc.nextInt();
      }
    }
    int D = 0;
    while (D < N) {
      if (D != 0) {
        System.out.println();
      }
      for (int i = N - 1; i >= D; i--) {
        System.out.print(mat[D][i] + " ");
      }
      for (int i = D + 1; i < N; i++) {
        System.out.print(mat[i][D] + " ");
      }
      System.out.println();
      for (int i = D + 1; i < N; i++) {
        System.out.print(mat[i][N - 1] + " ");
      }
      for (int i = N - 2; i > D; i--) {
        System.out.print(mat[N - 1][i] + " ");
      }
      D++;
      N--;
      System.out.println();
    }
  }
}
