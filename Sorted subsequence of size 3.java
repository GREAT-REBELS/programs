You are given an array arr, you need to find any three elements in it such that arr[i] < arr[j] < arr[k] and i < j < k.
Note:
The output will be 1 if the subsequence returned by the function is present in the array arr
If the subsequence is not present in the array then return an empty array, the driver code will print 0.
If the subsequence returned by the function is not in the format as mentioned then the output will be -1.

Examples :
Input: arr = [1, 2, 1, 1, 3]
Output: 1
Explanation: A subsequence 1 2 3 exist.

Input: arr = [1, 1, 3]
Output: 0
Explanation: No such Subsequence exist, so empty array is returned (the driver code automatically prints 0 in this case).
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution {
    public List<Integer> find3Numbers(int[] arr) {
        int N = arr.length; 
        int [] leftMin = new int[N];
        int [] rightMax = new int[N];
        leftMin[0] = arr[0];
        for(int i = 1;i < N;i++){
            leftMin[i] = Math.min(leftMin[i-1],arr[i]);
        }
        rightMax[N-1] = arr[N-1];
        for(int i=N-2;i>=0;i--){
            rightMax[i] = Math.max(rightMax[i+1],arr[i]);
        }
        for(int i=0;i<N;i++){
           if (arr[i] > leftMin[i] && arr[i] < rightMax[i]) {
                List<Integer> res = new ArrayList<>();
                res.add(leftMin[i]); res.add(arr[i]);res.add(rightMax[i]);
                return res;
            }
        }
        return new ArrayList<>();
    }
}
