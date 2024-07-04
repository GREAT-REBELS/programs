The program must accept N integers and an integer K as the input. The program must print the integers in the subarray of size K having the minimum sum. Then the program must print the integers in the subarray of 
size K having the maximum sum. If two or more subarrays of size K have the same minimum sum or the maximum sum, the program must print the first occurring subarray as the output

Example Input/Output 1:
Input:
7
7 2 1 4 5 3 6
2
Output:
2 1
7 2
Explanation:
Here K-2. There is only one subarray having the minimum sum 3 is 2 and 1. So they are printed in the first line.
There are two subarrays having the same maximum sum 9, they are 7 2 and 3 6. So the integers in the first occurring subarray (72) are printed in the second 
line.

Example Input/Output 2:
Input:
6
25 16 14 78 19 12
4
Output:
14 78 19 12
25 16 14 78
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
arr = list(map(int, input().split()))
K = int(input())
currSubArr_sum = sum(arr[:K])
minInd, maxInd = 0, 0
minSum, maxSum = currSubArr_sum, currSubArr_sum
for i in range(K, N):
    currSubArr_sum = (currSubArr_sum + arr[i]) - arr[i - K]
    if currSubArr_sum > maxSum:
        maxSum = currSubArr_sum
        maxInd = i - K + 1
    if currSubArr_sum < minSum:
        minSum = currSubArr_sum
        minInd = i - K + 1
print(*arr[minInd : minInd + K])
print(*arr[maxInd : maxInd + K])
