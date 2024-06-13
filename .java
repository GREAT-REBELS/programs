import java.util.*;
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
    int len = N + N;
    int strt = N - 1;
    int end = N;
    for (int i = 0; i < len; i++) {
      for (int j = 0; j < len; j++) {
        if (i != 0 && i != len - 1 && j != 0 && j != len - 1) {
          if (j >= strt && j <= end || j >= end && j <= strt) {
            System.out.print("*" + " ");
          } else {
            System.out.print(mat[i % N][j % N] + " ");
          }
        } else {
          System.out.print(mat[i % N][j % N] + " ");
        }
      }
      if (i != 0 && i != len - 1) {
        if (i < len / 2) {
          strt -= 1;
          end += 1;
        } else {
          strt += 2;
          end -= 2;
        }
      }
      System.out.println();
    }
  }
}
