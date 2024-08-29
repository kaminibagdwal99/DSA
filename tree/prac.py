class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

def invert_tree(p):
    if not p : return 0
    left = invert_tree(p.left)
    right = invert_tree(p.right)
    max_depth = 1+ max(left,right)

    return max_depth





node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)

 
root = node

print(postorder_transversal(root))