The program must accept a string S as the input. The program must print the string S for (L+1)/2 times (where L is the length of the string S) based on the following conditions. In the first line, the program 
must print the string S except the first and last characters. In the second line, the program must print the string S except the second and last but one characters.Similarly, the program must print the remaining 
possible string values as the output.

Boundary Condition(s): 3 <= Length of S <= 100

Input Format: The first line contains S.

Output Format: The first (L+1)/2 lines, each contains the string S based on the given conditions.

Example Input/Output 1:

Input:
environment

Output:
nvironmen
evironmet
enironmnt
envronent
enviorment
envirnment

Explanation:
The length of the string environment is 11. So the pattern contains 6 ((11+1)/2 = 6) lines of output. In the first line, the string S is printed except the first and last characters(e and t).
nvironmen
In the second line, the string S is printed except the second and last but one characters(n and n).
evironmet
Similarly, the remaining possible string values are printed.
enironmnt
envronent
envioment
envirnment

Example Input/Output 2:

Input:
Robotics

Output:
obotic
Rbotis
Rootcs
Robics
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = input()
length = len(word)
for i in range((length+1)//2):
    print(word[:i] + word[i+1:length-i-1] + word[length-i:])
