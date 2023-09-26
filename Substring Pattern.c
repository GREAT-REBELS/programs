Example 1:
Input:
skillrack
Output:
skillrack
*carllik
**illra
***rll
****l

Example 2:
Input:
first
Output:
first
*sri
**r
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include<string.h>
int main ()
{
char str[101];
scanf ("%s", str);
int lst = strlen (str) - 1, frst = 0;
int l = strlen (str) / 2,i=0;
printf ("%s\n", str);
while (strlen (str) > 1)
  {
  for (int i = 0; i <= frst; i++)
	{
	  printf ("*"); //based on the incremented first value we are printing '*' Symbols.
	}
  if (i % 2 != 0)
	{
	  for (int i = frst + 1; i < lst; i++)
	    {
	      printf ("%c", str[i]);
	    }
	}
      else
	{
	  for (int i = lst - 1; i > frst; i--)
	    {
	      printf ("%c", str[i]);
	    }
	}
      printf ("\n");
      frst++;
      lst--;
      i++;
   if (frst == l) //when first reaches l we break the loop.
	{
	  break;
	}
 }
}
