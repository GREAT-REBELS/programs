The program must accept two integers N and X as the input.The program must print the desired pattern as shown in the example Input/Output section.
Example Input/Output 1:
Input:
4
Output:
* * * * 
- * 1 2 * 
- - * 3 4 * 
- - - * * * * 

Example Input/Output 2:
Input:
5
Output:
* * * * * 
- * 1 2 3 * 
- - * 4 5 6 * 
- - - * 7 8 9 * 
- - - - * * * * * 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
int main()
{
    int N;
    scanf("%d",&N);
    int D=1;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<i;j++)
        {
            printf("- ");
        }
        if(i!=0 && i!=N-1)
        {
            for(int k=0;k<N;k++)
            {
                if(k==0 || k==N-1)
                {
                    printf("* ");
                }
                else
                {
                    printf("%d ",D++);
                }
            }
        }
        else
        {
            for(int i=0;i<N;i++)
            {
                printf("* ");
            }
        }
        printf("\n");
    }
}
