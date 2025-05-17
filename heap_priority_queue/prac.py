import heapq
def findKthLargest(nums,k):
    nums = [-i for i in nums]
    heapq.heapify(nums)
    res=[]
    while k >0:
        a = heapq.heappop(nums) * -1
        res.append(a)
        k=k-1
    return res[-1]

from collections import Counter
def leastInterval(list, n):
    count = Counter(list)
    maxheap = [-i for i in count.values()]
    heapq.heapify(maxheap)

    time = 0
    queue =[]

    while queue or maxheap:
        time +=1
        if maxheap:
            current_task = heapq.heappop(maxheap) +1
            if current_task:
                queue.append([current_task, time+n])

        if queue and queue[0][1]==time:
            heapq.heappush(maxheap, queue.pop(0)[0])

    return time

print(leastInterval(["A","A","A","B","B","B"], n = 2))
