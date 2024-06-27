The program must accept N integers as the input. The program must print the smallest positive integer S which is not equal to the sum of any combination of integers among the given N integers as the output.

Example Input/Output 1:
Input:
6
1 2 4 9 5 1
Output: 
23
Explanation:
The integer 1 is not possible as 1 is present in the given 6 integers.
The integer 2 is not possible as 2 is present in the given 6 integers.
The integer 3 is not possible as 1 and 2 are present in the given 6 integers.
The integer 4 is not possible as 4 is present in the given 6 integers. The integer 5 is not possible as 5 is present in the given 6 integers. The integer 6 is not possible as 1 and 5 are present in the given 6
integers. Similarly, up to 22 is not possible, because there is a combination that provides the same value. 
The smallest integer value which is not equal to the sum of any combination of integers among the given 6 integers is 23.
So 23 is printed as the output.

Example Input/Output 2:
Input:
5
17 9 15 2 4
Output:
1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
sum_ = 1
for num in nums:
    if num > sum_:
        break
    sum_ += num
print(sum_)
