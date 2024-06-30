The program must accept two integers M and N as the input. The program must form two lists of integers from 1 to M and 1 to N respectively. Then the program must print the count of pairs of integers C among the 
two lists based on the following conditions.
- The sum of integers in each pair must be divisible by 5.
- An integer in a given list cannot be used more than once to form a pair.

Example Input/Output 1:
Input: 
7 5
Output: 
5
Explanation:
The integers from 1 to 7 are 1, 2, 3, 4, 5, 6 and 7.
The integers from 1 to 5 are 1, 2, 3, 4 are 5.
The 5 possible pairs are given below. (7 and 3 in not considered as already 3 in the second list has been used with 2).
1 4
2 3
3 2
4 1
5 5

Example Input/Output 2:
Input:
16 18
Output: 
15
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
M, N = map(int, input().split())
lst = []
for i in range(1, N + 1):
    lst.append(i)
cnt = 0
for i in range(1, M + 1):
    for j in range(N):
        if (i + lst[j]) % 5 == 0 and lst[j] != -1:
            cnt += 1
            lst[j] = -1
            break
print(cnt)
