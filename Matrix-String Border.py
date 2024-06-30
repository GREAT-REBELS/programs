The program must accept four string values S1, S2, S3 and S4 and a character matrix as the input. The program must print Yes if the four string values are present at the four boundaries of the matrix in any order. 
Else the program must print No as the output.
Note:
The length of S1, S2, S3 and S4 are always equal L. 
The size of the character matrix is always L*L.
Example Input/Output 1:
Input:
teen meal neam lift
t e e n
f c e e
i u g a
l a e m

Output:
Yes
Explanation:
The four string values are teen, meal, neam and lift.
The four boundaries of the matrix are highlighted below.
't' 'e' 'e' 'n'
'f' c e 'e'
'i' u g 'a'
'l' 'a' 'e' 'm'
The first row representing the string teen.
The last column representing the string neam.
The last row representing the string meal.
The first column representing the string lift.
So Yes is printed as the output.

Example Input/Output 2:
Input:
HELLO HOBBY PENNY PHOTO
O T O H P
L E R T E
L X F B N
E T U I N
H O B B Y

Output:
Yes

Example Input/Output 3:
Input:
gifty horse gorch EASSY
g i f t y
o v e r s
r r t y S
c e t t A
h o r s E

Output:
No
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def chk(word, words):
    if word in words or word[::-1] in words:
        return 1
    return 0

words = input().split()
L = len(words[0])
matrix = []
for i in range(L):
    word = input().strip()
    matrix.append(list(word.replace(" ", "")))
top_word = "".join(matrix[0])
bottom_word = "".join(matrix[L - 1])
left_word = "".join(matrix[i][0] for i in range(L))
right_word = "".join(matrix[i][L - 1] for i in range(L))

if(chk(top_word, words) and chk(left_word, words) and chk(right_word, words) and chk(bottom_word, words)):
    print("Yes")
else:
    print("No")
