def insert(intervals,newInterval):
    res=[]
    for i in range(len(intervals)):
        if newInterval[1]<intervals[i][0]:
            res.append(newInterval)
            return res+ intervals[i:]
        elif newInterval[0]> intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(intervals[i][1], newInterval[1])]
    res.append(newInterval)
    return res
def merge(intervals):
    intervals.sort(key = lambda x:x[0])
    start =intervals[0][0]
    end = intervals[0][1]
    res=[]
    for i in intervals[1:]:
        if i[0]<end:
            end = i[1]
        else:
            res.append([start, end])
            start=i[0]
            end=i[1]
    res.append([start, end])
    return res
def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x:x[0])
    end=intervals[0][1]
    res=0

    for i in intervals[1:]:
        if i[0]<end:
            res= res+1
        else:
            end = min(end, i[1])
    return res

def can_attend_meetings(intervals):
    intervals.sort(key = lambda x:x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0]<intervals[i-1][1]:
            return False
    return True
def min_meeting_rooms(intervals):
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)
    s=e=count=total=0
    while s<len(start):
        if start[s]<end[e]:
            s=s+1
            count +=1
        else:
            e=e+1
            count = count-1
        total = max(total, count)
    return total

intervals = [(0,30),(5,10),(15,20),(21,25)]
print(min_meeting_rooms(intervals))