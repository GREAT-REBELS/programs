An odd length string S is passed as the input.The Program must print the pattern starting from the middle letter as shown in the Example 
Input/Output section.
  
Example Input/Output 1:                                  
Input:
WATER
Output:
****T
***TE
**TER
*TERW
TERWA

Example Input/Output 2:
Input:
ABCDEFG
Output:
******D
*****DE
****DEF
***DEFG
**DEFGA
*DEFGAB
DEFGABC
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include<string.h>
int main() {
char str[101];
scanf("%s",str);
int end=strlen(str)-1;
for(int i=0;i<strlen(str);i++)
{
    int ind = strlen(str)/2;
    for(int j=0;j<strlen(str);j++)
    {
        if(j>=end)
        {
            printf("%c",str[ind]);
            ind++;
            if(ind>=strlen(str))
            {
                ind = 0;
            }
        }
        else
        {
            printf("*");
        }
    }
    end--;
    printf("\n");
}
}

  
