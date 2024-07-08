import math
def minEatingSpeed(piles, h):
    l, r = 0, max(piles)
    res = r

    while l<=r:
        k = (l+r)//2
        time = 0
        
        for i in piles:
            time = time + math.ceil(i/k)

        if time <=h:
            res = min(res, k)
            r = k-1
        else:
            l=k+1

    return res

piles = [3,6,7,11]; h = 8
print(minEatingSpeed(piles,h))