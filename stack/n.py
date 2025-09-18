

def valid_parenthesis(expression):
    open = {"{", "(", "["}
    close = {")", "}", "]"}
    stack=[]
    for i in expression:

        if i in open:
            stack.append(i)
        elif i in close:
            if not stack:
                return False
            top_char = stack.pop()
            if not balance(top_char, i):
                return False
    return True if not stack else False

def balance(open,close):
    bracket ={"{":"}", "(":")", "[":"]"}
    return bracket[open]==close

class MinStack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def minnum(Self):
        return Self.minstack[-1]
    def top(self):
        return self.stack[-1]

def evalRPN(expression):
    stack=[]
    for i in expression:
        if i=="+":
            stack.append(stack.pop()+ stack.pop())
        elif i =="-":
            a= stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i=="*":
            stack.append(stack.pop()* stack.pop())
        elif i =="/":
            a= stack.pop()
            b = stack.pop()
            stack.append(b/a)
        else:
            stack.append(int(i))
    return stack[-1]


def generateParenthesis(n):
    stack=[]
    res =[]
    def dfs(open, close):
        if open==close==n:
            res.append("".join(stack))
            return 
        if open<n:
            stack.append("(")
            dfs(open+1, close)
            stack.pop()
        if open>close:
            stack.append(")")
            dfs(open, close+1)
            stack.pop()
    dfs(0,0)
    return res


def dailyTemperatures(temperature):
    res =[0]* len(temperature)
    stack=[]
    for i in range(1, len(temperature)):
        while stack and temperature[i]>temperature[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index]=i-prev_index
        stack.append(i)
    return res


def carFleet(target, position, speed):
    pair = [(p,s) for (p,s) in zip(position, speed)]
    stack=[]
    for p,s in sorted(pair)[::-1]:
        stack.append((target-p)/s)
        if len(stack)>=2 and stack[-1]<stack[-2]:
            stack.pop()
    return len(stack)
print(carFleet( target = 100, position = [0,1,4], speed = [4,2,1]))