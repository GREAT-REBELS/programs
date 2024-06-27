The program must accept a string S as the input. The program must check whether each open parenthesis 'C' has a matching close parenthesis ')'. If all the parentheses are matching, then the program must print 
else the program must print 1.

Example Input/Output 1: 
Input: 
Doll (Lion (cat rat) Tiger (snake) Fox) Shop (Dog())
Output: 
0
Explanation:
Here all 5 pairs of parentheses are matching.
So 0 is printed as the output.

Example Input/Output 2:
Input: 
(9*(7-2)+(1*5)
Output: 
 1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = input()
stack = []
for ch in word:
    if ch == "(":
        stack.append(ch)
    elif ch == ")" and len(stack) > 0:
        stack.pop()
print(1 if len(stack) else 0)
