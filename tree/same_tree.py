"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p , q ) -> bool:
        if not p and not q :
            return True
        
        if not p or not q or p.val !=q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        


node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)

node2 = TreeNode(1)
node2.right = TreeNode(2)
node2.left = TreeNode(3)


a = Solution()
print(a.isSameTree(node, node2))
        