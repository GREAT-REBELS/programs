The program must accept N integers and an integer K as the input. The program must print the count of subarrays that have at least one integer value greater than K as the output.   
Example Input/Output 1:
Input:
4 10
55 10 23 5

Output:
8
Explanation:
The subarrays that have at least one integer value greater than 10 are (55), (23), (55, 10), (10, 23), (23, 5), (55, 10, 23), (10, 23, 5) and (55, 10, 23, 5). So their count is 8 which is printed as the output.

Example Input/Output 2:
Input:
7 5
5 1 6 9 2 8 7

Output:
24

Example Input/Output 3:
Input:
4 33
12 25 16 21

Output:
0
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N, K = map(int, input().split())
lst = list(map(int, input().split()))
# Total number of subarrays
subArraysCnt = N * (N + 1) // 2
cnt = 0
for i in range(0, len(lst)):
    if lst[i] <= K:
        cnt += 1
    else:
        subArraysCnt -= cnt * (cnt + 1) // 2
        cnt = 0
print(subArraysCnt - cnt * (cnt + 1) // 2)
