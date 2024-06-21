The program must accept three integers X, Y and Z as the input. The program must print YES if Z can be formed by the sum of integers using X and Y. Else the program must print NO as the output.

Example Input/Output 1:
Input: 
3 5 22
Output: 
YES
Explanation:
Here X = 3, Y = 5 and Z = 22.
The integer 22 is formed by the sum of 3, 3, 3, 3, 5 and 5. So YES is printed as the output.

Example Input/Output 2:
Input:
11 7 23
Output: 
NO

Example Input/Output 3:
Input: 
11 13 76
Output: 
YES
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
X, Y, Z = map(int, input().split())
for i in range(Z // X + 1):
    rem = (Z - X * i)  # Calculating the remaining sum needed to reach 𝑍 after subtracting X*i
    if (rem >= 0 and rem % Y == 0):  # Checking If the remaining is non-negative and is divisible by Y
        print("YES")
        quit()
print("NO")
