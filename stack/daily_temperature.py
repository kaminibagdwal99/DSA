"""
Given an array of integers temperatures represents the daily temperatures, return an 
array answer such that answer[i] is the number of days you have to wait after the ith 
day to get a warmer temperature. If there is no future day for which this is possible,
 keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index]= i-prev_index

            stack.append(i)
        return res


a = Solution()
print(a.dailyTemperatures([73,74,75,71,69,72,76,73]))
