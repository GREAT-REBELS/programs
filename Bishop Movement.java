--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    int X = sc.nextInt();
    int Y = sc.nextInt();
    int A = sc.nextInt();
    int B = sc.nextInt();

    int row = 0, col = 0, cnt = 0;

    //Up Left Diagonally 
    row = X - 1;
    col = Y - 1;
    while (row >= 0 && col >= 0) {
      if (row == A && col == B) {
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
    while (row < N && col < M) {
      if (row == A && col == B) {
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
    while (row >= 0 && col < M) {
      if (row == A && col == B) {
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
    while (row < N && col >= 0) {
      if (row == A && col == B) {
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
