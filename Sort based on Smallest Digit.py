The program must accept N integers as the input. The program must sort the N integers in ascending order based on the smallest digit in each integer. If two or more integers have the same smallest digit, then the 
program must sort those integers in descending order. Finally, the program must print the N sorted integers as the output.

Example Input/Output 1:
Input:
7
6844 25171 53677 18072 26457 70816 59225
Output:
70816 18072 25171 59225 26457 53677 6844
Explanation:
The smallest digit in 6844 is 4.
The smallest digit in 25171 is 1.
The smallest digit in 53677 is 3.
The smallest digit in 18072 is 0.
The smallest digit in 26457 is 2.
The smallest digit in 70816 is 0.
The smallest digit in 59225 is 2.
After sorting the integers based on the smallest digit in each integer, the integers become 70816, 18072, 25171, 59225, 26457, 53677 and 6844. Hence the output is 70816 18072 25171 59225 26457 53677 6844

Example Input/Output 2:
Input: 
5 
7287 9836 47 76 99234
Output: 
99234 7287 9836 47 76
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def smallest_digit(num):
    smallest_digit = float('inf')
    while num > 0:
        smallest_digit = min(smallest_digit, num % 10)
        num = num // 10
    return smallest_digit

def custom_sort_key(num):
    return (smallest_digit(num), -num)

n = int(input())
nums = list(map(int, input().split()))
nums.sort(key=custom_sort_key)
print(*nums)
