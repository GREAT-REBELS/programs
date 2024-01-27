The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
6
Output:
1 * * * * 2
* 3 * * 4 *
* * 5 6 * *
* * 7 8 * *
* 9 * * 10 *
11 * * * *  12
Example Input/Output 2:
Input:
5
Output:
1 * * * 2
* 3 * 4 *
* * 5 * *
* 6 * 7 *
8 * * * 9
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>

int main() {
  int N;
  scanf("%d", & N);
  int k = 1, strt = 0, end = N - 1;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (j == strt || j == end) {
        printf("%d ", k++);
      } 
      else {
        printf("* ");
      }
    }
    strt++;
    end--;
    printf("\n");
  }
}
