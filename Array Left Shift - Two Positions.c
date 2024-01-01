The program must accept array of N integers as input. The program must shift the integers that occur between the positions X and Y (both inclusive) to the left by R times. The values X,Y and R also passed as 
the input. The program must print the revised array as the output,

Example Input/Output 1:
Input:
10
10 20 30 40 50 60 70 80 90 100
3 8
2
Output:
10 20 50 60 70 80 30 40 90 100
Explanation:
Here X = 3, Y = 8 and R = 2.
After 1 1st left shift, the array becomes 10 20 40 50 60 70 80 30 90 100.
After 2nd left shift, the array becomes 10 20 50 60 70 80 30 40 90 100.

Example Input/Output 2:
Input:
5
60 70 80 90
2 5 3
Output:
60 100 70 80 90
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
int main()
{
int N;
scanf("%d",&N);
int arr[N];
for(int i=0;i<N;i++)
{
    scanf("%d",&arr[i]);
}
int X,Y,R,i,j;
scanf("%d %d\n %d",&X,&Y,&R);
for(i=0;i<R;i++)
{
    int temp = arr[X-1];
    for(j=X-1;j<Y-1;j++)
    {
        arr[j] = arr[j+1];
    }
    arr[j] = temp;
}

for(int i=0;i<N;i++)
{
    printf("%d ",arr[i]);
}

}

