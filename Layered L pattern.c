The program must accept two integers N and X as the input.The program must print the desired pattern as shown in the example Input/Output section.

Example Input/Output 1:
Input:
5
Output:
1 
1 2 
1 2 3 
1 2 2 2 
1 1 1 1 1 

Example Input/Output 2:
Input:
10
Output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 5 
1 2 3 4 4 4 4 
1 2 3 3 3 3 3 3 
1 2 2 2 2 2 2 2 2 
1 1 1 1 1 1 1 1 1 1 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
int main()
{
    int N,T;
    scanf("%d",&N);
    if(N%2==0) T=N/2;
    else T = N/2+1;
    int L = N/2-1;
    for(int i=0; i<N; i++) {
        int D=1;
        if(i<T) {
            for(int j=0; j<=i; j++) {
                printf("%d ",D++);
            }
            printf("\n");
        } else {
            for(int j=0; j<=i; j++) {
                if(j>=L) {
                    printf("%d ",D);
                } else {
                    printf("%d ",D++);
                }
            }
            L--;
            printf("\n");
        }
    }
}
