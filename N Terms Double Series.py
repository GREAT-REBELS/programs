The program must accept three integers N, X and Y as the input. The program must print the first N terms in the following series. x+1,Y+1 2X-1, 2Y-1, 3x + 1 3Y+1, 4X-1, 4Y-1, 5x + 1 5Y+1,....

Example Input/Output 1:
Input:
10 2 5
Output:
3 6 3 9 7 16 7 19 11 26
Explanation:
Here N = 10 x = 2 and Y = 5 The first 10 terms in the given series are 3(2+1),6(5+1),3(2*2-1), 9(2*5-1), 7(3*2 + 1),16(3*5+1) 7(4*2-1), 19(4*5-1), 
11(5*2+1) and 26(5*5+1)
Hence the output is
3 6 3 9 7 16 7 19 11 26

Example Input/Output 2:
Input:
15 9 1
Output:
10 2 17 1 28 4 35 3 46 6 53 5 64 8 71
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N, X, Y = map(int, input().split())
i = 1
while i <= N // 2:
    if i % 2:
        print(i * X + 1, i * Y + 1, end=" ")
    else:
        print(i * X - 1, i * Y - 1, end=" ")
    i += 1
if N % 2 and i % 2 == 0:
    print(i * X - 1, end=" ")
elif N % 2 and i % 2:
    print(i * X + 1, end=" ")
