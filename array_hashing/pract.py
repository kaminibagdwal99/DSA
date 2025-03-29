class Solution:
    def productExceptSelf(self, nums):
        res =[1] * len(nums)
        pre =1
        for i in range(len(nums)):
            res[i] = pre
            pre =pre * nums[i] 
        print(res)
        post=1
        for i in range(len(nums)-1,-1,-1):
            res[i]= res[i]* post
            post = post*nums[i]
        return res
    
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest=0

        for i in numset:
            if (i-1) not in numset:
                length=1
                while (i+length) in numset:
                    length+=1
                longest=max(longest, length)
        return longest

a = Solution()

print(a.longestConsecutive(nums = [2,20,4,10,3,4,5]))