"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums ) -> int:
        value = Counter(nums)
        max_value =0
        key =0
        for i,v in value.items():
            max_value= max(i,max_value)
            key = i
        return key
        


a = Solution()
nums = [3,3,4]
print(a.majorityElement(nums))