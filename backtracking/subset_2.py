"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,/.2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10"""

class Solution:
    def subsetsWithDup(self, nums) :
        res = []
        nums.sort()
        def subset_helper(ind, ds):
            res.append(ds)
            for i in range(ind, len( nums)):
                if i > ind and nums[i]==nums[i-1]: continue
                subset_helper(i+1, ds+[nums[i]])
        subset_helper(0,[])
        return res

a = Solution()
print(a.subsetsWithDup(nums = [1,2,2]))
        