The program must accept an integer N as the input. The program must find the binary representation of N and print the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
463
Output:
111
00
1111
Explanation:
  The Binary representation of 463 is 111001111.
Example Input/Output 2:
Input:
81
Output:
1
0
1
000
1
Explanation:
  The Binary representation of 81 is 1010001.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int N;
    scanf("%d",&N);
    int a[1001],k=0;
    while(N!=0)
    {
        a[k++] = N%2;
        N/=2;
    }
    for(int i=k-1;i>=0;i--)
    {
        if(a[i] == a[i-1])
        {
            printf("%d",a[i]);
        }
        else
        {
             printf("%d",a[i]);
             printf("\n");
        }
    }
 
}
