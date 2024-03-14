from collections import deque

class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.left = left
        self.right= right

def levelorder(root):
    if not root:
        return []

    queue = deque([root])
    result= []

    while queue:
        levelsize = len(queue)
        levelnode = []

        for _ in range(levelsize):
            node = queue.popleft()
            levelnode.append(node.val)


            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(levelnode)

    return result




            


node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(7)
node.right.left =TreeNode(6)


print(levelorder(node))