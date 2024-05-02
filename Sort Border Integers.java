

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int R = sc.nextInt();
    int C = sc.nextInt();
    int mat[][] = new int[R][C];
    int arr[] = new int[2000];
    int k = 0;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        mat[i][j] = sc.nextInt();
        if (i == 0 || j == 0 || i == R - 1 || j == C - 1) {
          //Storing border elements in an array
          arr[k++] = mat[i][j];
        }
      }
    }
    int strt = 0, end = k - 1;
    //sorting the array
    for (int i = 0; i < k; i++) {
      for (int j = i + 1; j < k; j++) {
        if (arr[i] > arr[j]) {
          int temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
        }
      }
    }
    //printing the first row of the array
    for (int i = 0; i < C; i++) {
      System.out.print(arr[strt++] + " ");
    }
    System.out.println();

    for (int i = 1; i < R - 1; i++) {
      for (int j = 0; j < C; j++) {
        if (j == 0) {
          System.out.print(arr[end--] + " ");
        } else if (j == C - 1) {
          System.out.print(arr[strt++] + " ");
        } else {
          System.out.print(mat[i][j] + " ");
        }
      }
    }
    System.out.println();
    //printing the last row of the array
    for (int i = 0; i < C; i++) {
      System.out.print(arr[end--] + " ");
    }
    
  }
}
