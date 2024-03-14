"""iterative preorder traversal can be done using stack. i stack we add left we 
transverse from node and then save first left and seconf left and so on until left item 
exist """

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right  = right

def inorder(root):
    if not root:
        return []
    stack = []
    result = []
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left

        else:
            node = stack.pop()
            result.append(node.val)
            current = node.right
        
    return result




node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(7)
node.right.left =TreeNode(6)

print(inorder(node))