"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root) :
        res =[]
        queue = deque([root])

        while queue:
            rightSide = None
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:

                res.append(rightSide.val)

        return res


def print_tree(node, level=0):
    if node :
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.left, level + 1)

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(5)
a.right.right = TreeNode(4)
a.right.right.right = TreeNode(6)


print_tree(a)
z = Solution()
print(z.rightSideView(a))