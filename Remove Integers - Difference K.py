The program must accept a list of integers and an integer K as the input. The program must print the count of the minimum number of integers that should be removed from the list of integers such that the 
difference between the maximum and the minimum integers in the list is less than or equal to K as the output.
Example Input/Output 1:
Input:
1 3 4 9 10 11 12 17 20
4
Output: 
5
Explanation:
After removing the integers 1, 3, 4, 17 and 20 from the list, the list becomes 9 10 11 12. Here, the difference between the maximum and the minimum is 3 (12-9) which is less than 4. So the minimum count to remove
is 5.

Example Input/Output 2:
Input:
7 8 6 5 4 3
5
Output: 
0

Example Input/Output 3:
Input:
30 10 20 40 15 70 90 16 100
5
Output: 
6
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nums = list(map(int,input().split()))
K = int(input())
left = 0 
len_ = len(nums)
min_removal = len_
nums.sort()
for right in range(len_):
    while nums[right] - nums[left] > K:
        left+=1
    min_removal = min(min_removal,len_-(right-left+1)) 
print(min_removal)
        
    
