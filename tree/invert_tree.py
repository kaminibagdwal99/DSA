class TreeNode:
    def __init__(self, val= 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def invert_tree(self):

        if self is None:
            return None
        self.left,self.right = self.right, self.left
        if self.left:
            self.left.invert_tree()
        if self.right:
            self.right.invert_tree()




a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left =TreeNode(6)
a.right.right = TreeNode(7)

def print_tree(node, level = 0):
    if  node is not None:
        print_tree(node.left, level+1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.right, level+1)


print_tree(a)
a.invert_tree()
print()
print_tree(a)

