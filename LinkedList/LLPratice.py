class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head= None):
        self.head= None
        self.n = 0 

    def __len__(self):
        return self.n
    
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n +=1

    def __str__(self):
        cur = self.head
        result = ""
        while cur != None :
            result = result + str(cur.value) +"->"
            cur = cur.next
        result += "None"
        return result[:]

    def append(self, value):
        if self.head ==None:
            self.insert_head(value)
            return

        cur = self.head
        new_node = Node(value)

        while cur.next != None:
            cur= cur.next

        cur.next = new_node
        self.n = self.n+1

    def insert_after(self,value,target):
        new_node = Node(value)

        cur = self.head

        while cur != None:
            if cur.value ==target:
                break
            cur = cur.next

        if cur!= None:
            new_node.next = cur.next
            cur.next = new_node
            self.n +=1

        else:
            print("item not found")

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return "empty LL"

        self.head = self.head.next
        self.n -=1

    def pop(self):
        if self.head == None:
            return "empty LL"
        if self.head.next == None:
            return self.delete_head()

        cur = self.head

        while cur.next.next != None:
            cur = cur.next

        cur.next = None
        self.n -=1

         



        



v = LinkedList()
# v.insert_head(8)
v.insert_head(9)
v.append(6)
v.insert_after(3,6)
print(len(v))
v.pop()
print(len(v))
print(v)