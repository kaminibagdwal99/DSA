class Solution:
    def maxSubArray(self, nums):
        total =0
        sum =0
        for i in nums:
            total = total+i

            if total <0:
                total =0
            sum = max(total, sum)
        return sum
    
    def canJump(self, nums):
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i]>=goal:
                goal = i
        return True if goal ==0 else False 
    
    def jump(self, nums):
        l=r=0
        res =0
        while r < len(nums)-1:
            fartest  =0
            for i in range(l, r+1):
                fartest = max( fartest, i+nums[i])
            l = r+1
            r=fartest
            res+=1
        return res
        
nums = [2,3,1,1,4]
a = Solution()
print(a.jump(nums))