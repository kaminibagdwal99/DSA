class Solution:
    def singleNumber(self,nums):
        res=0
        for i in nums:
            res= res^i
        return res
    
    def hammingWeight(self, n):
        res=0
        while n:
            res = res + n%2
            n = n>>1
        return res
    
    def countBits(s, n):
        res=[0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 ==i:
                offset = i
            res[i]= 1 + res[i-offset]
        return res
    
    def missingNumber(self, nums):
        m = max(nums)
        set = [i for i in range(m+1)]
        total = 0
        for  i in set:
            total = total ^ i
        for i in nums:
            total = total ^ i
        return total
    
    def getSum(self, a,b):
        while b:
            temp = a^b
            b = (a&b)<<1
            a=temp
        return a
    
    def reverse(self, x):
        sign = -1 if x<0 else 1
        x = abs(x)
        res=0
        while x:
            res = res * 10 + x%10
            x= x//10
        return res* sign



a = Solution()
x = -123
print(a.reverse(x))