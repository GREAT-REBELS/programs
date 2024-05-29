In a boat, only 2 people can travel at a time. Each boat can carry a limit of weight L. There are some people standing in a queue to travel in the boat. The program must accept an integer representing the value 
of L and a list of integers representing the weights of the people in the queue. The program must print the minimum number of boats required to carry all the people from the queue as the output.

Example Input/Output 1:
Input:
3
1 2

Output: 
1
Explanation:
Here L = 3 and there are two people standing in the queue. The sum of weights of the two people is 3 (1+2) which is less than or equal to L. So both can travel in a single boat.
Hence the output is 1

Example Input/Output 2:
Input
5
5 3 5 1 4 5 3

Output: 
6
Explanation:
Here L = 5 and there are seven people standing in the queue. The people having the weight 1 and 4 can travel in a single boat, as the sum of their weights is 5 (1+4) which is less than or equal to L. The 
rest can travel on a separate boat. So the minimum number of boats required is 6. Hence the output is 6
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
L = int(input())
W = list(map(int, input().split()))
W.sort()
Lft, Rght = 0, len(W) - 1
cnt = 0

while Lft <= Rght:
    if W[Lft] + W[Rght] <= L:
        Lft += 1
        Rght -= 1
    else:
        Rght -= 1
    cnt += 1

print(cnt)
