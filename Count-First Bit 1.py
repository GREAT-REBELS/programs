The program must accept an integer N as the input. The program must print the count of integers from 1 to N which are having 1 as the first bit in their binary representation. The number of bits to consider to
find the first bit is the number of bits in the binary representation of N. So you must pad the leading zeros depending on the number of bits in the binary representation N.

Example Input/Output 1:
Input: 
10
Output:
3
Explanation:
Here = 10. The number of bits in the binary representation of 10 is 4. So the number of bits to consider to
find the first bit is 4.
The binary representation of the integers from 1 to 10 are given below.
0001
0010 
0011
0100
0101
0110
0111
1000
1001
1010 
There are three binary representations having 1 as the first bit (1000, 1001 and 1010).
So 3 is printed as the output

Example Input/Output 2:
Input:
16
Output: 
1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N = int(input())
bit_len = len(bin(N)[2:])
cnt = N - ((1 << bit_len - 1) - 1)
print(cnt)
