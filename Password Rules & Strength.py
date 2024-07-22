The program must accept a string P representing a password as the input. The password rules are given below.
Rule 1: The password must have at least 8 characters.
Rule 2: The password must have at least one upper case and one lower case alphabet.
Rule 3: The password must have at least one digit.
Rule 4: The password must have at least one special character.
The program must print the output based on the following conditions. 
- If only Rule 1 is satisfied or none of the rules satisfied, print WEAK as the output.
- If two rules (Rule 1 and any one rule from 2 to 4) are satisfied, print MEDIUM as the output.
- If three rules (Rule 1 and any two rules from 2 to 4) are satisfied, print GOOD as the output 
- If all four rules are satisfied, print STRONG as the output.

Example Input/Output 1:
Input: 
Qwerty@123
Output: 
STRONG
Explanation:
Here the password Qwerty@123 satisfied all the four rules. So STRONG is printed as the output.

Example Input/Output 2:
Input: 
Q$1a
Output: 
WEAK
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import re

password = input()
rule1 = len(password) >= 8
rule2 = bool(re.search(r"[A-Z]", password)) and bool(re.search(r"[a-z]", password))
rule3 = bool(re.search(r"\d", password))
rule4 = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
cnt = [rule2, rule3, rule4].count(True)
if all([rule1, rule2, rule3, rule4]):
    print("STRONG")
elif rule1 and cnt == 2:
    print("GOOD")
elif rule1 and cnt == 1:
    print("MEDIUM")
else:
    print("WEAK")
