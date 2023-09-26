Example 1:
Input:
12345
3
Output:
12543

Example 2:
Input:
6745424
4
Output:
6745424
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include<stdio.h>
int main()
{
long M;
int X,arr[1001],k=0;
scanf("%ld\n%d",&M,&X);
while(M!=0)
{
arr[k++]=M%10;
M/=10;
}
for(int i=k-1;i>=x;i--)
{
printf("%d",arr[j]);
}
for(int j=0;j<X;j++)
{
printf("%d",arr[i]);
}
}
