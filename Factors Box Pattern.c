The program must accept an integer N as the input. The program must find the factors of N and print the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input: 6
Output
1111111
1222221
1233321
1236321
1233321
1222221
1111111
    
Example Input/Output 2:
Input: 7
Output
111
171
111
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
int main()
{
int N;
scanf("%d",&N);
int arr[101],D=0;
for(int i=1;i<=N;i++){
    if(N%i==0){
        arr[D++] = i;
    }
}
for(int i=1;i<=2*D-1;i++){
    int k=0;
    if(i<=N){
        for(int j=1;j<=2*D-1;j++){
            printf("%d ",arr[k]);
            if(i>j){
                k++;
            }
            if((i+j)>=(2*D)){
                k--;
            }
        }
         printf("\n");
    }
    else{
        for(int j=1;j<=2*D-1;j++){
            printf("%d ",arr[k]);
            if(i+j<(2*D)){
                k++;
            }
            if(i<=j){
                k--;
            }
        }
         printf("\n");
        
    }
}
}
