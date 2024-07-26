The program must accept a string S containing only alphabets as the input. The program must print the length of the longest alternating "sr" substring. Note: At least one substring "sr" is always present in the 
string S.

Example Input/Output 1:
Input:
sksrillsrsrsrsrsrskillrack
Output: 
10
Explanation:
In the given string "sksrillsrsrsrsrsrskillrack", the longest substring sr is srsrsrsrsr. So the length of the longest substring is 10.
Hence the output is 10

Example Input/Output 2:
Input:
SrsrsrAsrsrBsrcsrdsr
Output: 
4

Example Input/Output 3:
Input: 
CLsrOUSAD
Output: 
2
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
S = input()
i = 0
max_length, subStr_length = 0, 0
while i < len(S) - 1:
    if S[i] == "s" and S[i + 1] == "r":
        subStr_length += 2
        i += 1
    else:
        max_length = max(max_length, subStr_length)
        subStr_length = 0
    i += 1
max_length = max(max_length, subStr_length)
print(max_length)
