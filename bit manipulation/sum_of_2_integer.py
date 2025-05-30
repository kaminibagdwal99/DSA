"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
"""

# tc: o(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b !=0:
            temp = a^b
            b = (a&b)<<1
            a = temp
        return a


a = Solution()
print(a.getSum(a = 1, b = 2))