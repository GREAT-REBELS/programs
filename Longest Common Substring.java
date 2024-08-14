You are given two strings str1 and str2. Your task is to find the length of the longest common substring among the given strings.

Examples:
Input: str1 = "ABCDGH", str2 = "ACDGHR"
Output: 4
Explanation: The longest common substring is "CDGH" which has length 4.

Input: str1 = "ABC", str2 = "ACB"
Output: 1
Explanation: The longest common substrings are "A", "B", "C" all having length 1.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution {
    public int longestCommonSubstr(String str1, String str2) {
        char[] arr1 = str1.toCharArray();
        char[] arr2 = str2.toCharArray();
        int[][] dp = new int[arr1.length+1][arr2.length+1];
        int res = 0;
        for(int i=1;i<=arr1.length;i++){
            for(int j=1;j<=arr2.length;j++){
                if(arr1[i-1] == arr2[j-1]){
                    dp[i][j] = dp[i-1][j-1]+1; 
                    res = Math.max(dp[i][j],res);
                }
            }
        }
        return res;
    }
}
