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
