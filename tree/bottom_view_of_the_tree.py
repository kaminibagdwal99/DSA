"""
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.

Note: The Input/Output format and Example given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.
 

Example 1:

Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation:
First case represents a tree with 3 nodes
and 2 edges where root is 1, left child of
1 is 3 and right child of 1 is 2.

Thus nodes of the binary tree will be
printed as such 3 1 2.
Example 2:

Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30
Your Task:
This is a functional problem, you don't need to care about input, just complete the function bottomView() which takes the root node of the tree as input and returns an array containing the bottom view of the given tree.

Expected Time Complexity: O(N*logN).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105
"""


class TreeNode:
    def __init__(self, value  =0, left = None, right = None) :
        self.value = value
        self.left = left
        self.right = right
def bottom_view(root):
    res = []
    map = {}
    col = 0
    queue   = [[root,col]]

    while queue:
        node = queue.pop(0)
        value = node[0].value
        col = node[1]
        map[col]= value
        cur = node[0]

        if cur.left:
            queue.append([cur.left, col-1])
        if cur.right:
            queue.append([cur.right, col+1])

    key = []
    for i in map.keys():
        key.append(i)
    key.sort()

    for i in key:
        res.append(map[i])

    return res



def print_tree(node, level=0):
    if node :
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)     
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
