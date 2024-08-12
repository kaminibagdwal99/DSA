
import math
def minEatingSpeed(piles, h):
    l , r = 0, max(piles)
    res = r
    while l<=r:
        k = (l +r)//2
        time = 0

        for i in piles:
            time = time + math.ceil(i/k)

        if time<=h:
            res = min(k, res)
            r = k-1
        else:
            l = k+1

    return res

piles = [30,11,23,4,20]; h = 6
print(minEatingSpeed(piles,h))