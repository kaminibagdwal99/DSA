"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack=[]

    def push(self,val):
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def minnum(self):
        return self.minstack[-1]

a = MinStack()
a.push(-2)
a.push(0)
a.push(-3)
print(a.minnum())
a.pop()
print(a.top())
print(a.minnum())