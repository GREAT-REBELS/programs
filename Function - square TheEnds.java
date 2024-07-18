You must implement the function squareTheEnds(int N) which accepts an integer N as the input. The function must form an integer X by replacing the first and last digits of N with its square value. Then the 
function must return the integer X.
Note: Do not define the main() function as it is already defined. You just return the integer X as per the given condition. The value of X will be printed by the main() function.

Example Input/Output 1:
Input: 
888
Output: 
64864
Explanation:
Here N = 888.
After replacing the first and last digits of the integer 888 with its square value, the integer becomes 64864.
So 64864 is printed as the output.

Example Input/Output 2:
Input: 
5000
Output: 
25000

Example Input/Output 3:
Input: 
123
Output: 
129
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
public static int squareTheEnds(int N) {
  String str = Integer.toString(N);
  String X = "";
  int firstDigit = Character.getNumericValue(str.charAt(0));
  int lastDigit = Character.getNumericValue(str.charAt(str.length() - 1));
  X = (firstDigit * firstDigit) + str.substring(1, str.length() - 1) + (lastDigit * lastDigit);
  return Integer.parseInt(X);
}
