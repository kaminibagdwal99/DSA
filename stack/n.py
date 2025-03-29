class stack:
    def evalRPN(self, expression):
        stack =[]
        for i in expression:
            if i =="+":
                stack.append(stack.pop()+stack.pop())
            elif i == "-":
                a=stack.pop()
                b= stack.pop()
                stack.append(b-a) 
            elif i =="*":
                stack.append(stack.pop()*stack.pop())
            elif i == "-":
                a=stack.pop()
                b= stack.pop()
                stack.append(b/a) 
            else:
                stack.append(int(i))
        return stack[-1]
    
    def generateParenthesis(self, n):
        stack=[]
        res=[]
        def backtrack(open, close):
            if open==close==n:
                res.append(("".join(stack)))
                return
            
            if open<n:
                stack.append("(")
                backtrack(open+1,close)
                stack.pop()
            if open>close:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
        backtrack(0,0)
        return res
    
    def dailyTemperatures(self, temp):
        stack = []
        res=[0] * len(temp)

        for i in range(len(temp)):
            while stack and temp[i]>temp[stack[-1]]:
                prev_index =stack.pop()
                res[prev_index]=i-prev_index
            stack.append(i)
        return res
    def carFleet(self,target,position,speed):
        pair = [[p,s] for p,s in zip(position,speed)]
        print(pair)
        stack=[]

        for i,v in sorted(pair)[::-1]:
            stack.append((target-i)/v)
            while len(stack)>=2 and stack[-1]<stack[-2]:
                stack.pop()
        return len(stack)

a= stack()
print(a.carFleet( target = 100, position = [0,1,4], speed = [4,2,1]))