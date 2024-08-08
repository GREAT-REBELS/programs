Given a Binary Tree. Check for the Sum Tree for every node except the leaf node. Return true if it is a Sum Tree otherwise, return false.
A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present in its left subtree and right subtree. An empty tree is also a Sum Tree as the sum of an empty tree can be considered to 
be 0. A leaf node is also considered a Sum Tree.

Examples :
Input:
    3
  /   \    
 1     2
Output: true
Explanation: The sum of left subtree and right subtree is 1 + 2 = 3, which is the value of the root node. Therefore,the given binary tree is a sum tree.

Input:
          10
        /    \
      20      30
    /   \ 
   10    10
Output: false
Explanation: The given tree is not a sum tree. For the root node, sum of elements in left subtree is 40 and sum of elements in right subtree is 30. Root element = 10 which is not equal to 30+40.  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def is_sum_tree(self, node):
        self.isSumTree = True
        def getSum(node):
            if not node:
                return 0
            if not (node.left or node.right):
                return node.data
            subTree_Sum = getSum(node.left) + getSum(node.right)
            if node.data != subTree_Sum:
                self.isSumTree = False
            return node.data + subTree_Sum
        getSum(node)
        return self.isSumTree
