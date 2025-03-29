"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

class Solution:
    def threeSum(self, nums) :
        nums = sorted(nums)
        l =set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        l.add((nums[i],nums[j],nums[k]))
        return [list(triplet) for triplet in l]

a = Solution()
nums = [-1,0,1,2,-1,-4]
# print(a.threeSum(nums))



class Solution:
    def three_Sum(self, nums) :
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                thressum = a + nums[l]+nums[r]
                if thressum>0:
                    r = r-1
                elif thressum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l = l+1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

b = Solution()
nums = [-1,1,2,-1,-4]
print(b.three_Sum(nums))