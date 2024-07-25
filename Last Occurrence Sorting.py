The program must accept two string values S1 and S2 as the input. The program must print the characters in S2 in ascending order based on the positions of their last occurrence in S1. 
Note: All the characters in S2 are always present in S1.

Example Input/Output 1:
Input:
earthquakes
shake
Output:
hakes
Explanation:
Here S1 is earthquakes and S2 is shake.
The position of the last occurrence of s in earthquakes is 11.
The position of the last occurrence of h in earthquakes is 5.
The position of the last occurrence of a in earthquakes is 8.
The position of the last occurrence of k in earthquakes is 9.
The position of the last occurrence of e in earthquakes is 10.
So the characters in shake are printed in ascending order based on the positions of their last occurrence in S1.
Hence the output is hakes

Example Input/Output 2:
Input:
Software Hardwares
SHortS
Output:
SSotHr
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
S1 = input()
S2 = input()
occ = []
for ch in S2:
    occ.append(
        (ch, S1.rindex(ch))) #rindex() method finds the last occurrence of the specified value
occ.sort(key=lambda X: X[1])
for item in occ:
    print(item[0], end="")
