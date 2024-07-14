The program must accept an integer matrix of size RxC representing the blueprint of a city as the input. The matrix always contains 1s and Os, where each 1 represents a shop and each 0 represents an empty place.
A group of shops in the city is called a market, where the shops are connected vertically and horizontally. The program must print the number of markets in the city as the output. 
Note: At least one shop is always present in the city.

Example Input/Output 1:
Input:
5 5
0 0 0 1 0
0 0 0 1 1
0 0 0 0 0
0 0 0 1 0
0 0 0 1 1

Output:
2
Explanation:
The markets in the city are highlighted below.
0 0 0 '1' 0
0 0 0 '1' '1'
0 0 0 0 0
0 0 0 '1' 0
0 0 0 '1' '1'
Here the number of markets in the city is 2, which is printed as the output

Example Input/Output 2:
Input:
6 4
0 0 0 1
0 0 0 0
0 0 1 1
1 0 1 0
1 0 0 1
1 1 1 1

Output:
3
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
