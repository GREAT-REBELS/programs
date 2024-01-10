The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
4
Output:
0 2 4 8 
1 0 6 10 
3 7 0 12 
5 9 11 0 
  
Example Input/Output 2:
Input:
7
Output:
0 2 4 8 14 22 32 
1 0 6 10 16 24 34 
3 13 0 12 18 26 36 
5 15 23 0 20 28 38 
7 17 25 31 0 30 40 
9 19 27 33 37 0 42 
11 21 29 35 39 41 0 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
#include <stdio.h>

int main() {
  int N;
  scanf("%d", & N);
  int mat[N][N];
  int D1 = 2, D2 = 1;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (i == j) {
        mat[j][i] = 0;
      } else if (i > j) {
        mat[j][i] = D1;
        D1 += 2;
      } else {
        mat[j][i] = D2;
        D2 += 2;
      }
    }
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      printf("%d ", mat[i][j]);
    }
    printf("\n");
  }

}
