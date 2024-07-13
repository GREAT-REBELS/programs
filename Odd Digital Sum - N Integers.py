The program must accept N integers as the input. The program must print the integers having the odd digital sum among the N integers as the output. If there is no such integer, the program must print -1 as the 
output. The digital sum of an integer is the recursive sum of the digits until the sum becomes a single digit.

Example Input/Output 1:
Input:
5
12 34 31 867 92

Output
12 34 867
Explanation:
The digital sum of 12 is 3, which is an odd integer. So 12 is printed as the output. The digital sum of 34 is 7, which is an odd integer. So 34 is printed as the output. The digital sum of 31 is 4, which is an 
even integer. So 31 is NOT printed. The digital sum of 867 is 3, which is an odd integer. So 867 is printed as the output. The digital sum of 92 is 2, which is an even integer. So 92 is NOT printed.
Example Input/Output 2:

Input:
4
11 22 33 454

Output:
-1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def digitalSum(num):
    digSum = 0
    while num:
        digSum += num % 10
        num = num // 10
    if digSum >= 10:
        return digitalSum(digSum)
    return digSum

N = int(input())
nums = list(map(int, input().split()))
flg = 0
for num in nums:
    if digitalSum(num) % 2:
        print(num, end=" ")
        flg = 1
if not flg:
    print(-1)
