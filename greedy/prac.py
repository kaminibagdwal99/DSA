def maxSubArray(nums):
    total =0
    res=0
    for i in nums:
        total = total+i
        if total<0:
            total=0
        res= max(res, total)
    return res

def canJump(nums):
    goal=len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if nums[i]+ i>=goal:
            goal=i
    return True if goal==0 else False

def jump(nums):
    res=0
    l=r=0
    while r<len(nums)-1:
        fartest = 0
        for i in range(l, r+1):
            fartest= max(fartest, nums[i]+i)
        l= r+1
        r = fartest
        res = res+1
    return res
def canCompleteCircuit(gas, cost):
    if sum(cost)> sum(gas):
        return False
    total=0
    start=0
    for i in range(len(gas)):
        total += (gas[i]-cost[i])
        if total <0:
            total=0
            start+=1
    return start
def mergeTriplets(triplets, target):
    visit = set()
    for i in triplets:
        if i[0]> target[0] or i[1]> target[1] or i[2]>target[2]:
            continue
        for k,v in enumerate(i):
            if target[k]==v:
                visit.add(k)
    return True if len(visit)==3 else False
from collections import Counter
import heapq
def isNStraightHand(hand, groupSize):
    map=Counter(hand)
    max_heap = list(map.keys())
    heapq.heapify(max_heap)

    while max_heap:
        first = max_heap[0]
        for i in range(first, first+groupSize):
            if i not in map:
                return False
            map[i]= map[i]-1
            if map[i]==0:
                if i !=max_heap[0]:
                    return False
                heapq.heappop(max_heap)
    return True

print(isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))