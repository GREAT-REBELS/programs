There is an RxC chessboard. The chessboard contains one bishop, one pawn and empty squares. The indices of the bishop (X, Y) and the pawn (M, N) are passed as the input to the program. The bishop moves in any 
direction diagonally. If the pawn is encountered or meets the end of the board, the movement of bishop stops. The program must print the number of squares that the bishop can move as the output.

Example Input/Output 1:
Input:
7 7
3 3
6 0
  
Output
11
Explanation:
The bishop movable squares are highlighted below.
- * * * * * -
* - * * * - *
* * - * - * *
* * * B * * *
* * - * - * *
* - * * * - *
P * * * * * -
Hence the count is 11.

Example Input/Output 2:
Input:
5 6
1 1
3 1

Output:
6
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int R = sc.nextInt();
    int C = sc.nextInt();
    int X = sc.nextInt();
    int Y = sc.nextInt();
    int M = sc.nextInt();
    int N = sc.nextInt();

    int row = 0, col = 0, cnt = 0;

    //Up Left Diagonally 
    row = X - 1;
    col = Y - 1;
    while (row >= 0 && col >= 0) {
      if (row == M && col == N) {
        break;
      } else {
        row--;
        col--;
        cnt++;
      }
    }
    //Down Left Diagonally
    row = X + 1;
    col = Y + 1;
    while (row < R && col < C) {
      if (row == M && col == N) {
        break;
      } else {
        row++;
        col++;
        cnt++;
      }
    }
    //Up Right Diagonally 
    row = X - 1;
    col = Y + 1;
    while (row >= 0 && col < C) {
      if (row == M && col == N) {
        break;
      } else {
        row--;
        col++;
        cnt++;
      }
    }
    //Down Right Diagonally 
    row = X + 1;
    col = Y - 1;
    while (row < R && col >= 0) {
      if (row == M && col == N) {
        break;
      } else {
        row++;
        col--;
        cnt++;
      }
    }
    System.out.print(cnt);

  }
}
