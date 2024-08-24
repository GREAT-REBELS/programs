You are given weights and values of items, and put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val and wt which represent values and weights associated with items respectively. Also given an integer W which represents knapsack capacity, find out the maximum sum values 
subset of val[] such that the sum of the weights of the corresponding subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don't pick it (0-1 property).

Examples :
Input: W = 4, val[] = {1,2,3}, wt[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 
   
Input: W = 3, val[] = {1,2,3}, wt[] = {4,5,6}
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution {
    static int knapSack(int w, int wt[], int val[]) {
        int n = val.length;
        int dp[][] = new int[n + 1][w + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= w; j++) {
                if (wt[i - 1] <= j) {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[n][w];
    }
}
