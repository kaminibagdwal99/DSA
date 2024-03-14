"""
a tree is a non linear hireachical  data structure which is consist of nodes 
connected by edges.

Binary Tree: A tree in which each node has at most two children, referred to as
 the left child and the right child.

Binary Search Tree (BST): A binary tree in which the left child of a node contains
 only nodes with keys less than the node's key, and the right child contains only 
 nodes with keys greater than the node's key.

AVL Tree: A self-balancing binary search tree in which the heights of the two child
 subtrees of any node differ by at most one.

Basic terminology:

    Node: The basic unit of a tree, which can hold some data and may have a reference 
    to its child nodes.

    Root: The topmost node in a tree. It is the starting point for traversing the tree.

    Parent: A node that has one or more child nodes.

    Child: A node that has a parent node.

    Leaf: A node that does not have any children.

    Internal Node: A node that has at least one child.

    Sibling: Nodes that share the same parent.

    Depth: The level of a node in the tree, with the root node being at depth 0.

    Height: The length of the longest path from a node to a leaf. The height of a tree 
    is the height of its root node.

    subtree: the accessed node and the entire tree beneath it is called subtree.
    In a tree data structure, each node can be considered as the root of a subtree 
    formed by its child nodes and their descendants. For example, in a binary tree, if
    we consider a node and all its descendants, including their children and further
    descendants, we form a subtree rooted at that node.

    why use trees:
    Data Structure like array, list , stack , queue are linear Data Dtructure which store
    data sequenctially, where increase in data size will increase the time comploexity  
"""

"""Binary tree represenation in python"""


class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.left = left
        self.right= right



node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(7)
node.right.left =TreeNode(6)


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.right, level + 1)

print_tree(node)