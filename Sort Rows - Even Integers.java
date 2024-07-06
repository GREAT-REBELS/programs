The program must accept an integer matrix of size RxC as the input. The program must sort the rows of the matrix based on the number of even integers in each row. If more than one rows have the same number of even
integers, the program must sort those rows in the order of their occurrence. Finally, the program must print the modified matrix as the output.

Example Input/Output 1:
Input:
3 4
1 2 4 5
4 9 8 6
9 7 8 5
Output:
9 7 8 5
1 2 4 5
4 9 8 6
Explanation:
The number of even integers in the 1st row of the matrix is 2 (1245).
The number of even integers in the 2nd row of the matrix is 3 (4986). The number of even integers in the 3rd row of the matrix is 1 (9785).
After sorting the rows of the matrix based on the number of even integers, the matrix becomes
9 7 8 5
1 2 4 5
4 9 8 6

Example Input/Output 2:
Input:
5 5
84 48 94 18 79
35 97 13 75 91
99 48 53 37 99
36 13 38 10 15
93 55 25 94 41
Output:
35 97 13 75 91
99 48 53 37 99
93 55 25 94 41
36 13 38 10 15
84 48 94 18 79
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def count_even_numbers(row):
    return sum(1 for num in row if num % 2 == 0)

R, C = map(int, input().split())
matrix = []
for _ in range(R):
    row = list(map(int, input().split()))
    matrix.append(row)
row_counts = [(count_even_numbers(matrix[i]), i) for i in range(R)]
row_counts.sort(key=lambda x: (x[0], x[1]))
for row in row_counts:
    print(*matrix[row[1]])

