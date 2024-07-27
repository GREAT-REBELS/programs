The program must accept two string values S1 and S2 as the input. The string S1 represents a pattern and the string S2 represents a space-separated string value. Each character in S1 represents a word in S2 in the
order of their occurrence. The program must print YES if the string S2 follows the pattern S1. Else the program must print NO as the output.

Example Input/Output 1:
Input:
abcacb
book pen pencil book pencil pen
Output: 
YES
Explanation:
The characters a, b and c ara matched with the words book, pen and pencil respectively. Here the string "book pen pencil book pencil pen" follows the pattern "abcacb", so YES is printed as the output.

Example Input/Output 2:
Input
Хуxу
bat ball bat ball
Output:
NO

Example Input/Output 3:
Input: 
PQRS 
doll car toy
Output: 
NO
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
S1 = input().strip()
S2 = input().split()
mappings = {}
if len(S1) != len(S2):
    print("NO")
    quit()
for ch, word in zip(S1, S2):
    if ch not in mappings and word not in mappings.values():
        mappings[ch] = word
    if (ch in mappings and mappings[ch] != word) or (word in mappings.values() and ch not in mappings):
        print("NO")
        quit()
print("YES")
