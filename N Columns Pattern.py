The program must accept N integers as the input. For each integer X among the N integers, the program must print the integer X for X times. Each line in the output must contain at most N integers.

Example Input/Output 1:
Input:
5
3 5 1 8 7
Output:
3 3 3 5 5
5 5 5 1 8
8 8 8 8 8
8 8 7 7 7
7 7 7 7
Explanation:
The value of N is 5, so each line of the output contains at most 5 integers.
The first integer 3. So three 3's are printed in the first line.
The second integer 5. So two 5's are printed in the first line and the remaining three 5's are printed in the second line.
The third integer 1. So only one 1 is printed in the second line.
Similarly, the remaining 2 integers 8 and 7 are printed in the same way.
Hence the output is
3 3 3 5 5
5 5 5 1 8
8 8 8 8 8
8 8 7 7 7
7 7 7 7

Example Input/Output 2:
Input:
2
12 6
Output:
12 12
12 12
12 12
12 12
12 12
12 12
6 6
6 6
6 6
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
lst = list(map(int, input().split()))
j = 0
for i in lst:
    D = i
    while j < N:
        if i:
            print(D, end=" ")
            i -= 1
            j += 1
        else:
            break
        if j == N:
            j = 0
            print()
