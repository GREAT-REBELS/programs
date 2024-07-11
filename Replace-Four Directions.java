The program must accept an integer matrix of size RxC and an integer X as the input. The program must replace the integers with asterisks (*) in the north-east, south-east, south-west and north-west directions
of X(including X) in the matrix. Then the program must print the modified matrix as the output.
Note: The integer X has occurred only once in the RxC integer matrix.
  
Example Input/Output 1:
Input:
5 4
14 13 46 24
33 35 30 18
12 22 23 27
31 21 26 44
47 10 36 49
22
Output:
14 13 46 * 
* 35 * 18
12 * 23 27
* 21 * 44
47 10 36 *
Explanation:
The integers in the north-east, south-east, south-west and north-west directions of 22 are highlighted in the 5x4 matrix.
14 13 46 '24'
'33' 35 '30' 18
12 '22' 23 27
'31' 21 '26' 44
47 10 36 '49'
So those integers are replaced with asterisks (*) in the matrix.
Hence the output is
14 13 46 * 
* 35 * 18
12 * 23 27
* 21 * 44
47 10 36 49

Example Input/Output 2:
Input:
4 4
31 73 29 87
77 44 66 46
90 9 10 43
3 1 39 34
10
Output:
* 73 29 87
77 * 66 *
90 9 * 43
3 * 39 *
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
