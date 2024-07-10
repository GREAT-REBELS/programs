The program must accept three integers R, B and N as the input. R represents the number of red balls. B represents the number of blue balls. The program must print all possible combinations of getting N balls 
from the R red balls and the B blue balls as the output.
Note:
- Each possible combination contains the number of red balls followed by the number of blue balls.
- The number of red balls in the possible combinations must be sorted in descending order.

Example Input/Output 1:
Input:
5 4 7
Output:
5 2
4 3
3 4
Explanation:
Here N-7, the all possible combinations of getting 7 balls from the 5 red balls and the 4 blue balls are given below.
5 2
4 3
3 4

Example Input/Output 2:
Input:
13 10 4
Output:
4 0
3 1
2 2
1 3
0 4
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
R, B, N = map(int, input().split())
for r in range(R, -1, -1):
    b = N - r  #'b' is the number of blue balls needed to make combination of 'N'
    if (b >= 0 and b <= B):  # checking if 'b' is an non-negative number and no of blue balls needed is less than or equal to available blue balls
        print(r, b)
