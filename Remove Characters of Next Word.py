The program must accept a string S containing multiple words as the input. For each word W in the string S, the program must remove the characters in W which are present in it's next word. Then the program must 
print the modified string S as the output. If a word is formed using the characters of it's next word, the entire word is removed in the string S. The last word in S remains the same because there is no word next 
to it.

Example Input/Output 1:
Input:
racing ring

Output: 
ac ring
Explanation:
The characters in the first word which are present in the second word are r, i, n, and g. After removing those characters, the first word becomes ac. Hence the output is ac ring

Example Input/Output 2:
Input:
always put your best foot forward

Output
alway$ pt your be$ Ot forward

Example Input/Output 3:
Input:
mobilePhone Phone RING EAR EARRINGS

Output:
mbil Phone ING EARRINGS
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
words = input().split()
for i in range(0, len(words) - 1):
    rep = set(words[i + 1])
    for j in words[i]:
        if j in rep:
            words[i] = words[i].replace(j,'')
    if words[i]:
        print(words[i], end=" ")
print(words[-1])
