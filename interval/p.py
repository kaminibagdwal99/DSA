def can_attend_meetings(intervals):
    intervals.sort()
    
    end = intervals[0][1]
    res =0

    for i in intervals[1:]:
        if i[0]>=end:
            end = i[1]
        else:
            res +=1
            end = max( end, i[1])
        
    
    return res

    

intervals =[[1,2],[2,3],[3,4],[1,3]]
print(can_attend_meetings(intervals))