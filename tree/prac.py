class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

def isSameTree(p,q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
             return False
        
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)




node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(3)

node2 = TreeNode(1)
node2.right = TreeNode(2)
node2.left = TreeNode(3)



print(isSameTree(node, node2))