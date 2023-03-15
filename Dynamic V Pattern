Example Input/Output 1:
Input:
3 # 5
Output:
------#
-----#
#---#
-#-#
--#

Example Input/Output 2:
Input:
7 @ 7
Output:
@-----------@
-@---------@
--@-------@
---@-----@
----@---@
-----@-@
------@

Example Input/Output 3:
Input:
10 * 4
Output:
*
-*
--*
---*
----*
-----*
------*-----*
-------*---*
--------*-*
---------*



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include<stdio.h>
int main()
{
int x,y,max;
char ch;
scanf("%d %c %d",&x,&ch,&y);
if(x>y)
{
    max=x;
}
else
{
    max=y;
}
int start=1,end=(x+y)-1;
for(int i=max;i>=1;i--)
{
    int Dflg=0,Iflg=0;
    for(int j=1;j<=(x+y)-1;j++)
    {
        if(i<=x && j==start)
        {
            printf("%c",ch);
            Iflg=1;
        }
        else if(i<=y && j==end)
        {
            printf("%c",ch);
            Dflg=1;
        }
        else if(j<start || j<end && i<=y)
        {
            printf("-");
        }
    }
    if(Iflg==1)
    {
        start++;
    }
    if(Dflg==1)
    {
    end--;
    }
    printf("\n");
}
}
