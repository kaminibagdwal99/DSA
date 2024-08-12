class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class Stack:
    def __init__(self) :
        self.top = None


    def is_empty(self):
        return self.top == None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        cur = self.top

        while cur:
            print(cur.value , '->', end = " ")
            cur = cur.next
        print("None")

    def peak(self):
        if self.is_empty():
            return "stack underflow"
        return self.top.value
    def pop(self):
        if self.is_empty():
            return "stack underflow"
        else:
            pop_value = self.top.value
            self.top = self.top.next
            return pop_value

# given input is " hello" reverse the string "olleh"

def reverse():
    str = "hello"
    s = Stack()

    for  i in  str:
        s.push(i)

    rev  = ""

    while not s.is_empty():
        rev = rev + s.pop()

    return rev

print(reverse())
def text_editor(string,pattern):
    s = Stack()
    v = Stack()

    for i in string :
        s.push(i)

    for  i in pattern:
        if i =="u":
            value = s.pop()
            v.push(value)
        elif i == "r":
            value = v.pop()
            s.push(value)
    res = ""
    while not s.is_empty():
        res = s.pop()+res
    return res

l =[
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

string="hello"
pattern= "uuuru"
print(text_editor(string, pattern))
# op: he




s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.traverse()
print(s.peak())
s.pop()
s.traverse()
print("*"*50)
class MinStack():
    def __init__(self):
        self.stack =[]
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        min_value = min(value, self.min_stack[-1] if self.min_stack else value)
        self.min_stack.append(min_value)

    def minnum(self):
        return self.min_stack[-1]
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()


    def top(self):
        return self.stack[-1]

a = MinStack()
a.push(-2)
a.push(0)
a.push(-3)
print(a.minnum())
a.pop()
print(a.top())
print(a.minnum())


print("*"*30)
class stack:
    def evalRPN(self,str):
        s = []
        for i in str:
            
            if i =="+":
                s.append(s.pop()+s.pop())
            elif i =="-":
                a= s.pop()
                b = s.pop()
                s.append(b-a)
            elif i =="*":
                s.append(s.pop() *s.pop())
            elif i =="/":
                a= s.pop()
                b = s.pop()
                s.append(int(b/a))
            else:
                s.append(int(i))

        return s[-1]
a= stack()
print(a.evalRPN(["2","1","+","3","*"]))