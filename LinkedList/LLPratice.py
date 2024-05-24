class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def tranverse(self):
        temp = self.top
        while temp:
            print(temp.val,"->", end = "")
            temp = temp.next
        print(None)

    def pop(self):

        if(self.is_empty()):
            return "Stack UNderFlow"
        else:

            pop_value = self.top.val
            self.top= self.top.next
            return pop_value

    def peek(self):
        if(self.is_empty()):
            return "Stack UNderFlow"
        return self.top

def reverse(str):
    a = Stack()
    for i in str:
        a.push(i)

    result = ""
    while not a.is_empty():
        result +=a.pop()
    
    return result




# print(reverse("hello"))

def text_editor(str, pattern):
    s=Stack()
    v = Stack()

    for i in str:
        s.push(i)

    for i in pattern:
        if i =="u":
            value =s.pop()
            v.push(value)
        elif i =="r":
            value = v.pop()
            s.push(value)

    result = ""
    while (not s.is_empty()):
        result=s.pop() +result
    return result

print(text_editor("hello","uuru"))


l =[
    [0,0,1,1],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,1,0]
]





# a = Stack()

# a.push(8)
# a.push(7)
# a.push(6)
# a.tranverse()
# print(a.delete_from_head())
# a.tranverse()
# print(a.peek())
