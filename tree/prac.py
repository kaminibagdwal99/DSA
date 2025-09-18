class TreeNode:
    def __init__(self, val=0):
        self.val=val
        self.left=None
        self.right = None


def print_tree(a, level=0):
    cur =a
    if cur:
        print_tree(a.right, level+1)
        print(level*4 * " ", "->",cur.val)
        print_tree(a.left, level+1)

def invert_tree(a):
    if not a:
        return None
    a.left, a.right = a.right, a.left
    if a.left:
        invert_tree(a.left)
    if a.right:
        invert_tree(a.right)
    return a
def max_depth(node):
    if not node: return 0
    left = max_depth(node.left)
    right = max_depth(node.right)
    return 1 +max(left, right)

def isSameTree(p,q):

    if not p and not q:
        return True
    if not p or not q or p.val!=q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSubtree(s,t):
    if not t :
        return True
    if not s:
        return False
    if isSameTree(s,t):return True

    return isSubtree(s.left,t) or isSubtree(s.right, t)

def lowestCommonAncestor(root, p, q):
    cur=root
    while cur:
        if p.val>cur.val and q.val>cur.val:
            cur=cur.right
        elif p.val<cur.val and q.val<cur.val:
            cur=cur.left
        else:
            return cur.val
        
from collections import deque
def levelorder(root):
    q= deque([root])
    res=[]
    while q:
        level_size = len(q)
        level_node = []
        for _ in range(level_size):
            node = q.popleft()
            level_node.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level_node)
    return res
def rightSideView(root):
    q= deque([root])
    res=[]
    while q:
        level_size = len(q)
        right_node = None
        for _ in range(level_size):
            node= q.popleft()
            if node:
                right_node = node.val
                q.append(node.right)
                q.append(node.left)
        if right_node:
            res.append(right_node)
    return res
def bottom_view(root):
    col=0
    map={}
    res=[]
    q = [[root, col]]
    while q:
        node = q.pop(0)
        val = node[0].val
        col = node[1]
        cur = node[0]
        if col not in map:

            map[col]=val

        if cur.left:
            q.append([cur.left, col-1])
        if cur.right:
            q.append([cur.right, col+1])
    key =[]
    for i in map.keys():
        key.append(i)
    key.sort()

    for i in key:
        res.append(map[i])
    return res
def Inordertransversal(root):
    if not root:
        return []
    return Inordertransversal(root.left)+ Inordertransversal(root.right)+ [root.val]

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
