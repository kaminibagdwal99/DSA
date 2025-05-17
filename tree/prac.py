class TreeNode:
    def __init__(self, value = 0, right = None, left = None):
        self.value = value 
        self.left = left
        self.right = right




def print_tree(node, level=0):
    if node:
        print_tree(node.left, level+1)
        print(" "*4*level+ "->",node.value)
        print_tree(node.right, level+1)
    
def invert_tree(root):
    if not root:
        return None
    if root.left:
        invert_tree(root.left)
    if root.right:
        invert_tree(root.right)
    root.left, root.right = root.right, root.left
    return root

def max_depth(root):
    depth=0
    if not root:
        return  depth
    left = max_depth(root.left)
    right = max_depth(root.right)
    depth = 1 + max(left, right)
    return depth


def same_tree(p,q):
    if not p and not q:
        return True
    if not p or not q or p.value != q.value:
        return False

    return same_tree(p.left, q.left) and same_tree(p.right, q.right)

def isSubtree(s,t):
    if not t: return True
    if not s: return False

    if same_tree(s,t):
        return True
    
    return isSubtree(s.left, t) or isSubtree(s.right, t)

def lowestCommonAncestor(node, p ,q):
    pass

node = TreeNode(6)
node.left = TreeNode(2)
node.right = TreeNode(8)
node.left.left = TreeNode(0)
node.left.right = TreeNode(4)
node.right.left = TreeNode(7)
node.right.right = TreeNode(9)
node.left.right.left = TreeNode(3)
node.left.right.right = TreeNode(5)

print(lowestCommonAncestor(node, node.left,node.left.right))

    


    