The program must accept an integer matrix of size RxC and an integer X as the input. The program must print the largest possible square sub-matrix having the middle integer as X in the given RxC matrix as the 
output.
Note:
The size of the largest possible square sub-matrix is always odd.
The RxC integer matrix always contains exactly one occurrence of X.

Example Input/Output 1:
Input:
7 9
43 85 91 83 26 30 70 11 95
34 72 22 19 99 79 50 90 88
80 63 51 57 64 36 38 12 25
37 67 13 53 32 81 59 48 92
62 20 74 17 96 44 52 33 98
86 16 29 58 42 66 24 61 46
68 97 40 87 28 41 65 27 55
52
Output:
64 36 38 12 25
32 81 59 48 92
96 44 52 33 98
42 66 24 61 46
28 41 65 27 55

Example Input/Output 2:
Input:
5 3
12 68 60 
81 64 61 
90 55 22 
74 66 77
17 38 20 
66
Output:
90 55 22
74 66 77
17 38 20

Example Input/Output 3:
Input:
4 4
65 38 90 44
87 85 92 75
51 61 41 77
25 99 67 48
65
Output:
65
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int R = scanner.nextInt();
        int C = scanner.nextInt();
        int[][] matrix = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        int X = scanner.nextInt();
        int x = -1, y = -1;
        outerloop:
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (matrix[i][j] == X) {
                    x = i;
                    y = j;
                    break outerloop;
                }
            }
        }
        int maxSize = Math.min(Math.min(x, R - x - 1), Math.min(y, C - y - 1)) * 2 + 1;
        R = x - maxSize / 2;
        C = y - maxSize / 2;
        
        for (int i = 0; i < maxSize; i++) {
            for (int j = 0; j < maxSize; j++) {
                System.out.print(matrix[R + i][C + j]+" ");
            }
            System.out.println();
        }
        
    }
}
