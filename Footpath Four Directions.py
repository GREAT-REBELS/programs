The program must accept four integers N, W, S and E representing the number of steps in the directions North, West, South and East respectively. A person is standing in a position, and he
moves N steps towards the north, then he moves W steps towards the west, then he moves S steps towards the south and E steps towards the east. The program must print the output based on the following conditions.
- Initially, the person moves N steps towards the north, so the program prints "N" N times towards the north. D
- Then the person moves W steps towards the west, so the program prints "W" W times towards the west.
- Then the person moves S steps towards the south, so the program prints "S" S times towards the south.
- Then the person moves E steps towards the east, so the program prints "E" E times towards the east.
The person stops moving when he crosses his path or there are no moves in the east. The program must print the hyphens instead of empty places to make the person's footpath more clear.

Example Input/Output 1:
Input: 
5 7 6 5
Output:
WWWWWWWN
S------N
S------N
S------N
S------- 
SEEEEE--
Explanation:
Here N = 5, W = 7, S = 6 and E = 5. Initially, the person moves 5 steps towards the north (N). Then the person moves 7 steps towards the west (W). Then the person 
moves 6 steps towards the south (S). Then the person moves 5 steps towards the east (E). Then the empty places are filled with hyphens.
Hence the output is
WWWWWWWN
S------N
S------N
S------N
S------- 
SEEEEE--

Example Input/Output 2:
Input:
4 3 3 3
Output:
S--N
S--N
SEEE

Example Input/Output 3:
Input:
6 6 6 10
Output:
WWWWWWN----
S-----N----
S-----N----
S-----N----
S-----N----
SEEEEEEEEEE

Example Input/Output 4:
Input:
10 5 4 8
Output:
W W W W W N
S - - - - N
S - - - - N
S - - - - N
S E E E E E
- - - - - N
- - - - - N
- - - - - N
- - - - - N
- - - - - N
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N, W, S, E = map(int, input().split())
row = max(N, S) + 1 if S >= N else max(N, S)
col = E + 1 if N <= S and W < E else W + 1
mat = [["-"] * col for _ in range(row)]
for i in range(N - 1, -1, -1):
    mat[i][W] = "N"
for i in range(W - 1, -1, -1):
    mat[0][i] = "W"
for i in range(1, S + 1):
    mat[i][0] = "S"
for i in range(1, E + 1):
    if i < col:
        mat[S][i] = "E"
    else:
        break
for i in range(row):
    print(''.join(mat[i]))
