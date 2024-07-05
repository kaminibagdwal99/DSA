class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def balanced(self):
        def dfs(self):
            if not self: return[ True, 0]

            left,right = dfs(self.left), dfs(self.right)

            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <=1) 
            return [balanced, 1+max(left[1], right[1])]
        return dfs(self)[0]


node = TreeNode(1)
node.right = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(7)
node.right.right.left =TreeNode(6)

v =node.balanced()
print(v)
