The program must accept two string values S1 and S2 are of equal length (containing only alphabets) as the input. The rules of the string traversal game are given below.
The game always starts from the last character of S1.
- If both the characters in S1 and S2 are consonants or vowels in the same position, then traverse in up/down direction between S1 and S2. Else traverse in the left direction in the same string.
- The game ends when there is no character to traverse in S1 and S2.
The program must print the characters that are used in the string traversal game as the output.

Example Input/Output 1:
Input:
cat
dog

Output: 
tgoacd
Explanation:
Here S1 = "cat" and S2 = "dog".
The game always starts from the last character of S1.
So the first character traversed in the game is t.
Then compare the characters at the same position(3). Here both are consonants(t, g). So the second character traversed in the game is g.
Then the only possible way to traverse is moving towards left. So the third character traversed in the game is o.
Then compare the characters at the same position(2). Here both are vowels(o, a). So the fourth character traversed in the game is a.
Then the only possible way to traverse is moving towards left. So the fifth character traversed in the game is c.
Then compare the characters at the same position(1). Here both are consonants(c, d). So the sixth character traversed in the game is d.
So tgoacd is printed as the output.

Example Input/Output 2:
Input:
SKILLRACK
BACDFEGHJ
  
Output:
KJHCARLFDLIKSB
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  def isVowel(ch):
    return ch.lower() in "aeiou"

s1 = input().strip()
s2 = input().strip()
turn = 1
res = ""
for i in range(len(s1) - 1, -1, -1):
    if (isVowel(s1[i]) and isVowel(s2[i])) or (not isVowel(s1[i]) and not isVowel(s2[i])):
        if turn:
            res += s1[i] + s2[i]
        else:
            res += s2[i] + s1[i]
        turn = not turn
    else:
        if turn:
            res += s1[i]
        else:
            res += s2[i]
print(res)
