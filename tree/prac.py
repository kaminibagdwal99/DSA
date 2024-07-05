class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def balanced(root):
    def dfs(root):
        if not root : return [True,0]
        left,right = dfs(root.left), dfs(root.right)

        balanced = left[0] and right[0] and abs(left[1]-right[1]<=1)
        return [balanced, 1+max(left[1], right[1])]
    return dfs(root)[0]
    
    

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
node.right.right.left =TreeNode(6)

a = balanced(node)
print(a)