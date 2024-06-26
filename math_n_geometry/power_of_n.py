"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
"""

# tc: log(n)
class Solution:
    def myPow(self, x, n) :
        number = abs(n)
        total  = 1
        if n ==0:
            return 1
        while number>1:
            if number%2==0:
                x = x*x
                number = number //2
            else:
                total = total *x
                number = number -1
        
        return total *x if n>0 else 1/total*x





a = Solution()
x = 2.00000; n = 10
print(a.myPow(x,n))


class Solutions:
    def myPow(self, x, n) :
        def helper(x,n):
            if x ==0: return 0
            if n ==0: return 1

            res = helper(x,n//2)
            res = res*res
            return x*res if n%2 else res
        res = helper(x, abs(n))
        return res if n>0 else  1/res




a = Solutions()
x = 2.00000; n = 10
print(a.myPow(x,n))