class Solution:
    def rob(self, nums):
        one,two =0,0
        for num in nums:
            one, two = two,max(num+one, two)
        return two

a = Solution()

nums = [2,7,9,3,1]
print(a.rob(nums))