class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class LinkdedList:
    def __init__(self):
        self.head = None #empty ll or: when head = None
        self.n = 0 #for checking number of nodes

    def __len__(self):
        return self.n

    def insert_head(self,value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def __str__(self):
        cur = self.head
        result =""

        while cur != None:
            result = result+ str(cur.data) +" "

            cur = cur.next
        return result[:]


    def append(self,value):

        new_node = Node(value)


        if self.head ==None:
            self.head = new_node
            self.n = self.n+1
            return

        cur = self.head 

        while cur.next !=None:
            cur = cur.next

        cur.next = new_node
        self.n = self.n +1


    def insert_after(self, pos, value):

        new_node = Node(value)

        cur = self.head

        while cur != None:
            if cur.data == pos:
                break
            cur = cur.next


        if cur != None: # item found
            new_node.next = cur.next
            cur.next = new_node
            self.n = self.n +1

        else: # loop pura chala
            print( "Item Not found")
    
    def clear(self):
        self.head = None
        self.n = 0            


    def  delete_head(self):
        if self.head == None:
            return ("empty ")
        self.head = self.head.next 
        self.n = self.n -1


    def pop(self):

        if self.head == None:
            return ("empty LL ")

        cur = self.head


        if cur.next == None:
            return self.delete_head()

        while cur.next.next !=None:
            cur = cur.next

        cur.next = None
        self.n = self.n -1

    def remove(self, value):


        if self.head == None:
            return ("empty LL ")


        if self.head.data == value:
            return self.delete_head()
        cur = self.head
        while cur.next != None:
            if cur.next.data == value:
                break
            cur = cur.next

        if cur.next !=None:
            cur.next = cur.next.next
        else:
            print("item not found")

    def search(self, value):
        cur = self.head
        pos = 0
        while cur != None:
            if cur.data ==value:
                return pos
            cur = cur.next
            pos = pos +1
        return "Not Found"


    def __getitem__(self, index):
        cur = self.head
        pos = 0
        while cur != None:
            if pos ==index:
                return cur.data
            cur = cur.next
            pos = pos +1
        return "Not Found"

    #wap to find max value in linked list and replace with given value

    def replace_with(self, value):
        cur = self.head
        max = cur
        while cur != None:
            if cur.data >max.data:
                max = cur
            cur = cur.next
        max.data = value

    #wap to add the odd position value of the LL 1>2>3>4 >5 ( sum = 2+4 = 6)
    def sum_odd(self):
        cur = self.head
        sum = 0
        counter = 0
        while cur != None:
            if counter%2 !=0:
                sum =sum+cur.data
            counter +=1
            cur = cur.next

        return sum


    #wap to reverse a linked list containg integer data 2>4>6>8>none 8>6>4>2>none


    def reverse(self):
        cur = self.head
        prev = None
        while cur!=None:
            next_node = cur.next
            cur.next = prev
            prev = cur 
            cur = next_node

        self.head = prev

    # given a lined list wap  to return a new string that i screated by  appending  all the charcrter  
    #  given in the linked list as per given rule
    #rule : 
    # 1.replace * or / by single space
    # 2. if */ are together replce with space and string with upper case
    #inp

    def change_Sentence(self):
        cur = self.head
        while cur!=None:
            if cur.data == "*" or cur.data =="/":
                cur.data =" "

                if cur.next.data =="*" or cur.next.data == "/":
                    cur.next.next.data =cur.next.next.data.upper()
                    cur.next = cur.next.next
            cur = cur.next

            




    
v = LinkdedList()

v.insert_head("t")
v.append("h")
v.append("e")
v.append("*")
v.append("/")
v.append("s")
v.append("k")
v.append("y")
v.append("*")
v.append("is")
v.append("/")
v.append("/")
v.append("b")
v.append("l")
v.append("u")
v.append("e")

print(v)

v.change_Sentence()


print(v)





