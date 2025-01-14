"""Preoder transversal By recusrsion root left right"""


class TreeNode:
    def __init__(self, val = 0, right=None,left=None):
        self.val = val
        self.right = right
        self.left = left

def preorder_transversal(root):
    if not root:
        return []

    return [root.val] + preorder_transversal(root.left) +preorder_transversal(root.right)

node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)

 


print(preorder_transversal(node))
