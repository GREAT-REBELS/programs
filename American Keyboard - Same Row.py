The program must accept a string S containing multiple words separated by a comma as the input. The program must print the words in the string S that are formed using alphabets from the same row of the American 
keyboard. If there is no such word in the string S, the program must print -1 as the output.
The alphabets in the three rows of the American keyboard are given below:
QWERTYUIOP
ASDFGHJKL
ZXCVBNM

Example Input/Output 1:
Input:
HELLO, DAD, PEACE
Output:
DAD
Explanation:
In the word HELLO, all the alphabets are not present in the same row of the American keyboard.
In the word DAD, all the alphabets are present in the same row(2nd row) of the American keyboard.
In the word PEACE, all the alphabets are not present in the same row of the American keyboard.
So the word DAD is printed as the output.

Example Input/Output 2:
Input:
root, had, bad,cat, water
Output: 
root had

Example Input/Output 3:
Input:
happy,world
Output: 
-1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def is_same_row(word):
    for row in rows:
        if all(char in row for char in word.upper()):
            return True
    return False
rows = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
words = input().split(',')
for word in words:
    if is_same_row(word):
        print(word)
        flg = 1 
if not flg:
    print(-1)
