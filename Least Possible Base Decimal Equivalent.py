The program must accept a string S representing a value in any base from 2 to 36 as the input. The program must find the least possible base of S and print its decimal equivalent as the output.
The face values for the symbols are given below.
0->0
1->1
2->2
...
9->9
A-> 10
B-11
C-> 12
...
X->33
Y-> 34
Z->35 

Example Input/Output 1:
Input: 
11
Output: 
3
Explanation:
The least possible base for 11 is 2. The decimal equivalent of (11)2 is 3. So 3 is printed as the output.

Example Input/Output 2:
Input: 
21A
Output: 
263
Explanation:
The least possible base for 21A is 11. The decimal equivalent of (21A) 11 is 263. So 263 is printed as the output.

Example Input/Output 3:
Input: 
XY
Output:
1189
Explanation:
The least possible base for XY is 35. The decimal equivalent of (XY)35 is 1189. So 1189 is printed as the output.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
S = input()
maxDig = 0
for dig in S:
    if int(dig, 36) > maxDig:
        maxDig = int(dig, 36)
base = maxDig + 1
dec = 0
for i, digit in enumerate(S[::-1]):
    dec += int(digit, 36) * (base**i)
print(dec)
