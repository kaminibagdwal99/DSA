# # # # class Node:
# # # #     def __init__(self, val):
# # # #         self.val = val
# # # #         self.next = None

# # # # class Stack:
# # # #     def __init__(self):
# # # #         self.top = None

# # # #     def push(self, val ):
# # # #         new_node = Node(val)
# # # #         new_node.next = self.top
# # # #         self.top = new_node

# # # #     def is_empty(self):
# # # #         return self.top == None
    
# # # #     def traverse(self):
# # # #         cur = self.top
# # # #         result = ""
# # # #         while cur:
# # # #             result = result + str(cur.val) + "->"
# # # #             cur = cur.next
# # # #         return result
    
# # # #     def peek(self):
# # # #         if self.is_empty():
# # # #             return " underflow"
# # # #         else:
# # # #             return self.top.val
        
# # # #     def pop(self):
# # # #         if self.is_empty():
# # # #             return " underflow"
# # # #         else:
# # # #             pop_value = self.top.val
# # # #             self.top = self.top.next
# # # #             return pop_value
        
    
# # # #     def size(self):
# # # #         count = 0
# # # #         temp = self.top
# # # #         while temp is not None:
# # # #             count += 1
# # # #             temp = temp.next
# # # #         return count


# # # # def reverse(str):
# # # #     s = Stack()

# # # #     for i in str:
# # # #         s.push(i)

# # # #     result = ""

# # # #     while not s.is_empty():
# # # #         result = result+s.pop()
# # # #     return result

    


# # # # # str = "hello"
# # # # # print(reverse(str))


# # # # def text_editor(input, pattern):

# # # #     s = Stack()
# # # #     v = Stack()

# # # #     for i in input:
# # # #         s.push(i)

# # # #     for i in pattern:
# # # #         if i == "u":
# # # #             v.push(s.pop())
# # # #         elif i == "r":
# # # #             s.push(v.pop())

# # # #     result=""

# # # #     while not (s.is_empty()):
# # # #         result =   result + s.pop()

# # # #     return result
    

# # # # a = text_editor("hello","uuuru")

# # # # print("answer is ", a)



# # # # def celebrity_problem(l):
# # # #     s = Stack()
# # # #     for i in range(len(l)):
# # # #         s.push(i)

# # # #     while s.size() >=2:
# # # #         i = s.pop()
# # # #         j = s.pop()

# # # #         if l[i][j] ==0:
# # # #             s.push(i)
# # # #         else:
# # # #             s.push(j)

# # # #     celeb = s.pop()


# # # #     for i in range(len(l)):
# # # #         if i != celeb:
# # # #             if l[i][celeb]==0 or l[celeb][i]==1:
# # # #                 return " not a celbrity"


# # # #     return ( "celebrity is", celeb)


    



# # # # l =[
# # # #     [0,0,1,1],
# # # #     [0,0,1,0],
# # # #     [0,0,0,0],
# # # #     [0,0,1,0]
# # # # ]

# # # # print(celebrity_problem(l))

# # # # #balanced parathesis
# # # # def is_balanced(expression):
# # # #     s = Stack()

# # # #     opening_brackets = {'(', '{', '['}
# # # #     closing_brackets = {')', '}', ']'}

# # # #     for i in expression:
# # # #         if i in opening_brackets:
# # # #             s.push(i)
# # # #         elif i in closing_brackets:
# # # #             if s.is_empty():
# # # #                 return False
# # # #             top_char = s.pop()
# # # #             if not is_matching(top_char,i):
# # # #                 return False
            
# # # #     return s.is_empty()



# # # # def is_matching(opening, closing):
# # # #     bracket_pairs = {')': '(', '}': '{', ']': '['}
# # # #     return bracket_pairs[closing] == opening

            




# # # # expression = "{(a+b)+(c+d)}"
# # # # result = is_balanced(expression)

# # # # if result:
# # # #     print("The expression is balanced.")
# # # # else:
# # # #     print("The expression is not balanced.")

# # # class MinStack():
# # #     def __init__(self):
# # #         self.stack = []
# # #         self.minstack =[]

# # #     def push(self, val):
# # #         self.stack.append(val)
# # #         val = min(val, self.minstack[-1] if self.minstack else val)
# # #         self.minstack.append(val)

# # #     def pop(self):
# # #         self.stack.pop()
# # #         self.minstack.pop()

# # #     def top(self):
# # #         return self.stack[-1]
    
# # #     def getmin(self):
# # #         return self.minstack[-1]
    
# # # a = MinStack()
# # # a.push(-2)
# # # a.push(0)
# # # a.push(-3)
# # # print(a.getmin())
# # # a.pop()
# # # print(a.top())
# # # print(a.getmin())


# # class solution:
# #     def evalRPN(self, list):
# #         stack = []

# #         for i in list:
# #             if i =="+":
# #                 stack.append(stack.pop()+stack.pop())
# #             elif i == "-":
# #                 a,b = stack.pop(),stack.pop()
# #                 stack.append(b-a)

# #                 pass
# #             elif i == "*":
# #                 stack.append(stack.pop() *stack.pop())
# #             elif i == "/":
# #                 a,b = stack.pop(),stack.pop()
# #                 stack.append(int(b/a))

                
# #             else:
# #                 stack.append(int(i))

# #         return stack[0]
    

# # a= solution()
# # print(a.evalRPN(["2","1","-","3","/"]))


    

# class solution:
#     def generate_parenthesis(self, n):
#         stack =[]
#         res = []

#         def backtrack(open, close):
#             if (n ==open==close):
#                 res.append("".join(stack))

#             if open <n:
#                 stack.append("(")
#                 backtrack(open+1, close)
#                 stack.pop()

#             if open > close:
#                 stack.append(")")
#                 backtrack(open,close+1)
#                 stack.pop()
#         backtrack(0,0)

#         return res
    

# a = solution()
# print(a.generate_parenthesis(3))


# class Solution:
#     def dailyTemperatures(self,temp):
#         res = [0] *len(temp)
#         stack = []

#         for i in range(len(temp)):
#             while stack and temp[i]>temp[i-1]:
#                 prev_index = stack.pop()
#                 res[prev_index]= i-prev_index
#                 pass
#             stack.append(i)

#         return res

# a = Solution()
# print(a.dailyTemperatures([73,74,75,71,69,72,76,73]))



# stack using array


class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self,value):
        if self.top == self.size -1:
            return "overflow"
        else:
            self.top +=1
            self.stack[self.top]= value

    def pop(self):
        if self.top == -1:
            return "empty"
        else:
            data = self.stack[self.top]
            self.top -=1
            return data


s = Stack(3)
print(s.stack)
print(s.push(4))
print(s.stack)
print(s.push(5))
print(s.pop())
print(s.push(5))
print(s.stack)