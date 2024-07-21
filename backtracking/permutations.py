"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

class Solution:
    def permute(self, nums):
        res =[]

        def permutation_helper(index, ds):
            if index == len(nums):
                res.append(ds[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permutation_helper(index+1, ds)
                nums[index], nums[i] = nums[i], nums[index]
        permutation_helper(0, nums)
                

        return res
    
a = Solution()
print(a.permute( nums = [1,2,3]))