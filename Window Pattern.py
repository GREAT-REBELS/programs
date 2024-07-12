The program must accept two integers N and X as the input. The program must print an S*S matrix of matrices (where S is the square root of X) based on the following conditions.
- The size of each matrix in the S*S matrix is N*N.
- Each matrix contains only asterisks.
- The matrices are separated by the pipe symbols (1) vertically(including edges).
- The matrices are separated by the hyphens (-) horizontally(including edges).
- Each intersection of the matrices(including corners) is represented by the plus symbol (+). 
Note: The value of X is always a perfect square.

Example Input/Output 1:
Input:
5 1
Output:
+-----+
|*****|
|*****|
|*****|
|*****|
|*****|
+-----+
Explanation:
Here N = 5 and X = 1.
The square root of 1 is 1.
So the size of the matrix is 1x1 and it contains a matrix of size 5*5 with asterisks.
Hence the output is
  
Example Input/Output 2:
Input:
2 4 
Output:
+--+--+
|**|**|
|**|**|
+--+--+
|**|**|
|**|**|
+--+--+

Example Input/Output 3:
Input:
1 16
Output:
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+
|*|*|*|*|
+-+-+-+-+
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math
N,X = map(int,input().split())
S = int(math.sqrt(X))

intersectionPattern = "+"
for i in range(S):
    intersectionPattern+="-"*N+"+"

row = "|"
for i in range(S):
    row+="*"*N+"|"

print(intersectionPattern)
for i in range(S):
    for j in range(N):
        print(row)
    print(intersectionPattern)
    

