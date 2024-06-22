The program must accept N integers as the input. The program must print the LCM of all the even integers among the N integers as the output.
Note: At least two even integers are always present among the N integers.

Example Input/Output 1: 
Input:
5
2 5 3 6 4
Output:
12
Explanation:
The even integers among the 5 integers are 2, 6 and 4.
The LCM of 2, 6 and 4 is 12.
So 12 is printed as the output.

Example Input/Output 2:
Input:
5  
10 21 14 89 2 
Output:
70
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return (a * b) // GCD(a, b)

N = int(input())
lst = list(map(int, input().split()))

even_numbers = [num for num in lst if num % 2 == 0]

res = even_numbers[0]
for num in range(1, len(even_numbers)):
    res = LCM(res, even_numbers[num])
print(res)
