The program must accept an integer matrix of size RxC and two integers X and Y as the input. The program must print YES if both X and Y are present diagonally(top left to bottom right diagonals and top right to 
bottom left diagonals) in the matrix. Else the program must print NO as the output.
Note: The integers X and Y always occur once in the matrix.
Example Input/Output 1:
Input:
6 5
32 94 99 26 82
51 69 52 63 17
90 36 88 55 33
93 42 73 39 28
81 31 83 53 10
12 29 85 80 87
42 80

Output:
YES
Explanation:
Here the integers 42 and 80 are present diagonally in the matrix.
32 94 99 26 82
51 69 52 63 17
90 36 88 55 33
93 42 73 39 28
81 31 83 53 10
12 29 85 80 87
So YES is printed as the output.

Example Input/Output 2:
Input:
7 5
79 40 13 74 99
73 77 32 72 87
93 82 95 57 50
61 33 54 71 16
15 92 65 10 27
35 42 90 49 47
81 83 51 11 56
42 50

Output:
YES

Example Input/Output 3:
Input:
4 6
99 56 91 65 34 39
75 42 30 64 41 89
66 29 93 35 85 68
16 33 95 74 62 54
29 41

Output:
NO
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt();
        int C = sc.nextInt();
        int[][] mat = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                mat[i][j] = sc.nextInt();
            }
        }
        int X = sc.nextInt();
        int Y = sc.nextInt();
        boolean found = false;
        for (int i = 0; i < R - 1; i++) {
            for (int j = 0; j < C; j++) {
                if (mat[i][j] == X) {
                    if (chk(mat, R, C, i, j, Y)) {
                        found = true;
                        break;
                    }
                } else if (mat[i][j] == Y) {
                    if (chk(mat, R, C, i, j, X)) {
                        found = true;
                        break;
                    }
                }
            }
            if (found) {
                break;
            }
        }
        if (found) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    static boolean chk(int[][] mat, int R, int C, int i, int j, int ele) {
        int R1 = i, C1 = j;
        int R2 = i, C2 = j;
        while (R1 < R && C1 >= 0) {
            if (mat[R1][C1] == ele) {
                return true;
            }
            R1++;
            C1--;
        }
        while (R2 < R && C2 < C) {
            if (mat[R2][C2] == ele) {
                return true;
            }
            R2++;
            C2++;
        }
        return false;
    }
}
