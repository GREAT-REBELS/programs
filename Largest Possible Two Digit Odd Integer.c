The program must accept two integers X and Y as the input. The program must choose exactly one digit from the digits of X and exactly one digit from the digits of Y. The program must form the largest possible
two-digit odd integer T from the choosen digits. If it is not possible to form T, the program must print -1 as the output.

Example Input/Output 1:
Input: 1
684 3457
Output: 
87
Explanation: All possible two-digit odd integers are 13, 15, 17, 63, 65, 67, 83, 85, 87, 43, 45, 47, 31, 41, 51 and 71.
Here the largest possible two-digit odd integer is 87. Hence the output is 87

Example Input/Output 2:
Input:
48 802
Output:
-1

Example Input/Output 3:
Input:
9088 296
Output:
99
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include <math.h>
int *sort(int arr[],int N) 
{
    for(int i=0;i<N;i++)
    {
        for(int j=i+1;j<N;j++)
        {
            if(arr[i]>arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    return arr;
}
int main()
{
int A,B;
scanf("%d %d",&A,&B);
int a1[51],a2[51],k1=0,k2=0;
while(A!=0)
{
    a1[k1++] = A%10;
    A/=10;
}
while(B!=0)
{
    a2[k2++] = B%10;
    B/=10;
}
int *arr1 = sort(a1,k1);
int *arr2 = sort(a2,k2);
int max=0;
for(int i=0;i<k1;i++)
{
    for(int j=0;j<k2;j++)
    {
        int D1 = arr1[i]*10+arr2[j];
        int D2 = arr2[j]*10+arr1[i];
        if(D1%2!=0)
          max = fmax(D1,max);
        if(D2%2!=0)
          max = fmax(D2,max);
    }
}
if(max==0)
  printf("-1");
else
  printf("%d",max);
}
