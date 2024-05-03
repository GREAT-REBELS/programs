The program must accept N integers as the input. The program must generate an integer matrix of size NxN with the N integers in each row. Then the program must replace each digit with an asterisk in the non-diagonal 
integers of the matrix. Finally, the program must print the matrix without any space in each row.

Boundary Condition(s): 2 <= N <=50 1 <= Each integer value <= 10^8

Input Format: The first line contains N. The second line contains N integers separated by a space.

Output Format: The first N lines containing the modified matrix.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
n=int(input())
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        if i==j:
            print(lst[i],end="")
        elif i+j==n-1:
            print(lst[n-i-1],end="")
        else:
            s=str(lst[j])
            print(len(s)*'*',end="")
    print()
            
