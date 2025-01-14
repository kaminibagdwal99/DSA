class Solution:
    def subsets(self, num):
        res = []
        cur = []
        def dfs(i):
            # base case
            if i >= len(num):
                res.append(cur.copy())
                return
            # desicion to include num[i]
            cur.append(num[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return res
            
            



a = Solution()
nums = [1,2,3]
print(a.subsets(nums))