import math
class Solution:
    def minEatingSpeed(self, piles,h):
        left, right= 0, max(piles)
        res=right
        while left<=right:
            k = (left+right)//2
            print(k)
            total=0

            for i in piles:
                total = total + math.ceil(i/k)
                print("total is", total)
            print("total is ...", total)

            if total<=h:
                res= min(res, total)
                right = k-1
            else:
                print("left")
                left = k+1
            return res

a=Solution()
piles = [3,6,7,11];h = 8
print(a.minEatingSpeed(piles,h))