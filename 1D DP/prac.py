

def countSubstrings(s):
    res=0
    for i in range(len(s)):
        res += panlindrome(s, i, i) + panlindrome(s,i,i+1)
    return res
def panlindrome(s,l,r):
    res =0
    while l>=0 and r<len(s) and s[l]==s[r]:
        res= res+1
        l=l-1
        r=r+1
    return res

def longestPalindrome(s):
    res=""
    resLen = 0
    for i in range(len(s)):
        l,r =i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1 >resLen:
                res=s[l:r+1]
                resLen=r-l+1
            l=l-1
            r=r+1
        l,r =i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1 >resLen:
                res=s[l:r+1]
                resLen=r-l+1
            l=l-1
            r=r+1
    return res

def rob(nums):
    rob1, rob2 =0,0
    for i in nums:
        temp = max(i+rob1,rob2)
        rob1=rob2
        rob2 = temp
    return rob2
def rob1(nums):
    return max(nums[0] , rob(nums[1:]), rob(nums[:-1]))


def climbStairs(n):
    one, two=1,1
    for  i in range(n-1):
        one, two = one+two, one
    return one


def minCostClimbingStairs(cost):
    cost.append(0)
    for i in range(len(cost)-3, -1, -1):
        cost[i] = min(cost[i]+cost[i+1], cost[i]+ cost[i+2])
    return min(cost[0], cost[1])
cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))