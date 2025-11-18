def isPalindrome(s):
    l,r=0, len(s)-1
    while l<r:
        while l<r and not s[l].isalnum():
            l=l+1
        while l<r and not s[r].isalnum():
            r=r-1
        if s[l].lower()!=s[r].lower():
            return False
        l=l+1
        r=r-1
    return True

def twoSum(numbers,target):
    l,r = 0, len(numbers)-1

    while l<r:
        if numbers[l]+numbers[r]<target:
            l=l+1
        elif numbers[l]+numbers[r]>target:
            r=r-1
        else:
            return [l+1, r+1]
        

def three_Sum(nums):
    res=[]
    nums.sort()
    for i,a in enumerate(nums):
        if i>0 and nums[i-1]==a:
            continue
        l,r=i+1, len(nums)-1
        while l<r:
            sum = a+ nums[l] + nums[r]
            if sum >0:
                r=r-1
            elif sum<0:
                l=l+1
            else:
                res.append([a, nums[l], nums[r]])
                l=l+1
                r=r-1
    return res

def maxArea(height):
    l,r = 0, len(height)-1
    res=0
    while l<r:
        area=(r-l)* min(height[l], height[r])
        res= max(res, area)
        if height[l]<=height[r]:
            l=l+1
        else:
            r=r-1
    return res
def trap(height):
    l,r = 0, len(height)-1
    maxleft, maxright = height[l], height[r]
    res=0
    while l<r:
        if maxleft<maxright:
            l=l+1
            maxleft = max(maxleft, height[l])
            res= res+ maxleft-height[l]
        else:
            r=r-1
            maxright = max(maxright, height[r])
            res= res+ maxright-height[r]
    return res
print(trap([0,2,0,3,1,0,1,3,2,1]))
