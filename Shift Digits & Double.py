The program must accept an integer N as the input. The program must form an integer X by shifting the digits at even positions in N once to the right. Then the program must print 2*X as the output.
Example Input/Output 1:
Input:
123456
Output: 
326508
Explanation:
In the given integer 123456, the digits in even positions are 2, 4, 6.
After shifting the digits in even positions for 1 time to the right, the integer becomes 163254.
After doubling the integer value, the integer becomes 326508 (2x163254)
Hence the output is 326508
Example Input/Output 2:
789335467
Output: 
1539666914
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def splitDigits(num):
    lst = []
    while num:
        lst.append(num % 10)
        num = num // 10
    return lst

def joinDigits(lst):
    num = 0
    for i in range(len(lst) - 1, -1, -1):
        num = num * 10 + lst[i]
    return num

num = int(input())
lst = splitDigits(num)
for i in range(len(lst) - 2, -1, -2):
    lst[i], lst[i - 1] = lst[i - 1], lst[i]

if len(lst) % 2:
    lst.insert(len(lst) - 1, lst[0])
else:
    lst.insert(len(lst), lst[0])
print(joinDigits(lst[1:]) * 2)
