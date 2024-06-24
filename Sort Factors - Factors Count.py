The program must accept an integer N as the input. The program must find the factors of N. Then the program must sort those factors in descending order based on their factors count. If more than one factors have 
the same factors count, the program must sort those factors in descending order. Finally, the program must print the sorted factors as the output.

Example Input/Output 1:
Input: 
50
Output: 
50 10 1 25 5 2 1
Explanation:
The factors of 50 are 1, 2, 5, 10, 25 and 50.
The integer 1 has 1 factor.
The integer 2 has 2 factors.
The integer 5 has 2 factors. The integer 10 has 4 factors.
The integer 25 has 3 factors.
The integer 50 has 6 factors. Here 2 and 5 have the same number of factors. So they are sorted in descending order.
After sorting the factors of 50 in descending order based on their factors count, the factors become 50 10 25 5 2 1.
So they are printed as the output.

Example Input/Output 2:
Input: 
455
Output:
455 91 65 35 13 751
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def getFactorsCnt(num):
    cnt = 0
    for i in range(1,num+1):
        if num%i==0:
            cnt+=1
    return cnt
N = int(input())
lst = []
for i in range(N,0,-1):
    if N%i==0:
        lst.append((i,getFactorsCnt(i)))
lst.sort(key=lambda X:X[1],reverse = True)
for i in lst:
    print(i[0],end=" ")
