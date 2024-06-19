The program must accept an integer N as the input. The program must print the maximum possible integer which is formed by toggling exactly one bit in the binary representation of N as the output. If all the bits in 
the binary representation of N are 1,the program must print the value of N.

Example Input/Output 1:
Input:
22
Output:
30
Explanation:
The binary representation of 22 is 10110.
If the first bit is toggled, the binary representation becomes 00110 and its decimal equivalent is 6. 
If the second bit is toggled, the binary representation becomes 11110 and its decimal equivalent is 30. 
If the third bit is toggled, the binary representation becomes 10010 and its decimal equivalent is 18.
If the fourth bit is toggled, the binary representation becomes 10100 and its decimal equivalent is 20.
If the fifth bit is toggled, the binary representation becomes 10111 and its decimal equivalent is 23.
Here the maximum integer value is 30. So it is printed as the output.

Example Input/Output 2:
Input:
15
Output:
15
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
num = int(input())
binaryStr = bin(num).replace("0b", "")
if binaryStr.count("1") == len(binaryStr):
    print(num)
    quit()
for i in binaryStr:
    if i == "0":
        binaryStr = binaryStr.replace("0", "1", 1)
        break
print(int(binaryStr, 2))
