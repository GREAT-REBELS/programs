Given two positive integer arrays arr and brr, find the number of pairs such that xy > yx (raised to power of) where x is an element from arr and y is an element from brr.

Examples :
Input: arr[] = [2, 1, 6], brr[] = [1, 5]
Output: 3
Explanation: The pairs which follow xy > yx are: 21 > 12,  25 > 52 and 61 > 16 .

Input: arr[] = [2 3 4 5], brr[] = [1 2 3]
Output: 5
Explanation: The pairs which follow xy > yx are: 21 > 12 , 31 > 13 , 32 > 23 , 41 > 14 , 51 > 15 .
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution {
   public long countPairs(int x[], int y[], int M, int N) {
        Arrays.sort(x);
        Arrays.sort(y);
        int c0 = 0,c1 = 0,c2 = 0,c3 = 0,c4 = 0;
        for(int ele : y){
            if(ele == 0){
                c0++;
            }else if(ele == 1){
                c1++;
            }else if(ele == 2){
                c2++;
            }else if(ele == 3){
                c3++;
            }else if(ele == 4){
                c4++;
            }
        }
        int j = 0;
        long res = 0;
        for(int i=0;i<M;i++){
            if(x[i] == 0){
                continue;
            }
            if(x[i] == 1){
                res += c0;
            }
            else{
                res += c0 + c1;
                while(j<N && y[j] <= x[i]){
                    j++;
                }
                if(j<N){
                    res += N - j;
                }
                if(x[i] == 2){
                    res -= c3;
                    res -= c4;
                }
                if(x[i] == 3){
                    res += c2;
                }
            }          
        }
        return res;
    }
}
