The program must accept N integers as the input. If N is even,the program must print the sum of middle four integers among N integers as the output.Else the program must 
print the sum of middle three integers among N integers as the output.
Example1:
Input:
5
2 3 5 7 8
Output:
15
Example2:
Input:
6
23 47 63 52 77 56
Output:
239
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include<stdio.h>
#include<stdlib.h>
{
int N,sum=0;
scanf("%d",&N);
int arr[N];
for(int i=0;i<N;i++)
{
scanf("%d",&arr[i]);
}
int len=N/2;
if(N%2==0)
{
    printf("%d",arr[len-1]+arr[len-2]+arr[len]+arr[len+1]);
}
else
{
    printf("%d",arr[len-1]+arr[len]+arr[len+1]);
}
}
