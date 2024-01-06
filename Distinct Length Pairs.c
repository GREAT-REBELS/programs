The program must accept M integers and N integers as the input. The program must form pairs of integers by selecting one integer from M integers and another 
integer from N integers. Then the program must print the number of pairs containing two integers with different number of digits as the output.

Example Input/Output 1:
Input:
34
12 1 454
988 2 112 47
Output: 8
Explanation:
The pairs with two different length integers are
12 988
12 2
12 112
1988
1 112
147
454 2
454 47
    
Example Input/Output 2:
Input:
5 10
9 62
464 69 1
69 26 22 252 28 172 341 9 5 592
Output:
34
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include<math.h>
int main()
{
int N,M;
scanf("%d %d",&N,&M);
long int arr1[N],arr2[M];
for(int i=0;i<N;i++)
{
    scanf("%ld",&arr1[i]);
}
for(int i=0;i<M;i++)
{
    scanf("%ld",&arr2[i]);
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
