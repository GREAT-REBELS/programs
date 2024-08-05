Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level traversal is considered. For example, in the below diagram, 3 and 4 are both the bottommost
nodes at a horizontal distance of 0, here 4 will be considered.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14
For the above tree, the output should be 5 10 4 14 25.

Examples :
Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation: First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.

Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def bottomView(self, root):
        queue = [[root,0]]
        dict_ = {} 
        while queue:
            node = queue.pop(0)
            curr = node[0]
            val = node[0].data 
            col = node[1]
            dict_[col] = val  
            if curr.left:
                queue.append([curr.left,col-1])
            if curr.right:
                queue.append([curr.right,col+1])
        res = []
        for key in sorted(dict_):
            res.append(dict_[key])
        return res
