#include <stdio.h>
int binarysearch(int arr[],int N,int k)
{
    int left=0,right=N-1;
    while(left<=right)
    {
        int mid=(left+right)/2;
        if(arr[mid]==k)
        {
            return mid;
        }
        else if(arr[mid]<k)
        {
            left=mid+1;
        }
        else
        {
            right=mid-1;
        }
    }
    return -1;
}
int main()
{
int N,k;
scanf("%d",&N);
int arr[N];
for(int i=0;i<N;i++)
{
    scanf("%d ",&arr[i]);
}
scanf("\n%d",&k);
int D=binarysearch(arr,N,k);
if(D!=-1)
{
    printf("Element found at %d",D);
}
else
{
    printf("Element not present");
}
}
