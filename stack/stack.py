"""stack is DS , Lifo (last in first out) . Implement Stack using Linked List opeartion ( top and bottom )
top( head) : push insert item from top, pop item from top,
peak : to check the topmost item, 
is_empty : tell if stack is empty
so basically a stack using LL is a LL where operation can be only only from head"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top == None

    def push(self, value):# 3>2>1 >>> 4>3>2>1
        new_node = Node(value)
        new_node.next =self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        while temp!= None:
            print(temp.value)
            temp = temp.next


    def peak(self):
        if self.is_empty():
            return "empty Stack"
        else:
            return self.top.value

    def pop(self):
        if self.is_empty():
            return "empty stack"
        else:
            pop_value = self.top.value
            self.top = self.top.next
            return pop_value

    def size(self):
        count = 0
        temp = self.top
        while temp is not None:
            count += 1
            temp = temp.next
        return count

# given input is " hello" reverse the string "olleh"

def reverse():
    str_input = "hello"
    s = Stack()

    for i in str_input:
        s.push(i)
    
    result = ""
    while not s.is_empty():
        result += s.pop()  # Append the popped character to result

    return result

# reversed_string = reverse()
# print(reversed_string)


# text editor 2 inpurt
"""
string:hello
pattern: uuuru
op: he
"""

def text_editor(input, pattern):

    s = Stack()
    v  = Stack()
    result = ""

    for i in input:
        s.push(i)
    
    for i in pattern:
        
        
            if i =="u":
                data = s.pop()
                v.push(data)
            elif i =="r":
                data = v.pop()
                s.push(data)
            

    while (not s.is_empty()):
        result = s.pop()+result 
    return result

# print(text_editor("hello","uuuru"))


#celebrity Problem

"""a celebrity is a person who donot know anybody but other know him """

l =[
    [0,0,1,1],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,1,0]
]

def find_celebrity(L):
    s = Stack()
    for i in range(len(L)):
        s.push(i)

    while s.size() >=2:
        i = s.pop()
        j = s.pop()

        if L[i][j]==0:
            s.push(i)
        else:
            s.push(j)

    celeb = s.pop()

    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb]==0 or  L[celeb][i]==1:
                return "no celeb"

    return ( "celebrity is", celeb)
    

# print(find_celebrity(l))

#balanced parathesis


def is_balanced(expression):
    stack = Stack()

    opening_brackets = {'(', '{', '['}
    closing_brackets = {')', '}', ']'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if not is_matching(top_char, char):
                return False

    return stack.is_empty()

def is_matching(opening, closing):
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    return bracket_pairs[closing] == opening

# Example usage
expression = "{(a+b)+(c+d)}"
result = is_balanced(expression)

if result:
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")
    

    

    

        




