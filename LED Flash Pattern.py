In an NxN LED light matrix, each LED has a lumen (how bright an LED is). The NxN LED matrixvhas a pattern to flash, which is given below.
- Initially, all the LEDs flashing in the matrix (at t = 1 ) Then it changes the flashing mode every second.
- At t = 2 all the LEDs in the last row and the last column will not flash.
- At t = 3 all the LEDs in the first row and the first column will not flash.
- At = 4 all the LEDs in the last two rows and the last two columns will not flash.
- At = 5 all the LEDs in the first two rows and the first two columns will not flash. Similarly, the LEDs in the matrix are flashing. It will repeat the flashing pattern when all the LEDs not flashing at a time.
The lumen value of each LED in the matrix is passed as the input to the program. The program must print the highest lumen of the LED at every second in the above-mentioned flashing pattern.

Example Input/Output 1:
Input:
4
1 2 8 4
6 3 4 1
5 6 7 2
9 3 4 9
Output:
9 8 9 6 9 1 9 
Explanation:
t = 1 the lumen values of the flashing LED's are given below.
1 2 8 4
6 3 4 1
5 6 7 2
9 3 4 9
Here 9 is the highest lumen value.
At t = 2 the lumen values of the flashing LEDs are given below.
1 2 8
6 3 4
5 6 7
Here 8 is the highest lumen value.
At t = 3 the lumen values of the flashing LEDs are given Below.
3 4 1
6 7 2
3 4 9
Here 9 is the highest lumen value.
At t = 4 the lumen values of the flashing LEDs are given below.
1 2
6 3
Here 6 is the highest lumen value.
Similarly, at t = 5 9 is the highest lumen value.
At t = 6, 1 is the only highest lumen value.
At t = 7, 9 is the only highest lumen value.
At t = 8, the pattern ends as all the LEDs not flashing at this time.
Hence the output is
9 8 9 6 9 1 9 

Example Input/Output 2:
Input:
5
67 82 13 18 76
91 43 25 79 52 
99 31 37 51 53
95 82 67 54 83 
39 23 92 61 84
Output:
99 99 92 99 92 91 84 67 84
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
T = 1
D1 = 0
D2 = N - 1
while True:
    highest_lumen = 0
    if T % 2:
        for i in range(D1, N):
            for j in range(D1, N):
                highest_lumen = max(highest_lumen, matrix[i][j])
        D1 += 1
    else:
        for i in range(0, D2):
            for j in range(0, D2):
                highest_lumen = max(highest_lumen, matrix[i][j])
        D2 -= 1
    if highest_lumen == 0:
        break
    print(highest_lumen, end=" ")
    T += 1
