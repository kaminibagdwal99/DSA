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


a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)

v =a.balanced()
print(v)
