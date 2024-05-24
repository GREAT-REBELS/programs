The program must accept an integer matrix of size N'N as the input. The program must rotate the matrix by 45 degrees in the clockwise direction. Then the program must print the rotated matrix and print 
asterisks instead of empty places as the output.

Boundary Condition(s): 3<= N <= 100
Input Format:
The first line contains N.
The next N lines, each contains N integers separated by a space.

Output Format:
The first (2N)-1 lines containing the rotated matrix.

Example Input/Output 1:
Input:
3
123
456
789

Output:
**1
*42
753
*86
**9
  
Explanation:
After rotating the matrix by 45 degrees in the clockwise direction, the matrix becomes
  1 
 4 2
7 5 3
 8 6
  9 
So the rotated matrix is printed and the asterisks are printed instead of empty places,

Example Input/Output 2:
Input
4
13 21 3649
55 65 57 80
17 32 63 44
56 60 78 98

Output:
***13
**55 21
*17 65 36
56 32 57 49
*60 63 80
**78 44
***98
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
