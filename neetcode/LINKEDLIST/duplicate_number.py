def duplicate(nums):
    slow ,fast =0,0
    while True:
        slow  = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow1=0
    while True:
        slow = nums[slow]
        slow1 = nums[slow1]
        if slow == slow1:
            return slow

a= duplicate([1,2,3,2,4])
print(a)