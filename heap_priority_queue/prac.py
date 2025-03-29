import heapq
from collections import Counter
class Solution:
    def lastStoneWeight(self, stones):
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            
            if b >a:
                heapq.heappush(stones, b-a)

            
            return stones[-1]
    def kClosest(self, points, k):
        res = []
        for i in points:
            d = i[0] **2 + i[1]**2
            res.append([d,i])
        final =[]
        heapq.heapify(res)

        while  k>0:
            d,v = heapq.heappop(res)
            final.append(v)
            k=k-1
        return final
    
    def findKthLargest(self, nums, k):
        nums = [-i for i in nums]
        heapq.heapify(nums)
        res =[]

        while k>0:
            a = heapq.heappop(nums) *-1
            res.append(a)
            k=k-1
        return res[-1]
    
    def leastInterval(self, l, n):
        v = Counter(l)
        maxheap = [-i for i in v.values()]
        heapq.heapify(maxheap)
        queue, time = [],0

        while queue  or maxheap:
            time +=1
            if maxheap:
                current_task = heapq.heappop(maxheap) +1
                if current_task:
                    queue.append([current_task,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(maxheap,queue.pop(0)[0])
        return time


        
a = Solution()
print(a.leastInterval(["A","A","A","B","B","B"], n = 2))
