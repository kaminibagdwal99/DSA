import heapq
class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand)% groupSize !=0:
            return False
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)
        minheap = list(count.keys())
        heapq.heapify(minheap)
        while minheap:
            first = minheap[0]
            for i in range(first, first +groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True


        
a = Solution()
print(a.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))