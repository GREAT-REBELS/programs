The program must accept a string S containing only alphabets as the input. The program must print YES if it is possible to modify the string S as a palindrome based on the following conditions.
- Any alphabet CH in the string S can be replaced with its previous/next alphabet in the English alphabet set.
- If CH is 'A', it must be replaced with 'B' as there is no previous alphabet.
- If CH is 'Z', it must be replaced with 'Y' as there is no next alphabet.
- If CH is 'a', it must be replaced with 'b' as there is no previous alphabet.
- If CH is 'z', it must be replaced with 'y' as there is no next alphabet.
If it is not possible to form a palindrome by modifying the string S, the program must print NO as the output.
Note: The palindromic string is always case sensitive.

Example Input/Output 1:
Input:
afdc
Output:
YES
Explanation:
Here the string is afdc.
The first alphabet 'a' is replaced with 'b'.
The second alphabet 'f can be replaced with either 'e' or 'g'. To get the palindromic string, it must be replaced with 'e'.
The third alphabet 'd' can be replaced with either 'c' or 'e'. To get the palindromic string, it must be replaced with 'e'.
The fourth alphabet 'c' can be replaced with 'b' or 'd'. To get the palindromic string, it must be replaced with 'b'.
Now the string becomes beeb which is a palindrome.
So YES is printed as the output.

Example Input/Output 2:
Input:
bdhajzicb
Output: 
NO

Example Input/Output 3:
Input:
azAZGuwEYByb
Output:
YES
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = input()
left, right = 0, len(word) - 1
while left <= right:
    if abs(ord(word[left]) - ord(word[right])) > 2:
        print("NO")
        quit()
    left += 1
    right -= 1
print("YES")
