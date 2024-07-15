The program must accept an integer matrix of size NxN and an integer X as the input. The program must rotate the matrix by X degrees in the clockwise direction. Finally, the program must print the modified matrix
as the output. If it is not possible to rotate the matrix by X degrees, the program must print INVALID as the output. The matrix rotation is possible if the value of X is a multiple of 90 (i.e., 0, 90, 180, 270, 
360, 450, 540, and so on).

Example Input/Output 1:
Input:
4
44 17 27 29
39 29 18 19
13 40 13 31
36 47 29 22
270
Output:
29 19 31 22
27 18 13 29
17 29 40 47
44 39 13 36
Explanation:
After rotating the matrix by 270 degrees, the matrix becomes.
29 19 31 22
27 18 13 29
17 29 40 47
44 39 13 36


Example Input/Output 2:
Input:
5 
35 11 98 52 8 
44 48 77 85 80 
67 77 25 44 10 
97 17 38 55 95 
32 70 78 85 69
45
Output:
INVALID
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
public class Main {
  static void transposeMatrix(int mat[][]) {
    int N = mat.length;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        int temp = mat[i][j];
        mat[i][j] = mat[j][i];
        mat[j][i] = temp;
      }
    }
  }
  static void reverseMatrix(int mat[][]) {
    int N = mat.length;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N / 2; j++) {
        int temp = mat[i][j];
        mat[i][j] = mat[i][N - j - 1];
        mat[i][N - j - 1] = temp;
      }
    }
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int mat[][] = new int[N][N];

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        mat[i][j] = sc.nextInt();
      }
    }

    int deg = sc.nextInt();

    if (deg % 90 != 0) {
      System.out.print("INVALID");
      return;
    }

    int turns = deg / 90;

    while (turns > 0) {
      transposeMatrix(mat);
      reverseMatrix(mat);
      turns--;
    }

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        System.out.print(mat[i][j] + " ");
      }
      System.out.println();
    }
  }
}
