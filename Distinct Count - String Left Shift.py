The program must accept a string S containing only alphabets as the input. The program must print the count of distinct string values formed when shifting the alphabets in S to the left as the output. 

Example Input/Output 1:
Input:
abab
Output:
2
Explanation:
The possible combinations when shifting the alphabets in abab to the left are baba, abab,
baba and abab.
Here the distinct strings are baba and abab.
So the count 2 is printed as the output.

Example Input/Output 2:
Input:
aSasa
Output:
5

Example Input/Output 3:
Input:
AABBAAABBA
Output: 
5
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
S = input()
res = set()
for _ in range(len(S)):
    S = S[1:] + S[0]
    res.add(S)
print(len(res))
