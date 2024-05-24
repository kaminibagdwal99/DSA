#Stack using array


class Stack:

    def __init__(self,size):
        self.size = size #size of array
        self.__stack = [None] * self.size #[None, None, None] if size =3 only we will use only append and pop
        self.top = -1 #no value

    def push(self, value):
        if self.top ==self.size -1:
            return " overflow"
        else:
            self.top = self.top + 1 # increase top with one
            self.__stack[self.top]=value
            return "operation succcesful"

    def pop(self):
        if self.top ==-1:
            return "underflow"
        else:
            data= self.__stack[self.top]
            self.top = self.top-1
            return " operation successful"

    def traverse(self):
        for i in range(self.top+1):
            print(self.__stack[i], end = ' ')


s = Stack(3)

print(s.push(2))
print(s.push(2))
print(s.traverse())
print(s.pop())
print(s.traverse())
