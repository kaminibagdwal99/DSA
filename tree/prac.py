class TreeNode:
    def __init__(self, val=0):
        self.val=val
        self.left = None
        self.right = None





def invert_tree(a):
    if not a: return None
    a.left, a.right = a.right, a.left
    if a.left:
        invert_tree(a.left)
    if a.right:
        invert_tree(a.right)
    return a

def max_depth(a):
    if not a :return 0
    left = max_depth(a.left)
    right = max_depth(a.right)
    maxdepth = 1+ max(left, right)
    return maxdepth

def isSameTree(p,q):
    if not p and not q: return True
    if not p or not q or p.val!=q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def print_tree(a,level=0):
    if a is not None:
        print_tree(a.right, level+1)
        print(" "*level*4 , "->",a.val)
        print_tree(a.left, level+1)


def isSubtree(s,t):
    if not t: return True
    if not s:
        return False
    
    if  isSameTree(s, t):
        return True
    
    return isSubtree(s.left, t.left) or isSubtree(s.right, t.right)


def lowestCommonAncestor(root, p, q):
    cur=root
    while cur:
        if p.val > cur.val and q.val>cur.val:
            cur= cur.right
        elif p.val < cur.val and q.val>cur.val:
            cur= cur.left
        else:
            return cur.val
        
from collections import deque
def levelorder(node):
    if not node:
        return []
    queue = deque([node])
    result =[]

    while queue:
        levesize = len(queue)
        levelnode = []


        for _ in range(levesize):
            node = queue.popleft()
            levelnode.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(levelnode)
    return result

def lefttSideView(a):
    q = deque([a])
    res=[]
    while q:
        size = len(q)
        lnode=None

        for i in range(size):
            node = q.popleft()
            if node:
                lnode= node
                q.append(node.right)
                q.append(node.left)
        if lnode:
            res.append(lnode.val)
    return res


def bottom_view(root):
    res=[]
    col=0
    q=[[root, col]]
    map={}
    while q:
        node = q.pop(0)
        cur= node[0]
        val = node[0].val
        col = node[1]

        if col not in map:
            map[col]=val

        if cur.left:
            q.append([cur.left, col-1])
        if cur.right:
            q.append([cur.right, col+1])
    key = []
    for i in map.keys():
        key.append(i)
    key.sort()

    for i in key:
        res.append(map[i])
    return res




node = TreeNode(20)
node.left = TreeNode(8)
node.right = TreeNode(22)
node.left.left = TreeNode(5)
node.left.right = TreeNode(3)
node.right.left = TreeNode(4)
node.right.right = TreeNode(25)
node.left.right.left = TreeNode(10)
node.right.left.right = TreeNode(14)


print_tree(node)

print(bottom_view(node))


        