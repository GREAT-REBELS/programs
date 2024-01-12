#include<stdio.h>

int main() {
  int N;
  scanf("%d", & N);
  for (int i = 0; i < N; i++) {
    int D = -1;
    for (int j = N - i - 1; j > 0; j--) {
      printf("-");
    }
    for (int k = 0; k < i * 2 + 1; k++) {
      if (k <= (i * 2 + 1) / 2) {
        D += 2;
        printf("%d", D);
      } else {
        D -= 2;
        printf("%d", D);
      }
    }
    printf("\n");
  }
}
