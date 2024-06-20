The program must accept an integer N as the input. The program must print all possible binary representations using 1 bit. Then the program must print all possible binary representations using 2 bits. Similarly, 
the program must print all possible binary representations till N bits as the output.

Example Input/Output 1:
Input:
3
Output:
0
1
00
01
10
11
000
001
010
011
100
101
110
111
Explanation:
Here N = 3.
All possible binary representations using 1 bit are 0 and 1.
All possible binary representations using 2 bits are 00, 01, 10 and 11.
All possible binary representations using 3 bits are 000, 001, 010, 011, 100, 101, 110 and 111.

Example Input/Output 2:
Input:
2
Output:
0
1
00
01
10
11
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def generateBinaryNums(length, binaryStr=""):
    if length == 0:
        print(binaryStr)
        return
    generateBinaryNums(length - 1, binaryStr + "0")
    generateBinaryNums(length - 1, binaryStr + "1")

N = int(input())
for i in range(1, N + 1):
    generateBinaryNums(i)

