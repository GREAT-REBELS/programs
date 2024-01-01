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

