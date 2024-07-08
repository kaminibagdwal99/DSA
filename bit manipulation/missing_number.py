"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in 
the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
# tc : o(n) sc : o(n)
class Solution:
    def missingNumber(self, nums) -> int:
        len = max(nums)
        set = [i for i in range(len+1)]

        for i in nums:
            if i  in set:
                set.remove(i)
        return set[0]
                

a = Solution()
print(a.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))



# tc: o(n)sc: o(1)
class Solutions:
    def missingNumber(self, nums) -> int:
        n = len(nums)

        sum = (n * (n+1))//2
        
        total =0

        for i in nums:
            total +=i

        return sum-total

a = Solutions()
print(a.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))


class Solutionss:
    def missingNumber(self, nums) -> int:
        len = max(nums)
        set = [i for i in range(len+1)]
        
        total =0

        

    
        for i in set:
            
            total = total ^i
           
        for i in nums:
            total = total ^ i

        

        return total

a = Solutionss()
print(a.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))