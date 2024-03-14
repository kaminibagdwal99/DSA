class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.left = left
        self.right= right

def Inordertransversal(root):
    if not root:
        return []
    
    return Inordertransversal(root.left) + [root.val] + Inordertransversal(root.right)


node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(7)
node.right.left =TreeNode(6)
 
root = node

result = Inordertransversal(root)
print(result)