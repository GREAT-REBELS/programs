Mr.X and his friend Mr.Y are playing a game guessing letters. Mr.X writes down the name N secretly without revealing it to Mr.Y and conveys the number of letters in the name N to his friend Y. Mr.Y tries to 
accurately guess the letters in N and comes up with a name G. The program must accept N and G as the input. The program  must print how many letters were guessed right (exactly in the same position) and how many 
letters were guessed in the incorrect position(s).
Note: The length of N and G are always equal. 

Example Input/Output 1:
Input:
aaaw wwaa
Output:
1
2
Explanation:
In the two names aaaw and wwaa, the letter 'a' was guessed right (exactly in the same position). So the count 1 is printed in the first line. In the two names 
aaaw and wwaa, the letters 'a' and 'w' were guessed in the incorrect position(s). So the count 2 is printed in the second line.

Example Input/Output 2:
Input:
abcd ABcd
Output
2
0

Example Input/Output 3:
Input
FDGRH ASDFR
Output
0
3
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N, G = input().split()
right_cnt, wrong_cnt = 0, 0
for i in range(len(N)):
    if N[i] == G[i]:
        right_cnt += 1
for ch in set(N):
    wrong_cnt += min(N.count(ch), G.count(ch))
wrong_cnt -= right_cnt
print(right_cnt)
print(wrong_cnt)

