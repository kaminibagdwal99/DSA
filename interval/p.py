class Solution:
    def insert(self, intervals, newInterval):
        res =[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1] )]
        res.append(newInterval)
        return res
    def merge(self, intervals):
        start = intervals[0][0]
        end = intervals[0][1]
        res=[]

        for i in intervals[1:]:
            if i[0]<end:
                end = max(end, i[1])
            else:
                res.append([start, end])
                start= i[0]
                end=i[1]
        res.append([start, end])
        return res
    
    def eraseOverlapIntervals(self, intervals):
        res=0
        intervals.sort()
        end = intervals[0][1]
        for i in intervals[1:]:
            if i[0]<end:
                res+=1
                end = min(end, i[1])
            else:
                end = i[1]
        return res
    
    def can_attend_meetings(self, intervals):
        intervals.sort()
        for i in range(1,len(intervals)):
            return intervals[i][0]>intervals[i-1][1]
        
    def min_meeting_rooms(self, intervals):
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        count, res = 0,0
        s,e=0,0

        while s <len(intervals):
            if start[s]<end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res= max(res, count)
        return res
a = Solution()


intervals = [(0,30),(5,10),(15,20),(21,25)]
print(a.min_meeting_rooms(intervals))