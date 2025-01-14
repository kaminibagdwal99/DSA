
class Solution:
    def singleNumber(self, nums):
        res =0
        for i in nums:
            res = res^ i
        return res

a = Solution()
nums = [4,1,2,1,2]
print(a.singleNumber(nums))