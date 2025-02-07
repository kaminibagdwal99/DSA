class Solution:
    def min_meeting_rooms(self,intervals):
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        s,e = 0,0
        count, res = 0,0

        while s < len(intervals):
            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            res = max(res, count)
        return res
a = Solution()
intervals = [(0,30),(5,10),(15,20),(21,25)]
print(a.min_meeting_rooms(intervals))