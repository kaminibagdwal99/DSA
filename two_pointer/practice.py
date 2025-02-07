
class Solutions:
    def maxArea(self, nums):
        res =0
        l,r = 0, len(nums)-1
        while l<=r:
            area = (r-l)* min(nums[l], nums[r])
            res = max(area,res)
            if nums[l]<=nums[r]:
                l+=1
            else:
                r-=1
        return res
a = Solutions()
nums = [1,8,6,2,5,4,8,3,7]
print(a.maxArea(nums))