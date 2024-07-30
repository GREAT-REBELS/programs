The program must accept an integer N as the input. The program must print the next greater integer of N with prime digits (2, 3, 5 and 7) as the output.
Example Input/Output 1:
Input: 
342
Output:
352
Explanation:
Here N=342, the next greater integer with prime digits is 352.
So 352 is printed as the output.

Example Input/Output 2:
Input: 
786
Output:
2222
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
while True:
    N += 1
    if all(digit in '2357' for digit in str(N)):
        print(N) 
        quit()  
