
class stack:
    def evalRPN(self,expression):
        stack =[]
        for i in expression:
            if i =="+":
                stack.append(stack.pop()+stack.pop())
            elif i =="-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)

            elif i =="*":
                stack.append(stack.pop() *stack.pop())
            elif i =="/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[-1]
a= stack()
print(a.evalRPN(["2","1","-","3","/"]))