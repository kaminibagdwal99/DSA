class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


def BFS(node):
    res = []
    q = deque([node])
    while q:
        lorder = len(q)
        lnode=[]
        for _ in range(lorder):
            node = q.popleft()
            lnode.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
        res.append(lnode)
    return res
    
    

def print_tree(node, level=0):
    if node :
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.right, level + 1)



    
    

node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(7)
node.right.left =TreeNode(6)

print_tree(node)
a = BFS(node)
print(a)