def binary_Search(aar, target):
    l, r =0, len(aar)-1
    while l<=r:
        mid = (l+r)//2
        if target>arr[mid]:
            l=mid+1
        elif target<arr[mid]:
            r=mid-1
        else:
            return True
    return False


def search_in_2d(arr, target):
    row, col = len(arr), len(arr[0])
    t,b = 0, row-1

    while t<=b:
        row =(t+b)//2
        if target>arr[row][-1]:
            t=row+1
        elif target<arr[row][0]:
            b= row-1
        else:
            break
    row =(t+b)//2
    l,r = 0, col-1

    while l<=r:
        mid = (l+r)//2
        if target>arr[row][mid]:
            l= mid+1
        elif target<arr[row][mid]:
            r= mid-1
        else:
            return True
    return False
import math
def minEatingSpeed(piles, h):
    l, r = 0 , max(piles)
    res=r
    while  l<=r:
        k=(l+r)//2
        time=0
        for i in piles:
            time = time + math.ceil(i/k)
        if time<=h:
            r=k-1
            res= min(res, k)
        else:
            l=k+1
    return res


def findMin(nums):
    l,r = 0,len(nums)-1
    res=nums[0]
    while l<=r:
        if nums[l]<nums[r]:
            res= min(nums[l], res)
            break
        mid= (l+r)//2
        res = min(res, nums[mid])
        if nums[l]<=nums[mid]:
            l=mid+1
        else:
            r=mid-1
    return res

def search(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        
        if nums[l]<=nums[mid]:
            # leftsorted
            if target>nums[mid] or target< nums[l]:
                l= mid+1
            else:
                r=mid-1
            
        else:
            # rightsorted
            if target>nums[mid] or target< nums[l]:
                l=mid+1
            else:
                r=mid-1
    return -1

class TimeMap:
    def __init__(self):
        self.store ={}

    def set(self, key, val, time):
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([val, time])

    def get(self, key, time):
        val = self.store.get(key, [])
        l,r = 0, len(val)-1
        res=""
        while l<=r:
            mid = (l+r)//2
            if val[mid][1]<=time:
                res = val[mid][0]
                l=mid+1
            else:
                r=mid-1
        return res



a = TimeMap()
a.set("foo", "bar", 1)
print(a.get("foo", 1))
      
print(a.get("foo", 3))
a.set("foo", "bar2", 4)
print(a.get("foo", 4))
print(a.get("foo", 5))