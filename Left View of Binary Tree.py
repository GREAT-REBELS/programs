Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree
as argument. If no left view is possible, return an empty tree.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /   \    /    \
  4      5   6    7
   \
     8   

Examples :

Input:
   1
 /  \
3    2
Output: 1 3

Input:
  10 
 /  \
20   30
/
40
Output: 10 20 40
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def helper(node,res,level):
    if node:
        if len(res) < level:
            res.append(node.data)
        helper(node.left,res,level+1)
        helper(node.right,res,level+1)
def LeftView(root):
    res = [] 
    helper(root,res,1)
    return res 
