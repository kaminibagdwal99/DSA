"""max depth of the tree a or maximum height of the tree"""

class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.left = left
        self.right= right

def max_depth(root):
    if not root: return 0
    left = max_depth(root.left)
    right = max_depth(root.right)

    max_height = 1 +max(left,right) 

    return max_height


node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(7)
node.right.left =TreeNode(6)


print(max_depth(node))