The height of N cats are passed as the input. The program must print the height of the cats graphically as a column chart represented by # and - as 
shown in the Example Input/Output

Example Input/Output 1:
Input:
6 
10 4 2 6 7 2
Output:
# - - - - - 
# - - - - - 
# - - - - - 
# - - - # - 
# - - # # - 
# - - # # - 
# # - # # - 
# # - # # - 
# # # # # # 
# # # # # # 

Example Input/Output 2:
Input:
10 
1 2 3 4 5 6 7 8 9 10
Output:
- - - - - - - - - # 
- - - - - - - - # # 
- - - - - - - # # # 
- - - - - - # # # # 
- - - - - # # # # # 
- - - - # # # # # # 
- - - # # # # # # # 
- - # # # # # # # # 
- # # # # # # # # # 
# # # # # # # # # # 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
int main()
{
int N;
scanf("%d\n",&N);
int arr[N],max=0;
for(int i=0;i<N;i++)
{
    scanf("%d",&arr[i]);
    if(arr[i]>max)
    {
        max = arr[i];
    }
}
for(int i=0;i<max;i++)
{
    for(int j=0;j<N;j++)
    {
        if(i==max-arr[j])
        {
            printf("# ");
            arr[j]-=1;
        }
        else
        {
            printf("- ");
        }
    }
    printf("\n");
}
}
