The program must accept a string S and two integers R, N as the input. The string S always contains Os and 1s. The program must expand the string S based on the first R characters.
- If the character is 0, the program must insert 1 after 0 (0 -> 01). 
- If the character is 1, the program must insert 0 after 1 (1 -> 10).
Finally, the program must print the Nth character in the modified string S. Note: At least N characters are always present in the modified string S.

Example Input/Output 1:
Input: 
101
2 3
Output:
0
Explanation:
Here R = 2 and N = 3.
The first character is 1, so 0 is inserted after 1.
The second character is 0, so 1 is inserted after 0.
Now the string becomes 10011. The 3rd character in the above string is 0, which is printed as the output.

Example Input/Output 2:
Input:
11
1 3
Output:
1

Example Input/Output 3:
Input:
11011
5 10
Output: 
0
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
binaryStr = input()
R,N = map(int,input().split())
expandedBinaryStr = []
cnt = 0
for ch in binaryStr:
    expandedBinaryStr.append(ch)
    if cnt<R:
        if ch=='1':
            expandedBinaryStr.append('0')
        else:
            expandedBinaryStr.append('1')
    cnt+=1
print(expandedBinaryStr[N-1])
