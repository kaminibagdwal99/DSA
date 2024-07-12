"""
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree and are at same position then consider the left ones only(i.e. leftmost). 
For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3
Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
Your Task:
Since this is a function problem. You don't have to take input. Just complete the function topView() that takes root node as parameter and returns a list of nodes visible from the top view from left to right.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 105
1 ≤ Node Data ≤ 105
"""


class TreeNode:
    def __init__(self, value =0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def top_view(root):
    col =0
    map ={}
    res  =[]
    queue = [[root,col]]

    while queue:
        node = queue.pop(0)
        col = node[1]
        value = node[0].value
        cur = node[0]

        if col not in map:
            map[col]=value

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

        

        


a = TreeNode(10)
a.left = TreeNode(20)
a.right = TreeNode(30)
a.left.left=TreeNode(40)
a.left.right=TreeNode(60)
a.right.left = TreeNode(90)
a.right.right = TreeNode(100)

def print_tree(node, level=0):
    if node :
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)


print_tree( a)

print(top_view(a))
