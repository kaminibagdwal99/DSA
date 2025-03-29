class Solution:
    def isPalindrome(self, s):
        l,r = 0, len(s)-1
        while l<r:
            while l<r and not self.is_alnum(s[l]):
                l+=1
            while l<r and not self.is_alnum(s[r]):
                r-=1

            if s[l].lower() !=s[r].lower():
                return False
            l=l+1
            r=r-1
        return True
    def is_alnum(self, c):
        return (
            ord("A")<=ord(c)<=ord("Z") or 
            ord("a")<=ord(c)<=ord("z") or
            ord("0")<=ord(c)<=ord("9")
        )
    def twoSum(self, num,target):
        left, right = 0, len(num)-1
        while left<right:
            if num[left]+ num[right]>target:
                right=right-1
            elif num[left] + num[right]<target:
                left=left+1
            else:
                return [left+1,right+1]
            
    def three_Sum(self, nums):
        nums.sort()
        res=[]

        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            l, r = i+1, len(nums)-1

            while l<r:
                thresum= a+ nums[l]+nums[r]
                if thresum>0:
                    r=r-1
                elif thresum<0:
                    l=l+1
                else:
                    res.append([a,nums[l], nums[r]])
                    l=l+1
                    # while nums[l]==nums[l-1] and l<r:
                    #     l+=1
        return res
    
    def maxArea(self, height):
        l,r=0,len(height)-1
        res=0
        while l<r:
            area= (r-l)*min(height[l], height[r])
            res=max(res, area)
            if height[l]<=height[r]:
                l=l+1
            else:
                r=r-1
        return res

                    

s = "A man, a plan, a canal: Panama"
a = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(a.maxArea(height))