The program must accept an even integer N as the input. The program must print the desired pattern as shown in the Example Input/Output  section. 
Example Input/Output 1:
Input:
6
Output:
123654
*1243
**12
Example Input/Output 2:
Input: 8
Output:
12348765
*123654
**1243
***12
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include<string.h>
int main()
{
int N;
scanf("%d",&N);
int D = N,T=N;
for(int i=0;i<N/2;i++)
{
    for(int k=0;k<i;k++)
    {
        printf("* ");
    }
    for(int j=0;j<D;j++)
    {
        if(j<D/2)
        {
            printf("%d ",j+1);
        }
        else
        {
            printf("%d ",T--);
        }
    }
    D-=2;
    T = D;
    printf("\n");
}
}
