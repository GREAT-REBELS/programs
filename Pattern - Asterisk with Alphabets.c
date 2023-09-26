The program must accept an integer N as the input. The program must print the desired pattern as shown in the example.
Example Input/Output 1:
Input:
4
Output:
***A
**ABA
*ABCBA
ABCDCBA

Example Input/Output 2:
Input:
7
Output:
******A
*****ABA
****ABCBA
***ABCDCBA
**ABCDEDCBA
*ABCDEFEDCBA
ABCDEFGFEDCBA
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
int main()
{
int N;
char ch='A';
scanf("%d",&N);
for(int i=1;i<=N;i++)
{
    ch='A';
    for(int j=N-i-1;j>=0;j--)
    {
        printf("*");
    }
    for(int k=0;k<(2*i)-1;k++)
    {
        int mid=((2*i)-1)/2;
        if(k<mid)
        {
            printf("%c",ch++);
        }
        else
        {
            printf("%c",ch--);
        }
    }
    printf("\n");
}
}

