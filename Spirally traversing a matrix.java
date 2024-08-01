You are given a rectangular matrix, and your task is to return an array while traversing the matrix in spiral form.
Examples:
Input: matrix[][] = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15,16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

Input: matrix[][] = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution {
  public ArrayList < Integer > spirallyTraverse(int matrix[][]) {
    int strtRow = 0, strtCol = 0, endRow = matrix.length - 1, endCol = matrix[0].length - 1;
    ArrayList < Integer > ans = new ArrayList < > ();
    while (strtRow <= endRow && strtCol <= endCol) {
      for (int i = strtCol; i <= endCol; i++) {
        ans.add(matrix[strtRow][i]);
      }
      for (int i = strtRow + 1; i <= endRow; i++) {
        ans.add(matrix[i][endCol]);
      }
      for (int i = endCol - 1; i >= strtCol && strtRow != endRow; i--) {
        ans.add(matrix[endRow][i]);
      }
      for (int i = endRow - 1; i > strtRow && strtCol != endCol; i--) {
        ans.add(matrix[i][strtCol]);
      }
      strtRow++;
      strtCol++;
      endCol--;
      endRow--;
    }
    return ans;
  }
}
