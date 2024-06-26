The program must accept a list of M integers and a list of N unique integers as the input. The program must sort the first list of M integers based on the order of the integers in the second list of N integers as 
the output. If the integers in the first list are not present in the second list, the program must sort those integers in ascending order and print them last.

Example Input/Output 1:
Input: 
9 3
10 7 1 4 5 4 7 5 4
7 4 5
Output:
7 7 4 4 4 5 5 1 10
Explanation: Here M = 9, N = 3.
The integers in the first list are 10 7 1 4 5 4 7 5 4.
The integers in the second list are 7 4 5.
The first integer in the second list is 7, which is present twice in the first list.
The second integer in the second list is 4, which is present thrice in the first list.
The third integer in the second list is 5, which is present twice in the first list.
So the integers 7 7 4 4 4 5 5 are printed first.
The remaining integers in the first list are 10 and 1.
So they are sorted in ascending order and printed last.
Hence the output is 7 7 4 4 4 5 5 1 10

Example Input/Output 2:
Input: 
7 2
2 1 3 2 0 2 4
0 1
Output:
0 1 2 2 2 3 4
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from collections import Counter

N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
nums = list(map(int, input().split()))
# Count occurrences of each number in lst
counter = Counter(lst)

for num in nums:
    if num in counter:
        print(*[num] * counter[num], end=" ")  #'*' operator before a list unpacks its elements.
        counter[num] -= counter[num]

for num in lst:
    if counter[num]:
        print(
            *[num] * counter[num], end=" ")  #'*' operator before a list unpacks its elements.
        counter[num] -= counter[num]
