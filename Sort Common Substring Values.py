The program must accept two string values S1, S2 (containing only alphabets) and an integer X as the input. The program must print all the common substring values of length X in the string values S1 and S2 
sorted in ascending order as the output. If there is no common substring of length X then the program must print -1 as the output.

Example Input/Output 1:
Input:
telephone
phone
3

Output:
hon one pho
Explanation:
Here X = 3.
The common substring values of length 3 in the string values telephone and phone are pho,
hon and one. After sorting the common substring values in ascending order, the substring values become hon, one and pho.

Example Input/Output 2:
Input:
ENVIRONMENT
education
2

Output: 
-1

Example Input/Output 3:
Input:
SkillRack
SkillSkillRack
2

Output:
Ra Sk ac ck il ki IR II
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def splitWord(word,N):
    subStrLst = []
    for i in range(len(word)-N+1):
        subStrLst.append(word[i:i+N])
    return subStrLst

word1 = input()
word2 = input()
N = int(input())
subStrLst1,subStrLst2 = splitWord(word1,N),splitWord(word2,N)
commonSubstrs = []
for subStr in subStrLst1:
    if subStr in subStrLst2:
        commonSubstrs.append(subStr)
if not commonSubstrs:
    print(-1)
    quit()

print(*sorted(commonSubstrs))
