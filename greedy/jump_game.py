"""
You are given an integer array nums. You are initially positioned at the array's first index,
 and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes
 it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
# tc : (n) sc : o(1)
class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums)-1
        print("goal", goal)
        
        for i in range(len(nums)-1, -1, -1):
            print("i",i)
            print(nums[i], "goal ", goal)
            
           
            if i+nums[i]>=goal:
               
                goal =i
                

        return True if goal ==0 else False

a = Solution()
nums = [2,1,1,0,4]
print(a.canJump(nums))