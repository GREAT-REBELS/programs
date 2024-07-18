The program must accept an integer N as the input. The program must print the next greater integer of N having no consecutive 1s in its binary representation. If there are no consecutive 1s in the binary 
representation of N, the program must print the integer N as the output.

Example Input/Output 1:
Input: 
6
Output: 
8
Explanation:
Here N = 6.
The binary representation of 6 is 110 (2 consecutive 1s).
The binary representation of 7 is 111 (3 consecutive 1s).
The binary representation of 8 is 1000 (NO consecutive 1s).
So 8 is printed as the output.

Example Input/Output 2:
Input: 
9
Output: 
9
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ConsecutiveOnes(num):
    return "11" in bin(num)

N = int(input())
while N:
    if not ConsecutiveOnes(N):
        print(N)
        quit()
    N += 1
