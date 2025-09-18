


def singleNumber(nums):
    total = 0
    for i in nums:
        total = total^i
    return total


def hammingWeight(n):
    res=0
    while n:
        res= res+ n%2
        n= n//2
    return res

def countBits(n):
    res=[0] *(n+1)
    offset =1
    for i in range(1, n+1):
        if offset * 2 ==i:
            offset = i
        res[i] = 1+ res[i-offset]
    return res
def reverseBits(n):
    res=0
    for i in range(32):
        bit = (n>>i)&1
        res=res| bit<<(31-i)
    return res

def missingNumber(nums):
    set = [i for i in range(max(nums)+1)]
    total=0
    for i in set:
        total=total ^i
    for i in nums:
        total ^=i
    return total
def getSum(a, b):
    while b:
        temp = a^b
        b = (a&b)>>1
        a=temp
    return a

def reverse(x):
    sign = -1 if x<0 else 1
    x = abs(x)
    total=0
    while x>0:
        total = total * 10 + x%10
        x=x//10
    return sign * total

x = -123
print(reverse(x))