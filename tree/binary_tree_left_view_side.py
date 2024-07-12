"""
Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument. If no left view is possible, return an empty tree.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   
"""
from collections import deque
class TreeNode:
    def __init__(self, value=0,left = None, right = None ) :
        self.value = value
        self.left = left
        self.right = right
class Solution:
    def lefttSideView(self,node):
        res = []
        queue = deque([node])

        while queue:
            lsize = len(queue)
            lnode  =None

            for _ in range(lsize):
                root = queue.popleft()
                if root:
                    lnode = root

                    queue.append(root.right)
                    queue.append(root.left)
            if lnode:
              res.append(lnode.value)
        return res

            
                    

def print_tree(node, level=0):
    if node :
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.right, level + 1)

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(5)
a.right.right = TreeNode(4)
a.right.right.right = TreeNode(6)


print_tree(a)
z = Solution()
print(z.lefttSideView(a))
