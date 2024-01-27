------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.nextLine();
    String limit = "9".repeat(str.length());
    boolean flg = false;
    char arr1[] = str.toCharArray();
    for (int i = Integer.valueOf(str) + 1; i <= Integer.valueOf(limit) + 1; i++) {
      char arr2[] = String.valueOf(i).toCharArray();
      Arrays.sort(arr1);
      Arrays.sort(arr2);
      if (Arrays.equals(arr1, arr2)) {
        System.out.print(i);
        flg = true;
        break;
      }
    }
    if (!flg) {
      System.out.print("-1");
    }
  }
}
