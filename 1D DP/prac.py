def climbStairs(n):
    one, two = 1,1
    for i in range(n-1):
        one, two = one+two, one
    return one


def minCostClimbingStairs(cost):
    cost.append(0)
    for i in range(len(cost)-3,-1, -1):
        cost[i] = min(cost[i+1]+cost[i], cost[i+2]+cost[i])
    return min(cost[0], cost[i])

def rob(nums):
    pass
nums = [2,7,9,3,1]
print(rob(nums))