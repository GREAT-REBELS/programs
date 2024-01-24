The program must accept an integer N and a string S containing only alphabets as the input.The program must print the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
3
SkillRack
Output:
Sk*ll*ac*
S**l**a**
*********

Example Input/Output 2:
Input:
5
keyboard
Output:
KeyBoard
KeyB*ard
Key**ard
Ke***ar*
K****a**
********
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include<string.h>

int main() {
  int N;
  scanf("%d", & N);
  char str[101];
  scanf("%s", str);
  int D = N;
  int len = strlen(str);
  for (int i = 0; i < N; i++) {
    int cnt = 0;
    for (int j = 0; j < len; j++) {
      if (str[j] != '*') {
        cnt++;
      }
      if (cnt == D) {
        str[j] = '*';
        cnt = 0;
      }
    }
    D--;
    printf("%s\n", str);
  }
}
