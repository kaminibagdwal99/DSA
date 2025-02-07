
class Solution:
    def maxSubArray(self,nums):
        sum =0
        total = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum<0:
                sum = 0
            total = max(total, sum)
        return total
    
    def canJump(self, nums):
        goal = len(nums)-1
        for i in range(len(nums)-1, -1,-1):
            if i + nums[i]>= goal:
                goal = i
        return True if goal == 0 else False
    
    def jump(self, nums):
        res = 0
        l=r=0

        while r < len(nums)-1:
            fartest = 0
            for i in range(l, r+1):
                fartest = max(fartest, i + nums[i])

            l = r+1
            r = fartest
            res +=1
        return res
    
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)< sum(cost):
            return -1
        total = 0 
        start =0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])

            if total<0:
                total = 0
                start = i+1

        return start
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize !=0:
            return False


a = Solution()
print(a.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))