"""iterative preorder traversal can be done using root left right"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right  = right

def preorder(root):
    if not root:
        return []
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
        
    return result



node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)

print(preorder(node))