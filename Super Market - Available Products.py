In a supermarket, there are X products that are listed on a board. Each product has a unique number. A boy wants to purchase Y products from the supermarket. The program must accept X integers representing the 
unique number of X products and Y integers representing the unique number of Y products as the input. The program must print the unique number of all the products that are available to the boy in the order of 
their occurrence(i.e., the order mentioned in the board) as the output.
Note: At least one product is always available in the supermarket from the list of Y products.

Example Input/Output 1:
Input:
7 3
3 4 6 2 7 1 9
2 1 6
Output: 
6 2 1
Explanation:
The products available in the supermarket are given below.
3 4 6 2 7 1 9
The boy wants to purchase 3 products that are given below.
2 1 6
Here all three products are available for the boy from the supermarket. So they are printed in the order of their occurrence.
Hence the output is
6 2 1

Example Input/Output 2:
Input:
5 5
5 4 3 7 10
7 3 6 9 10
Output:
3 7 10
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
X, Y = map(int, input().split())
supermarket_products = list(map(int, input().split()))
boy_purchaseList = list(map(int, input().split()))
for productId in supermarket_products:
    if productId in boy_purchaseList:
        print(productId, end=" ")
