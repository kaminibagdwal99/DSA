class Solution:
    def min_meeting_rooms(self,intervals):
        start = sorted([i[0] for i in intervals ])
        end = sorted([i[1] for i in intervals ])
        count = 0
        res =0
        s,e = 0,0
        while s < len(intervals):
            if start[s]<end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res  = max(count, res)
        return res

a = Solution()
intervals = [(0,30),(5,10),(15,20),(21,25)]
print(a.min_meeting_rooms(intervals))