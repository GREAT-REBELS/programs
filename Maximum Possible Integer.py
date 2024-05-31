The program must accept an integer N as the input. The program must print the maximum possible integer X which is less than N, but the sum of digits in X is greater than the sum of digits in N. If there is no 
such integer, the program must print the integer N as it is.

Example Input/Output 1:
Input: 
35

Output: 
29
Explanation:
Here N = 35. The sum of digits in 35 is 8.
The maximum possible integer X which is less than 35 and having the sum of digits greater than 8 is 29.
So 29 is printed as the output.

Example Input/Output 2:
Input: 
48

Output: 
48
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def digSum(N):
    sum_ = 0
    while N > 0:
        sum_ += N % 10
        N //= 10
    return sum_


N = int(input())
D = N - 1
K = digSum(N)
while D:
    if digSum(D) > K:
        print(D)
        quit()
    D -= 1
print(N)
