The program must accept a character matrix of size RxC as the input. The program must print the number of diagonals having only vowels that are parallel to the top-left to bottom-right diagonal and the top-right
to bottom-left diagonal in the matrix.

Example Input/Output 1:
Input:
4 4
u m o a
i n a q
y e r w
i n o e
Output:
6
Explanation:
The diagonals that are parallel to the top-left to bottom-right diagonal and having only vowels are highlighted below.
u m o 'a'
'i' n a q
y 'e' r w
'i' n 'o' e
The diagonals that are parallel to the top-right to bottom-left diagonal and having only vowels are highlighted below.
'u' m o 'a'
i n 'a' q
y 'e' r w
'i' n o 'e'
The total number of diagonals with only vowels is 6. So 6 is printed as the output.

Example Input/Output 2:
Input:
5 4
Y O V A
k L v d
H q L h
j A v u
e O a R
Output:
3 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.Scanner;
public class Main
{
    static boolean isVowel(char ch){
        return "aeiouAEIOU".indexOf(ch)!=-1;
    }
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int R = sc.nextInt();
		int C = sc.nextInt();
		char mat[][] = new char[R][C];
		for(int i=0;i<R;i++){
		    for(int j=0;j<C;j++){
		        mat[i][j] = sc.next().charAt(0);
		    }
		}
		int res = 0;
		boolean flg = true;
		//topleft to bottomRight 
		for(int i=0;i<C;i++){
		    flg = true;
		    for(int row=0,col=i;row<R && col<C;row++,col++){
		        if(!isVowel(mat[row][col])){
		            flg = false;
		            break;
		        }
		    }
		    if(flg)
		       res+=1;
		}
		for(int i=1;i<R;i++){
		    flg = true;
		    for(int row=i,col=0;row<R && col<C;row++,col++){
		        if(!isVowel(mat[row][col])){
		            flg = false;
		            break;
		        }
		    }
		    if(flg)
		       res+=1;
		}
		//topRight to bottomleft 
		for(int i=C-1;i>=0;i--){
		    flg = true;
		    for(int row=0,col=i;row<R && col>=0;row++,col--){
		        if(!isVowel(mat[row][col])){
		            flg = false;
		            break;
		        }
		    }
		    if(flg)
		       res+=1;
		}
		for(int i=1;i<R;i++){
		    flg = true;
		    for(int row=i,col=C-1;row<R && col>=0;row++,col--){
		        if(!isVowel(mat[row][col])){
		            flg = false;
		            break;
		        }
		    }
		    if(flg)
		       res+=1;
		}
		System.out.print(res);
	}
}
