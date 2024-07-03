The program must accept a string S containing only alphabets as the input. The program must print all the vowels in the string S in the order of their occurrence interlaced with all the consonants in the string S in
the reverse order of their occurrence as the output.

Example Input/Output 1:
Input:
SkillRack
Output:
ikacRilkS
Explanation:
The vowels in the string SkillRack are i and a.
The consonants in the string SkillRack are S, k, I, I, R, c and k.
After interlacing the vowels (in the order of their occurrence) with the consonants (in the reverse order of their occurrence), the string becomes ikacRilkS.
So ikacRIIkS is printed as the output.

Example Input/Output 2:
Input: 
Heaven
Output: 
enaveH

Example Input/Output 3:
Input:
AEIOU
Output:
AEIOU
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = input()
vowels = []
consonants = []

for char in word:
    if char.lower() in 'aeiou':
        vowels.append(char)
    else:
        consonants.append(char)

consonants.reverse()
res = []
i, j = 0, 0
while i < len(vowels) and j < len(consonants):
    res.append(vowels[i])
    res.append(consonants[j])
    i += 1
    j += 1
  
# Adding remaining vowels if any
while i < len(vowels):
    res.append(vowels[i])
    i += 1

# Adding remaining consonants if any
while j < len(consonants):
    res.append(consonants[j])
    j += 1

print(''.join(res))
