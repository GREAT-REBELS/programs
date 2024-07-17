The program must accept the prices of N ice creams and the total amount T with a boy as the input. The program must print the maximum number of ice creams that can be bought by the boy as the output.

Example Input/Output 1:
Input:
5 29
5 10 12 4 15
Output:
3
Explanation:
The prices of the 5 ice creams are 5 10 12 4 15.
T = 29
The possible ways the boy can buy ice creams are given below.
5 10 12 (27 <= 29)
5 10 4 (19 <= 29)
5 12 4 (21 <= 29)
54 15 (24 <=29)
10 12 4 (26 <= 29)
10 4 15 (29 <= 29)
The maximum number of ice creams that can be bought by the boy is 3. So 3 is printed as the output.

Example Input/Output 2:
Input
6 60
10 4 15 3 6 9
Output:
6
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N, Total = map(int, input().split())
Prices = list(map(int, input().split()))
if sum(Prices) <= Total:
    print(len(Prices))
    quit()
Prices.sort()
cost, count = 0, 0
for price in Prices:
    cost += price
    if cost > Total:
        print(count)
        quit()
    count += 1
    
