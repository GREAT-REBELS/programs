Given an array nums[], construct a Product Array nums[] such that nums[i] is equal to the product of all the elements of nums except nums[i].

Examples:
Input: nums[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.

Input: nums[] = [12,0]
Output: [0, 12]
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        prefix = suffix = 1
        for i in range(n):
            res[i] = prefix 
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= suffix 
            suffix *= nums[i]
        return res
