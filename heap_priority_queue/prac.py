
import heapq
from collections import Counter
class Solution: 
    def findKthLargest(self,nums, k):
        nums = [-i for i in nums]
        heapq.heapify(nums)
        res = []

        while k>0:
            a = heapq.heappop(nums) * -1
            res.append(a)
            k = k-1
        return res[-1]
    
    def leastInterval(self,frequency, n):
        count = Counter(frequency)
        rs = [-i for i in count.values()]
        heapq.heapify(rs)

        time = 0
        q = []

        while q or rs:
            time +=1

            if rs:
                current_task = heapq.heappop(rs) +1
                if current_task:
                    q.append((current_task, time +n))

            if q and q[0][1]==time:
                heapq.heappush(rs,q.pop(0)[0])

        return time


a = Solution()
print(a.leastInterval(["A","A","A","B","B","B"], n = 2))
