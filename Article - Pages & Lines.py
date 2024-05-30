Mr. ABC wants to write an article on a notebook. The total number of characters in his article is X. Each page in the notebook can hold Y lines. Each line can hold Z characters. The values of X, Y and Z are passed
as the input to the program. The program must print the minimum number of pages required to write the article followed by the minimum number of lines required to write the article as the output.
Note: The notebook always has enough pages to write the article.

Example Input/Output 1:
Input:
1569
10
50
  
Output:
4
32
Explanation:
The total number of characters in the article is 1569. Each page can hold 10 lines. Each line can hold 50 characters.
The minimum number of pages required to write the article is 4.
The first page contains 500 characters.
The second page contains 500 characters.
The third page contains 500 characters.
The fourth page contains 69 characters.
The minimum number of lines required to write the article is 32.
The first page contains 10 lines.
The second page contains 10 lines.
The third page contains 10 lines.
The fourth page contains 2 lines (where the last line contains 19 characters).

Example Input/Output 2:
Input:
2000
20
100

Output:
1
20

Example Input/Output 3:
Input:
251
5
10

Output:
6
26
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math

articleCharacters = int(input())
Lines = int(input())
LineCharacters = int(input())
print(math.ceil(articleCharacters / (LineCharacters * Lines)))
print(math.ceil(articleCharacters / LineCharacters))
