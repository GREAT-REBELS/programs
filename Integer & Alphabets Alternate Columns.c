The program must accept an odd integer N as the input. Then the program must print the desired pattern as shown in the Example Input/Output section.
Note: After z in the pattern, a must repeat again in the next line.

Example Input/Output 1:
Input:
5
Output:
1
2 a
3 b 1
4 c
5
Example Input/Output 2:
Input:
7
Output:
1
2 a
3 b 1
4 c 2 a
5 d 3
6 e
7
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>

int main() {
  int N;
  scanf("%d", & N);
  int D = 1;
  for (int i = 0; i < N; i++) {
    int dig = i + 1;
    char ch = 'a';
    if (ch == 'z') {
      ch = 'a';
    }
    ch += (dig - 2);
    for (int j = 0; j < D; j++) {
      if (j % 2 == 0) {
        printf("%d ", dig);
        dig -= 2;
      } else {
        printf("%c ", ch);
        ch -= 2;
      }
    }
    if (i < N / 2) {
      D++;
    } else {
      D--;
    }
    printf("\n");
  }
}
