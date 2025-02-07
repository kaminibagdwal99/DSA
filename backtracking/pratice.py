class Solution:
    def permute(self,nums):
        res = []
        
        def helper(idx,ds):
            if idx==len(nums):
                res.append(ds.copy())
                return
            for i in range(idx,len(nums)):
                nums[i], nums[idx]=nums[idx],nums[i]
                helper(idx+1,ds)
                nums[i], nums[idx]=nums[idx],nums[i]




            
        helper(0,nums)
        return res

a = Solution()
print(a.permute( nums = [1,2,3]))
