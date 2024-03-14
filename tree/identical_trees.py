class TreeNode:
    def __init__(self, val = 0, left=None , right=None):
        self.val = val
        self.left = left
        self.right = right
def check_balance(p,q):
    if not p and not q:
        return True

    return p.val == q.val and check_balance(p.left,q.left) and check_balance(p.right,q.right)

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)

print(check_balance(node,root))