The program must accept a string S as the input. The program must replace all the vowels in the string S with 1. Then the program must print the modified string and the count of vowels C in the string S as the
output. If the string S contains characters other than alphabets, the program must print Invalid as the output.

Example Input/Output 1:
Input: 
AeFloT
Output: 
11F1T 3
Explanation:
The count of vowels in the string AeFloT is 3 and they are A, e and o. After replacing the vowels with 1, the string becomes 11FI1T.
Hence the output is
11FI1T 3

Example Input/Output 2:
Input: 
AB1E
Output: 
Invalid
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = input()
if not word.isalpha():
    print("Invalid")
    quit()
cnt = 0
for ch in word:
    if ch.lower() in ["a", "e", "i", "o", "u"]:
        print(1, end="")
        cnt+=1
    else:
        print(ch, end="")
print(end=" ")
print(cnt)
