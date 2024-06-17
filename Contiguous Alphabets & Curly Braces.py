The program must accept a string S containing only alphabets as the input. The program must enclose the contiguous alphabets (in alphabetical order by ignoring the case) with a pair of curly braces {}. Then the 
program must print the modified string S as the output. If there are no such contiguous alphabets in the string S, the program must print the string S as it is.

Example Input/Output 1:
Input:
DefeaT

Output:
{Def}eaT
Explanation:
The contiguous alphabets in the string Defeat are D, e and f. So they are enclosed within a pair of curly braces.
Hence the output is {Def}eaT.

Example Input/Output 2:
Input:
stUdeNt

Output:
{stU){de}Nt

Example Input/Output 3:
Input:
onnne

Output
onnne
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = input()
N = len(word)
i = 0
while i < N:
    strt = i
    while i + 1 < N and ord(word[i + 1].lower()) - ord(word[i].lower()) == 1:
        i += 1
    if i > strt:
        print("{" + word[strt : i + 1] + "}", end="")
    else:
        print(word[i], end="")
    i += 1

Time Complexity - O(N) 
Space Complexity - O(N) 
