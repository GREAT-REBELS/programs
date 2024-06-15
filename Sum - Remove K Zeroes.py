The program must accept N integers and an integer K as the input. The program must remove the first K zeroes in the cumulative binary representation of N integers. Then the program must print the sum of the N 
modified integer values as the output. Note: At least K zeroes are always present in the cumulative binary representation of N integers.

Example Input/Output 1:
Input:
4 7
21 75 127 86

Output:
179
Explanation:
The binary representation of the 4 integers are 10101, 1001011, 1111111 and 1010110. 
After removing the first 7 zeroes in the cumulative binary representation of 4 integers, the integers become 7, 15, 127 and 30.
So their sum 179 (7+15+127+30 = 179) is printed as the output.

Example Input/Output 2:
Input:
5 5
5 6 8 10 12

Output:
29
Explanation:
The binary representation of the 5 integers are 101, 110, 1000, 1010 and 1100.
After removing the first 5 zeroes in the cumulative binary representation of 5 integers, the integers become 3, 3, 1, 10 and 12.
So their sum 29 (3+3+1+10+12= 29) is printed as the output.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N, K = map(int, input().split())
lst = list(map(int, input().split()))
sum_ = 0
for i in lst:
    if K:
        binaryStr = bin(i).replace("0b", "")
        binVal = binaryStr
        for j in range(len(binaryStr)):
            if K and binaryStr[j] == "0":
                binVal = binVal.replace("0", "", 1)
                K -= 1
        sum_ += int(binVal, 2)
    else:
        sum_ += i
print(sum_)
