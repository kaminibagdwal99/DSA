"""Postoder transversal By recusrsion  left right root"""


class TreeNode:
    def __init__(self, val = 0, right=None,left=None):
        self.val = val
        self.right = right
        self.left = left

def postorder_transversal(root):
    if not root:
        return []

    return postorder_transversal(root.left)+postorder_transversal(root.right)+[root.val]

node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)

 
root = node

print(postorder_transversal(root))
