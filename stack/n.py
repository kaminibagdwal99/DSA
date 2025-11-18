def valid_parenthesis(expression):
    
    opened = {'(', '{', '['}
    closed = {')', '}', ']'}
    stack = []

    for i in expression:
        if i in opened:
            stack.append(i)
        elif i in closed:
            if not stack:return False
            top_char = stack.pop()
            if not balance(top_char, i):
                return False

    return True if not stack else False

    
def balance(open, closed):
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    return bracket_pairs[closed]==open 
expression = "{(a+b)+(c+d)}"
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def minnum(self):
        return self.min_stack[-1]
    
    def top(self):
        return self.stack[-1]

def evalRPN(expression):
    stack=[]
    for i in expression:
        if i =="+":
            stack.append(stack.pop()+ stack.pop())
        elif i =="-":
            a= stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i =="*":
            stack.append(stack.pop()* stack.pop())
        elif i =="/":
            a= stack.pop()
            b = stack.pop()
            stack.append(b/a)
        else:
            stack.append(int(i))
    return stack[-1]

def carFleet(target, position, speed):
    pair = [(p,s) for (p,s) in zip(position, speed)]
    stack=[]
    for p,s in sorted(pair)[::-1]:
        stack.append((target-p)/s)
        if len(stack)>=2 and stack[-1] <=stack[-2]:
            stack.pop()
    return len(stack)
def dailyTemperatures(temp):
    res=[0]* len(temp)
    stack=[]
    for i in range(len(temp)):
        while stack and temp[i]>=temp[stack[-1]]:
            index= stack.pop()
            res[index]= i-index
        stack.append(i)
    return res
def min_elemen(arr):
    res=[-1]*(len(arr))
    stack=[]
    for i in range(len(arr)-1, -1, -1):
        while stack and arr[i] <=arr[stack[-1]]:
            index = stack.pop()
            res[index]=arr[i]
        stack.append(i)
    return res
def next_greater_element(arr):
    res=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i] >=arr[stack[-1]]:
            index = stack.pop()
            res[index]=arr[i]
        stack.append(i)
    return res

print(next_greater_element([4,5,2,10,8]))