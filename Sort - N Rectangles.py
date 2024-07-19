The program must accept the length L and the breadth B of N rectangles as the input. The program must find the area of N rectangles. Then the program must sort the N rectangles in ascending order based on their
area. If two or more rectangles have the same area, the program must sort N rectangles in ascending order based on their length. Finally, the program must print the length, the breadth and the area of the sorted
rectangles as the output.

Example Input/Output 1:
Input:
5
5 7
2 5
3 2
2 3
4 6
Output:
2 3 6
3 2 6
2 5 10
4 6 24
5 7 35
Explanation:
The area of the first rectangle is 35 (5*7).
The area of the second rectangle is 10 (2*5).
The area of the third rectangle is 6 (3*2).
The area of the fourth rectangle is 6 (2*3). 
The area of the fifth rectangle is 24 (4*6).
After sorting the rectangles based on the given conditions, the rectangles become
2 3 6
3 2 6
2 5 10
4 6 24
5 7 35

Example Input/Output 2:
Input:
6
20 5
3 20
15 4
10 10
11 2
5 5
Output:
11 2 22
5 5 25
3 20 60
15 4 60
10 10 100
20 5 100
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
rectangles = []
for _ in range(N):
    length, breadth = map(int, input().split())
    rectangles.append([length, breadth, length * breadth])
rectangles.sort(key=lambda X: (X[2], X[0]))
for length, breadth, area in rectangles:
    print(length, breadth, area)
