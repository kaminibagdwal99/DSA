class Solution:
    def productExceptSelf(self,nums):
        res =[1]* len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res
            
a = Solution()
nums = [-1,1,0,-3,3]
print(a.productExceptSelf(nums))