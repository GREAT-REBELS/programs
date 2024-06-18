The program must accept the first term F and the common difference D of an arithmetic progression as the input. The program also accepts the four integer values N, T, X and Y as the input to the program. The 
program must print the output based on the following conditions. 
- In the first line, the program must print the Nth term in the arithmetic progression as the output.
- In the second line, if the given term T is present in the arithmetic progression then the program must print the position of the term T. Else the program must print the string value "Not Found" as the output.
- In the third line, the program must print the absolute difference between the xth term and the yth term in the arithmetic progression as the output.
Note: The common difference D is always non-zero.
Example Input/Output 1:
Input:
1 4
7
21
13 17
Output:
25
6
16
Explanation:
First Term = 1.
Common Difference = 4.
The integers in the arithmetic progression are 1, 5, 9, 13, 17, 21, 25 and so on. The 7th term in the arithmetic progression is 25. So 25 is printed in the first line.
The position of the term 21 in the arithmetic progression is 6. So 6 is printed in the second line.
The absolute difference between the 13th term and the 17th term is 16 (49-65). So 16 is printed in the third line.

Example Input/Output 2:
Input:
0 -3
3
-14
4 7
Output:
-6
Not Found
9
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
F, D = map(int, input().split())
N = int(input())
T = int(input())
X, Y = map(int, input().split())
# The formula to find nth term of ap is, F+(N-1)D where F is the first term and D is the common difference
print(F + (N - 1) * D)
if (T - F) % D == 0 and (T - F) // D >= 0:
    num, K = F, 0
    while num != T:
        num = F + (K - 1) * D
        print(num)
        K += 1
    print(K - 1)
else:
    print("Not Found")
print(abs((F + (Y - 1) * D) - (F + (X - 1) * D)))
