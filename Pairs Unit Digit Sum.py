The program must accept an integer N as the input. The program must print the count of unique pairs of digits that can be formed using the digits of N (expect the unit digit), where the sum of digits in each pair
is equal to the unit digit of N as the output. If there is no such pair, the program must print -1 as the output.

Example Input/Output 1:
Input: 
2464538
Output: 
3
Explanation:
The unit digit of 2464538 is 8.
The 3 unique pairs of digits are given below.
(2, 6) -> 2+6=8
(4, 4) -> 4+4=8
(5, 3) -> 5+3=8

Example Input/Output 2:
Input:
345672
Output: 
-1

Example Input/Output 3:
Input: 
7117471178
Output: 
1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
nums = []
unit_dig = N % 10
N = N//10
while N > 0:
    nums.append(N % 10)
    N = N // 10
pairs_set = set()
for i in range(0, len(nums)):
    complement = unit_dig - nums[i]
    if (complement in nums and (nums[i], complement) not in pairs_set and (complement, nums[i]) not in pairs_set):
        if complement == nums[i] and nums.count(complement) > 1:
            pairs_set.add((nums[i], complement))
        elif complement != nums[i]:
            pairs_set.add((nums[i], complement))

print(len(pairs_set) if len(pairs_set) else -1)

