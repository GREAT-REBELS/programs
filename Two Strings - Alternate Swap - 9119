Example Input/Output 1:                                  
Input:
abcdef
mnopqr
Output:
nmporq
badcfe

Example Input/Output 2:
Input:
abcdefg
mnopqrs
Output:
nmporqg
badcfes

Example Input/Output 3:                                
Input:
abcdefghijk
mnopqrs
Output:
nmporqgsijk
badcfeh

Example Input/Output 4:                                
Input:
abcdefg
mnopqrstuvw
Output:
nmporqt
badcfesguvw

Example Input/Output 5:                                
Input:
a
z
Output:
a
z
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include <string.h>
int main()
{
char s1[101],s2[101];
scanf("%s\n%s",s1,s2);
int len1=strlen(s1),len2=strlen(s2);
for(int i=0;i<len1;i++)
{
    if(i%2==0 && i+1<len2)
    {
        printf("%c",s2[i+1]);
    }
    else if(i%2!=0 && i-1<len2)
    {
        printf("%c",s2[i-1]);
    }
    else
    {
        printf("%c",s1[i]);
    }
}
printf("\n");
for(int i=0;i<len2;i++)
{
    if(i%2==0 && i+1<len1)
    {
        printf("%c",s1[i+1]);
    }
    else if(i%2!=0 && i-1<len2)
    {
        printf("%c",s1[i-1]);
    }
    else
    {
        printf("%c",s2[i]);
    }
}
printf("\n");
}
