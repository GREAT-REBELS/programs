A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people.  A square matrix mat is used to represent people at the party such that if an element of
row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.
Note: Follow 0-based indexing.

Examples:
Input: 
mat[][] = [[0 1 0],
           [0 0 0], 
           [0 1 0]]
Output: 
1
Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity. 

Input: mat[][] = [[0 1],
                  [1 0]]
Output: 
-1
Explanation: The two people at the party both know each other. None of them is a celebrity.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution {
  public int celebrity(int mat[][]) {
    int res = -1, N = mat.length;
    for (int i = 0; i < N; i++) {
      int zeroCnt = 0;
      for (int j = 0; j < N; j++) {
        if (mat[i][j] == 0)
          zeroCnt += 1;
      }
      if (zeroCnt == N) {
        res = i;
        break;
      }
    }
    if (res == -1) {
      return -1;
    }
    for (int i = 0; i < N; i++) {
      if (res != i && mat[i][res] != 1) {
        return -1;
      }
    }
    return res;
  }
}
