The program must accept an integer matrix of size RxC, the position (X, Y) of a cell and a string P representing a path containing the characters >, v, < and as the input. The path P always starts from the given
cell (X, Y). The program must print the integers which are present in the given path P. The four characters in the path P representing the four directions.
- The character > indicates that the next cell is on the right.
- The character v indicates that the next cell is on the bottom.
- The character < indicates that the next cell is on the left.
- The character ^ indicates that the next cell is on the top.
If the path P is not valid (i.e., if it crosses the edges of the matrix), the program must print the string value "Invalid Path" as the output.

Example Input/Output 1:
Input:
5 5
1 2 3 4 5
6 7 8 9 0
1 2 3 4 5
6 7 8 9 0
1 2 3 4 5
1 2

Output:
2 3 4 5 0
Explanation:
The starting position of the path is (1, 2).
The path P is >>>v.
The integers present in the given path P are highlighted below.
1 '2' '3' '4' '5'
6 7 8 9 '0'
1 2 3 4 5
6 7 8 9 0
1 2 3 4 5
Hence the output is
2 3 4 5 0

Example Input/Output 2:
Input:
3 4
1 2 3 4
5 6 7 8
1 2 3 0
1 1
>>w<v>
  
Output:
Invalid Path
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
        
        int row = sc.nextInt() - 1;
        int col = sc.nextInt() - 1;
        String P = sc.next();
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(mat[row][col])
        for (int i = 0; i < P.length(); i++) {
            char ch = P.charAt(i);
            if(ch == '>') {
                col++;
            } else if(ch == '<') {
                col--;
            } else if(ch == '^') {
                row--;
            } else{
                row++;
            }
            if (row >= 0 && row < R && col >= 0 && col < C) {
                arr.add(mat[row][col]);
            } else {
                System.out.print("Invalid Path");
                return;
            }
        }
        for(int num : arr){
            System.out.print(num+" ");
        }
    }
}
