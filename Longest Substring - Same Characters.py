The program must accept a string S as the input. The program must print all possible longest substring values that are formed using a character in the order of their occurrence. If there is no such substring in S,
the program must print -1 as the output. Note: The string S is case insensitive. 

Example Input/Output 1:
Input: 
aaabbccc
Output:
aaa ccc
Explanation:
In the given string aaabbccc, the longest possible substring values that are formed using a character are aaa and ccc. Hence the output is aaa ccc

Example Input/Output 2:
Input: 
XXyyyy33333xxxZZzzzAaAaA
Output: 
33333 ZZzzz AaAaA

Example Input/Output 3: 
Input:
pqrs@87
Output:
-1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = input()
subStrings = []
i, K = 0, 0
maxLen = 0
while i < len(word):
    K = i
    while i + 1 < len(word) and word[i].lower() == word[i + 1].lower():
        i += 1
    i += 1
    maxLen = max(maxLen, len(word[K:i])) 
    if len(word[K:i]) >= maxLen:
        subStrings.append(word[K:i])
if maxLen == 1:
    print(-1)
    quit()
for subStr in subStrings:
    if len(subStr) == maxLen:
        print(subStr, end=" ")
