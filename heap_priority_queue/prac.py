
import heapq
class KthLargest:
    def __init__(self, capacity, list):
        self.capacity = capacity
        self.max_heap = list

        heapq.heapify(self.max_heap)
        while self.capacity<len(self.max_heap):
            heapq.heappop(self.max_heap)
    def add(self,val):
        heapq.heappush(self.max_heap, val)
        if self.capacity<len(self.max_heap):
            heapq.heappop(self.max_heap)
        return self.max_heap[0]

def lastStoneWeight(stones):
    stones =[-i for i in stones]
    heapq.heapify(stones)
    while len(stones)>1:
        a= heapq.heappop(stones)
        b= heapq.heappop(stones)
        if b>a:
            heapq.heappush(stones, b-a)
    return stones[0]

def kClosest(points, k):
    res=[]
    for i in points:
        distance = i[0]**2 + i[1]**2
        res.append([distance, i])
    heapq.heapify(res)
    final=[]

    while k:
        p,s = heapq.heappop(res)
        final.append(s)
        k=k-1
    return final 


def findKthLargest(nums, k):
    nums= [-i for i in nums]
    heapq.heapify(nums)
    res=[]

    while k:
        a= heapq.heappop(nums)*-1
        res.append(a)
        k=k-1
    return res[-1]
from collections import Counter
def leastInterval(task, n):
    q=[]
    count = Counter(task)
    max_heap = [-i for i in count.values()]
    heapq.heapify(max_heap)
    time=0

    while max_heap or q:
        time+=1
        if max_heap:
            current_task = heapq.heappop(max_heap)+1
            if current_task:
                q.append([current_task,time+n ])
        if q and q[0][1]==time:
            heapq.heappush(max_heap, q.pop(0)[0])
    return time


print(leastInterval(["A","A","A","B","B","B"], n = 2))
