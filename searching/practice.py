
import math
class Solution:
    def findMin(self,nums):
        l,r = 0,len(nums)-1
        res = nums[0]
        
        while l<=r:
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break

            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r = mid-1
        return res


a = Solution()
nums = [4,5,6,7,8,1,2]
print(a.findMin(nums))