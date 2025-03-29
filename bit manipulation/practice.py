class Solution:
    def singleNumber(self, nums):
        res=0
        for i in nums:
            res = res ^i
        return res
    
    def hammingWeight(self, i):
        res =0
        while i:
            res = res + i%2
            i= i>>1
        return res
    
    def countBits(self,n):
        offset =1
        a=[0] *( n+1)

        for i in range(1,n+1):
            if 2*offset==i:
                offset=i
            
            a[i] = 1+a[i-offset]
        return a
    
    def missingNumber(self,nums):
        maxno= max(nums)
        set = [i for i in range(maxno+1)]
        total =0

        for i in set :
            total =total ^i

        for i in nums:
            total = total^i
        return total  
    
    def getSum(self, a,b):
        while b!=0:
            temp = a^b
            b = (a&b)>>1
            a=temp
        return a
    
    def reverse(self, x):
        res=0
        sign = -1 if x<0 else 1
        x=abs(x)
        while x:
            res = res *10 + x%10
            x=x//10
        return sign *res
    
    
a = Solution()
x = -123
print(a.reverse(x))