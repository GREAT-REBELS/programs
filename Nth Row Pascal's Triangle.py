The program must accept an integer N as the input. The program must print the Nth row in Pascal's triangle as the output. Pascal's triangle is a triangular array constructed by summing adjacent integers in 
preceding rows.
Example Input/Output 1:
Input:
5

Output:
1 4 6 4 1
Explanation:
The first 5 rows of Pascal's triangle are given below.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
The 5th row in Pascal's triangle is 1 4 6 4 1. So they are printed as the output.

Example Input/Output 2:
Input:
10

Output:
19 36 84 126 126 84 36 9 1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
c = 1
for i in range(1, N + 1):
    print(c, end=" ")
    c = c * (N - i) // i
