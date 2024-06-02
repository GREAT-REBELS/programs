The program must accept an integer N as the input. The program must find the factors of N. Then the program must find the factors of each factor of N except 1 and N. The program must repeat the process of finding 
factors till there is no factor to find. Finally, the program must print all the obtained factors with hyphens as the output.
Note: The number of hyphens in the output indicates the depth of finding the factors.

  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def getFactors(N, depth):
    for i in range(1, N + 1):
        if i == 1 or i == N:
            print("-" * depth, end="")
            print(i)
        elif N % i == 0:
            print("-" * depth, end="")
            print(i)
            getFactors(i, depth + 1)


N = int(input())
print("-", end="")
print(N)
getFactors(N, 2)
