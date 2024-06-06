class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [0]* self.size

    def push(self, value):
        if self.top == self.size -1:
            return "Stack Overflow"
        else:
            self.top +=1
            self.stack[self.top]=value

    def pop(self):
        if self.top ==-1:
            return "stack underflow"
        else:
            data = self.stack[self.top]
            self.top = self.top -1

    def top(self):
        return self.stack[self.top]


s = Stack(10)
s.push(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.stack)
s.pop()
print(s.stack)
s.push(8)
s.push(9)
print(s.stack)




