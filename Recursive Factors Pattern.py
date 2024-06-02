The program must accept an integer N as the input. The program must find the factors of N. Then the program must find the factors of each factor of N except 1 and N. The program must repeat the process of finding 
factors till there is no factor to find. Finally, the program must print all the obtained factors with hyphens as the output.
Note: The number of hyphens in the output indicates the depth of finding the factors.

Example Input/Output 1:
Input:
6
Output:
-6
--1
--2
---1
---2
--3
---1
---3
--6

Example Input/Output 3:
Input:
8
Output:
-8
--1
--2
---1
---2
--4
---1
---2
----1
----2
---4
--8

Example Input/Output 3:
Input:
7
Output:
-7
--1
--7

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
