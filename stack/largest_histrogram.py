"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

class Solution:
    def largestRectangleArea(self, heights):
        maxarea=0
        stack =[] #pair(index, height)

        for i ,v in enumerate(heights):
            start =i
            while stack and stack[-1][1]>v:
                    index, height = stack.pop()
                    maxarea= max(maxarea, height *(i-index))
                    start = index

            stack.append((start, v))

        for i , h in stack:
             maxarea= max(maxarea, h*(len(heights)-i))
        return maxarea
    


a = Solution()
print(a.largestRectangleArea( heights = [2,1,5,6,2,3,2,3,4,1]))