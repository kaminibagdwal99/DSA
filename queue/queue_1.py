"""a queue is Linear DS which is  FIFO where insertion is from head and deletion is from end. head is 
called front and tail is called read. insertion is known as enqueue and deletion is known as dequeue.

we will implement a queue with LL where we take head as well tail as if we only single pointer like
head( insertion TC will o(n) while deletion will be o(1) therefore we will consider taking two pointer
head and tail"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front

        else:
            self.rear.next=new_node
            self.rear = new_node

    def dequeue(self):
        if self.front == None:
            return "empty Queue"
        else:
            self.front = self.front.next

    def  transverse(self):
        temp =  self.front

        while temp != None:
            print(str(temp.value )+ "|" ,end = " ")
            temp = temp.next

    def is_empty(self):
        return self.front == None

    def size(self):
        temp =  self.front
        counter = 0

        while temp != None:
            temp = temp.next
            counter = counter +1
        return counter

    def front_item(self):
        if self.front==None:
            return "empty queue"
        else:
            return self.front.value

    
    def rear_item(self):
        if self.rear==None:
            return "empty queue"
        else:
            return self.rear.value

def fun(num):
    if (num==0):
        return 0
    else:
        q.enqueue(num%10)
        res = fun(num//10)
        res = res * 10 + q.dequeue()
        return res

q = Queue()
print(fun(123))
q.enqueue(1)
print(q.front.value, q.front.next, q.rear.value,q.rear.next)
q.enqueue(2)
print(q.front.value, id(q.front.next),id(q.rear), q.rear.value,q.rear.next)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.front.value, id(q.front.next),id(q.rear), q.rear.value,q.rear.next)
print(q.transverse())
q.dequeue()
print(q.transverse())
print("size of queue is ",q.size())
print("front item is ",q.front_item())
print("rear item is ",q.rear_item())




