The program must accept an integer N as the input. The program must form an integer matrix of size NxN. Then the program must fill the integers in the matrix from N to (NN) + N-1. The integers in the matrix must be
filled from the top row to the bottom row, where each row is filled from left to right. Then the program must transpose the matrix and reverse the even rows of the transposed matrix. Finally, the program must
print the modified matrix as the output.  

Example Input/Output 1:
Input:
3
Output:
3 6 9
10 7 4
5 8 11
Explanation:
Here N = 3, so an integer matrix of size 3x3 is formed.
3 4 5
6 7 8
9 10 11
After transposing the matrix, it becomes
3 6 9
4 7 10
5 8 11
After reversing the even rows of the transposed matrix, it becomes
3 6 9
10 7 4 
5 8 11

Example Input/Output 2:
Input:
6
Output:
6 12 18 24 30 36 
37 31 25 19 13 7 
8 14 20 26 32 38 
39 33 27 21 15 9 
10 16 22 28 34 40 
41 35 29 23 17 11 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = N;
    int mat[][] = new int[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        mat[j][i] = K++;
      }
    }
    for (int i = 0; i < N; i++) {
      if (i % 2 == 0) {
        for (int j = 0; j < N; j++) {
          System.out.print(mat[i][j] + " ");
        }
      } else {
        for (int j = N - 1; j >= 0; j--) {
          System.out.print(mat[i][j] + " ");
        }
      }
      System.out.println();
    }
  }
}
