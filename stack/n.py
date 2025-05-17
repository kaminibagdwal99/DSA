class Solution:
    def carFleet(self, target, position,speed):
        pair= [[p,s] for p,s in zip(position,speed)]
        stack=[]

        for i , v in sorted(pair)[::-1]:
            stack.append((target-i)/v)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

no_of_flleet = Solution()
print(no_of_flleet.carFleet( target = 100, position = [0,1,4], speed = [4,2,1]))