Input:
1 0 1 
1 1 1 
1 1 0
Output: 1 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
int main()
{
int N,count=0;
scanf("%d",&N);
int matrix[N][N];
for(int i=0;i<N;i++)
{
    for(int j=0;j<N;j++)
    {
        scanf("%d",&matrix[i][j]);
    }
}
for(int i=0;i<N-1;i++)
{
    for(int j=0;j<N-1;j++)
    {
        if(matrix[i][j]==1 && matrix[i][j+1]==1 && matrix[i+1][j]==1 && matrix[i+1][j+1]==1)
        {
            count++;
        }
    }
}
printf("%d",count);
}
