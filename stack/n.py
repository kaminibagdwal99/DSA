class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top ==None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack underflow"
        else:
            pop_value = self.top.value
            self.top = self.top.next
            return pop_value

    def transverse(self):
        cur = self.top
        while cur:
            print(cur.value,'=>', end = "")
            cur=cur.next
        print("None")

    def peak(self):
        if self.is_empty():
            return "Stack underflow"
        return self.top.value
    
    def size(self):
        count = 0
        temp = self.top
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    


def text_editor(str,pattern):
    s = Stack()
    v = Stack()

    for i in str:
        s.push(i)

    for i in pattern:
        if i == "u":
            value = s.pop()
            v.push(value)
        else:
            value = v.pop()
            s.push(value)
    result =""

    while not s.is_empty():
        result =s.pop()+result

    return result


def find_celebrity(l):
    s = Stack()
    for i in range(len(l)):
        s.push(i)

    while s.size()>=2:
        i=s.pop()
        j=s.pop()

        if l[i][j]==0:
            s.push(i)
        else:
            s.push(j)

    celeb = s.pop()

    for i in range(len(l)):
        if i !=celeb:
            if l[i][celeb]==0 or l[celeb][i]==1:
                return "no one is celeb"
            
    return celeb
    








s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.transverse()
print(s.peak())
s.pop()
s.transverse()
str = "hello"
pattern="uuuru" 
l =[
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

print(text_editor(str,pattern))
print(find_celebrity(l))


print("*"*50)
def balance(expression):
    open = {"{","(","{"}
    closed = {")","}","]"}
    stack =[]
    for i in expression:
        if i in open:
            stack.append(i)
        elif i in closed:
            if not stack:
                return False
            top = stack.pop()
            if not is_balanced(top,i):
                return False
            
    return True if not stack else  False
            
def is_balanced(open, closed):
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    return bracket_pairs[closed]==open



expression = "{(a+b)+(c+d)}"
print(balance(expression))

print("*"*50)

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,value):
        self.stack.append(value)
        val = min( value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(val)

    def pop(self):
        if not self.stack or self.minStack:
            "stack underflow"
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def getmin(self):
        return self.minStack[-1]
    


a = MinStack()
a.push(-2)
a.push(0)
a.push(-3)
print(a.getmin())
a.pop()
print(a.top())
print(a.getmin())


class stackeval:
    def evalRPN(self ,exp):
        stack =[]

        for i in exp:
            if i =="+":
                stack.append(stack.pop() + stack.pop())
            elif i =="-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i =="*":
                stack.append(stack.pop() * stack.pop())
            elif i =="/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))

                print(stack)


        return stack[0]




a= stackeval()
print(a.evalRPN(["2","1","+","3","*"]))

print("8"*50)
def daily_temp(l):
    res = [0]*len(l)
    stack =[]
    for i in range(len(l)):
        while stack and l[i]>l[-1]:
            index = stack.pop()
            res[index]= i-index


        stack.append(i)
    return res


print(daily_temp([73,74,75,71,69,72,76,73]))

def carFleet(target,position,speed):
    pair = [[position,speed] for position,speed in zip(position,speed) ]
    stack =[]
    for p,s in sorted(pair)[::-1]:
        stack.append((target-p)//s)
        if len(stack)>=2 and stack[-1<=stack[-2]]:
            stack.pop()

    return len(stack)
print(carFleet( target = 100, position = [0,2,4], speed = [4,2,1]))

def next_greater_element(list):
    res = [-1]*len(list)
    stack = []
    for i in range(len(list)-1,-1,-1):
        while stack and list[i]>=list[stack[-1]]:
            stack.pop()
        if stack:
            res[i]=list[stack[-1]]
        stack.append(i)
    return res
print(next_greater_element([4,5,2,10,8]))