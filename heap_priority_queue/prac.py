import heapq
class KthLargest:
    def __init__(self, l, arr):
        self.capacity = l
        self.minheap = arr
        heapq.heapify(self.minheap)
        while len(self.minheap)>self.capacity:
            heapq.heappop(self.minheap)
    def add(self, val):
        heapq.heappush(self.minheap, val)
        if len(self.minheap)>self.capacity:
            heapq.heappop(self.minheap)
        return self.minheap[0]

def lastStoneWeight(stones):
    stones = [-i for i in stones]
    heapq.heapify(stones)
    while len(stones)>1:
        a=heapq.heappop(stones)
        b = heapq.heappop(stones)
        if b>a:
            heapq.heappush(stones, b-a)
    return stones[-1]

def kClosest(points, k):
    res=[]
    for i in points:
        distance = i[0]**2 + i[1]**2
        res.append([distance,i])
    heapq.heapify(res)
    final=[]

    while k>0:
        p,s = heapq.heappop(res)
        final.append(s)
        k=k-1
    return final
def findKthLargest(nums, k):
    nums=[-i for i in nums]
    heapq.heapify(nums)
    res=[]
    while k>0:
        a=heapq.heappop(nums)*-1
        res.append(a)
        k=k-1
    return res[-1]
from collections import Counter
def leastInterval(task, n):
    count = Counter(task)
    min_heap = [-i for i in count.values()]
    heapq.heapify(min_heap)
    q=[]
    time=0
    while q or min_heap:
        time=time+1
        if min_heap:
            current_task = heapq.heappop(min_heap)+1
            if current_task:
                q.append([current_task, time+n])
        if q and q[0][1]==time:
            heapq.heappush(min_heap, q.pop(0)[0])
    return time
    
print(leastInterval(["A","A","A","B","B","B"], n = 2))
