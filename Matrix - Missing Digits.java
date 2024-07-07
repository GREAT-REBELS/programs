The program must accept a matrix of size NxN containing only digits as the input. In each 3x3 submatrix in the given matrix, exactly one digit is missing among the 10 digits (0 to 9). The program must find the 
missing digit in each 3x3 submatrix and print it as the output. Note: The value of N is always divisible by 3.

Example Input/Output 1:
Input:
6
1 2 3 4 5 6
8 9 7 2 3 7
4 5 6 8 9 0
3 2 1 4 6 7
9 8 7 2 3 1
5 6 0 5 0 8
Output:
0 1 4 9
Explanation:
There are four 3x3 submatrices in the given 6x6 matrix. In the first 3x3 submatrix, the missing digit is 0.
1 2 3
8 9 7
4 5 6
Similarly, the missing digits in the remaining three 3x3 submatrices are 1, 4 and 9. Hence the output is
0 1 4 9

Example Input/Output 2:
Input
3
4 7 9
1 0 2
3 5 6
Output:
8 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[][] mat = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                mat[i][j] = scanner.nextInt();
            }
        }
        for (int i = 0; i < N; i += 3) {
            for (int j = 0; j < N; j += 3) {
                System.out.print(findMissingDigit(mat, i, j) + " ");
            }
        }
    }

    static int findMissingDigit(int[][] mat, int startRow, int startCol) {
        int D = 45; //sum of all digits from (0 to 9)
        int sum = 0;
        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                sum+=mat[i][j];
            }
        }
        return D-sum;
    }
}
