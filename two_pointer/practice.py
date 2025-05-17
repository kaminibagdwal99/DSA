class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s)-1

        while l<r:
            while l<r and not self.isalnum(s[l]):
                l+=1
            while l<r and not self.isalnum(s[r]):
                r= r-1
            if s[l].lower() != s[r].lower():
                return False
            l= l+1
            r=r-1
        return True
    
    def isalnum(self, s):
        return ord("a")<=ord(s)<=ord("z") or ord("A")<=ord(s)<=ord("Z") or ord("0")<=ord(s)<=ord("9")
    
    def twoSum(self, numbers, target):
        l=0
        r = len(numbers)-1
        while l<r:
            if numbers[l]+ numbers[r]>target:
                r= r-1
            elif numbers[l]+ numbers[r] < target:
                l = l+1
            else:
                return [l+1, r+1]
            
    def three_Sum(self, nums):
        nums.sort()
        res=[]

        for i , a in enumerate(nums):
            if i >0 and nums[i-1]==a:continue
            l,r = i+1, len(nums)-1
            while l<r:
                thre = a+ nums[l]+ nums[r]
                if thre >0:
                    r= r-1
                elif thre <0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l = l+1
        return res
    
    def maxArea(self, height):
        l, r= 0, len(height)-1
        res=0
        while l<r:
            area = (r-l) * min(height[l], height[r])
            res= max(area, res)
            if height[l]<= height[r]:
                l+=1
            else:
                r= r-1
        return res
a= Solution()      
height = [1,8,6,2,5,4,8,3,7]
print(a.maxArea(height))
