The program must accept an integer matrix of size NxN as the input. The program must find the layer in the given matrix where the sum of integers in its four corners is maximum among the other layers. Then the
program must print the integers in that layer and print the asterisks instead of the integers in the inner layers. If two or more layers of the matrix have the same maximum sum, the program must print the 
outermost layer among those layers as the output.

Example Input/Output 1:
Input:
4
6 2 4 7
1 3 7 8
6 9 0 1
1 5 2 9
Output:
6 2 4 7
1 * * 8
6 * * 1
1 5 2 9
Explanation:
The first layer of the matrix is highlighted below.
'6' '2' '4' '7'
''1' 3 7 '8'
'6' 9 0 '1'
'1' '5' '2' '9' 
The integers in the four corners of the above layer are 6, 7, 9 and 1. So their sum is 23.
The second layer of the matrix is highlighted below.
6 2 4 7
1 '3' '7' 8
6 '9' '0' 1
1 5 2 9 
The integers in the four corners of the above layer are 3, 7, 0 and 9. So their sum is 19. 
Here the maximum sum is 23. So the integers in the first layer are printed and the asterisks are printed instead of the integers in the inner layer(second layer).

Example Input/Output 2:
Input:
7
16 62 65 65 38 43 11
39 64 91 54 24 55 13
65 76 89 81 99 27 15
89 59 51 98 84 96 17 
38 24 75 18 84 24 16 
89 22 21 14 41 34 14 
19 92 24 66 81 39 12
Output:
89 81 99 
51 * 84 
75 18 84 

Example Input/Output 3:
Input:
9
5 1 8 9 9 1 4 3 3
1 5 2 3 4 7 7 6 5
3 9 4 5 1 1 9 7 9 
8 7 9 1 2 4 1 8 1 
3 9 3 8 6 1 1 9 9 
3 4 4 9 7 6 5 1 2
1 9 1 7 0 7 8 3 2
1 2 3 4 5 7 5 7 6 
5 2 0 7 1 5 4 6 1
Output:
4 5 1 1 9 
9 * * * 1 
3 * * * 1 
4 * * * 5 
1 7 0 7 8 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
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
    int currSum = 0, maxSum = 0, D = -1;
    for (int i = 0; i < N / 2; i++) {
      currSum = mat[i][i] + mat[i][N - i - 1] + mat[N - i - 1][i] + mat[N - i - 1][N - i - 1];
      if (currSum > maxSum) {
        maxSum = currSum;
        D = i;
      }
    }
    if(mat[N/2][N/2]){
      System.out.print(mat[N/2][N/2]); 
      return;
    }
    for (int i = D; i < N - D; i++) {
      for (int j = D; j < N - D; j++) {
        if (i == D || i == N - D - 1 || j == D || j == N - D - 1) {
          System.out.print(mat[i][j] + " ");
        } else {
          System.out.print("*" + " ");
        }
      }
      System.out.println();
    }
  }
}
