"""
Description
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required

    tc: nlog(n) sc: o(n)
    """

    def min_meeting_rooms(self, intervals) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        s, e = 0,0
        count , res = 0,0

        while s< len(intervals):
            if start[s]<end[e]:
                s+=1
                count +=1
            else:
                e+=1
                count -=1
            res = max(count, res)
        return res

a = Solution()
intervals = [(0,30),(5,10),(15,20),(21,25)]
print(a.min_meeting_rooms(intervals))