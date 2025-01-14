import math

class Solution:
    def minEatingSpeed(self, piles, h) :
        left,right = 0, max(piles)
        res = right

        while left <= right:
            k = (left+right)//2
            time = 0

            for i in piles:
                time = time + math.ceil(i/k)

            if time <=h:
                res = min(res, k)
                right = k-1
            else:
                left = k+1

        return res




a = Solution()

piles = [30,11,23,4,20]; h = 5
print(a.minEatingSpeed(piles,h))