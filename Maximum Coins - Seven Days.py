The 7 days in a week from Sunday to Saturday are numbered from 1 to 7. On Sunday and Saturday, a magical pot will double the gold coins put in it. On remaining days, the magical pot will just increase the coins 
by 5. The program must accept two integers N and D representing the number of gold coins in the pot and the starting day respectively. The program must print the maximum coins M that can be obtained using the 
magical pot for seven days continuously.
Example Input/Output 1:
Input:
1 7
Output: 
29
Explanation:
Initially, the number of gold coins in the pot is 1 and the starting day is 7(Saturday).
On day 7, the magical pot doubles the gold coins as it is Saturday.
So the number of gold coins in the pot becomes 2 (1*2 = 2).
On day 1, the magical pot doubles the gold coins as it is Sunday.
So the number of gold coins in the pot becomes 4 (2*2 = 4).
On day 2, the magical pot just increases the gold coins by 5 as it is Monday.
So the number of gold coins in the pot becomes 9 (4+5 = 9).
Similarly, on day 3, the number of gold coins in the pot becomes 14 (9+5=14).
On day 4, the number of gold coins in the pot becomes 19 (14+5 = 19).
On day 5, the number of gold coins in the pot becomes 24 (19+5 = 24).
On day 6, the number of gold coins in the pot becomes 29 (24+5 = 29).
Hence the output is 29

Example Input/Output 2:
Input:
50 2
Output: 
300
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N, D = map(int, input().split())
i = 0
while i < 7:
    D = D % 7
    if D == 0 or D == 1:  # 0 Indiactes Saturday and 1 Indicates Sunday
        N *= 2
    else:
        N += 5
    i += 1
    D += 1
print(N)

(OR) 
It is said that to calculate for seven days continously, So It will include all the days in a week.On Saturday and Sunday Totally the magical pot will quadruple coins and from Monday to Friday the magical pot 
will increase by total of 25 coins
N, D = map(int, input().split())
print((N + 25) * 4)

