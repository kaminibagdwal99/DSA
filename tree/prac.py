class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node, level =0):
    if node is not None:
        print_tree(node.right, level+1)
        print(" "*level  *4+'->',node.value)
        print_tree(node.left, level+1)

from collections import deque
class Solution:
    def rightSideView(self, node):
        res = []
        queue = deque([node])

        while queue:
            l_size = len(queue)
            r_node = []

            for _ in range(l_size):
                root = queue.popleft()
                r_node.append(root.value)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if r_node:
                res.append(r_node)
        return res
    
    def isSameTree(self, p,q):
        if not p and not q:
            return True
        if not p or not q or p.value != q.value:
            return False
        return (self.isSameTree(p.left, q.left )) and (self.isSameTree(p.right, q.right))




node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)

node2 = TreeNode(1)
node2.right = TreeNode(2)
node2.left = TreeNode(2)


a = Solution()
print(a.isSameTree(node, node2))