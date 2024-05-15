"""the diameter of the binary tree is the length of the longest path betwen any two node
in a tree"""

class NodeTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val,
        self.right = right
        self.left = left

a = NodeTree(5)
a.left = NodeTree(2)
a.right = NodeTree(3)
a.left.right = NodeTree(6)
a.right.left = NodeTree(7)
a.right.right = NodeTree(1)
a.right.left.right = NodeTree(8)



def print_tree(node, level=0):
    if node is not None:
        print_tree(node.left, level + 1)
        print(' ' * 8 * level + '->', node.val)
        print_tree(node.right, level + 1)

print_tree(a)