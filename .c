---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include<math.h>
int main()
{
int N,M;
scanf("%d %d",&N,&M);
int arr1[N],arr2[M];
for(int i=0;i<N;i++)
{
    scanf("%d",&arr1[i]);
}
for(int i=0;i<M;i++)
{
    scanf("%d",&arr2[i]);
}
int cnt=0;
for(int i=0;i<N;i++)
{
    int cnt1=log10(arr1[i])+1;
    for(int j=0;j<M;j++)
    {
        int cnt2=log10(arr2[j])+1;
        if(cnt1!=cnt2)
        {
            cnt++;
        }
    }
}
printf("%d",cnt);
}
