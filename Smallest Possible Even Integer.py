The program must accept two integers X and Y as the input. The program must print the smallest possible even integer using all the digits in the integers X and Y. If it is not possible form an even integer, the 
program must print -1 as the output.

Example Input/Output 1:
Input:
137 4276
Output:
1234776
Explanation:
The smallest possible even integer using all the digits in 137 and 4276 is 1234776. Hence the output is 1234776

Example Input/Output 2:
Input:
1357 97531
Output: 
-1

Example Input/Output 3:
Input: 
3004 560
Output: 
3000456
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def splitNum(num):
    lst = []
    while num:
        lst.append(num % 10)
        num //= 10
    return lst

X, Y = map(int, input().split())
nums = splitNum(X) + splitNum(Y)
nums.sort()
#checking for leading Zeros
if nums[0] == 0:
    for i in range(1, len(nums)):
        if nums[i] != 0:
            nums[0], nums[i] = nums[i], 0
            break
#Making the last digit as Even
for i in range(len(nums) - 1, -1, -1):
    if nums[i] % 2 == 0 and nums[-1] % 2 != 0:
        nums[-1], nums[i] = nums[i], nums[-1]
        break

if nums[-1] % 2 != 0:
    print(-1)
else:
    for dig in nums:
        print(dig, end="")

