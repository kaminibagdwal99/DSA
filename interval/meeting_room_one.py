"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true

"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings( booloean)
    """
    def can_attend_meetings(self, intervals) :
        intervals.sort()
        
        for i in range( 1,len(intervals)):
            print(intervals[i])
            if intervals[i][0]<intervals[i-1][1]:
                return False
            
        return True

           
a = Solution()
intervals = [[0,30],[5,10],[15,20]]
print(a.can_attend_meetings(intervals))