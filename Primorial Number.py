The program must accept an integer N as the input. The program must print the primorial of N as the output. The primorial of N is defined as the product of the first N prime integers.

Example Input/Output 1:
Input:  
3
Output: 
30
Explanation:
The first 3 prime integers are 2, 3 and 5. So their product 30 (2*3*5) is printed as the output.

Example Input/Output 2:
Input: 
5
Output: 
2310
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
           return 0
    return 1

Num = int(input())
res = 2
K = 3
Num -= 1
while Num:
    if isPrime(K):
        res *= K
        Num -= 1
    K += 2
print(res)
