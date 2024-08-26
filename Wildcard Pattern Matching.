Given two strings pattern and str which may be of different size, You have to return 1 if the wildcard pattern i.e. pattern, matches with str else return 0. All characters of the string str and pattern always
belong to the Alphanumeric characters.
The wildcard pattern can include the characters ? and *
‘?’ – matches any single character.
‘*’ – Matches any sequence of characters (including the empty sequence).
Note: The matching should cover the entire str (not partial str).

Examples:
Input: pattern = "ba*a?", str = "baaabab"
Output: 1
Explanation: replace '*' with "aab" and '?' with 'b'.

Input: pattern = "a*ab", str = "baaabab"
Output: 0
Explanation: Because in string pattern character 'a' at first position, pattern and str can't be matched.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution {
    public int wildCard(String p, String s) {
        int m = s.length();
        int n = p.length();
        int[][] match = new int[m + 1][n + 1]; 
        match[0][0] = 1;      
        for (int j = 1; j <= n; j++) {
            match[0][j] = (p.charAt(j - 1) == '*' && match[0][j - 1] == 1) ? 1 : 0;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '?') {
                    match[i][j] = match[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    match[i][j] = (match[i - 1][j] == 1 || match[i][j - 1] == 1) ? 1 : 0;
                } else {
                    match[i][j] = 0;
                }
            }
        }    
        return match[m][n];
    }
}
