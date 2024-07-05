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
from collections import Counter
word1,word2 = input().split()
counter = Counter(word1)
k = 0
rght_cnt,wrng_cnt = 0,0
for ch in word2:
    if ch == word1[k]:
        rght_cnt+=1 
    elif ch in word1 and counter[ch]>0 :
        wrng_cnt+=1
        counter[ch]-=1
    k+=1
print(rght_cnt)
print(wrng_cnt)
