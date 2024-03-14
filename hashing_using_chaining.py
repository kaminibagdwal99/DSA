class Node:
    def __init__(self,key,value):
        self.key = key
        self.data = value
        self.next = None


class LinkdedList:
    def __init__(self):
        self.head = None #empty ll or: when head = None
        self.n = 0

    def __len__(self):
        return self.n


    def traverse(self):
        cur = self.head

        while cur != None:
            print(cur.key,"-->",cur.data," ", end = " ")

            cur = cur.next

    def size(self):
        cur = self.head
        size = 0

        while cur != None:
            size = size+1


            cur = cur.next
        return size



    def append(self,key,value):

        new_node = Node(key,value)


        if self.head ==None:
            self.head = new_node
            self.n = self.n+1
            return

        cur = self.head 

        while cur.next !=None:
            cur = cur.next

        cur.next = new_node
        self.n = self.n +1



    def remove(self, key):


        if self.head == None:
            return ("empty LL ")


        if self.head.key == key:
            return self.delete_head()
        cur = self.head
        while cur.next != None:
            if cur.next.key == key:
                break
            cur = cur.next

        if cur.next !=None:
            cur.next = cur.next.next
        else:
            print("item not found")

    def search(self, key):
        cur = self.head
        pos = 0
        while cur != None:
            if cur.key ==key:
                return pos
            cur = cur.next
            pos = pos +1
        return -1


    def __getitem__(self, index):
        cur = self.head
        pos = 0
        while cur != None:
            if pos ==index:
                return cur.data
            cur = cur.next
            pos = pos +1
        return "Not Found"

    def get_node_at_index(self,index):
        temp = self.head 
        counter = 0 
        while temp != None:
            if counter == index:
                return temp
            temp = temp.next
            counter +=1
    

    def  delete_head(self):
        if self.head == None:
            return ("empty ")
        self.head = self.head.next 
        self.n = self.n -1


    


class Dictionaries:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        #array of ll
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        l=[]
        for i in range(capacity):
            l.append(LinkdedList())
        return l

    def put(self,key,value):
        bucket_index = self.hash_function(key)

        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            #insert
            self.buckets[bucket_index].append(key,value)
            self.size +=1
            load_factor = self.size/self.capacity

            print("load_factor is",load_factor)


            if (load_factor)>2:
                self.rehash()

        else:
            #update
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value

    
    def rehash(self):
        self.capacity = self.capacity *2
        old_buckets = self.buckets
        self.size =0
        self.buckets = self.make_array(self.capacity)

        for i in old_buckets:
            for j in range(i.size()):
                node = i.get_node_at_index(j)
                key = node.key
                value = node.data
                self.put(key,value)

    
    def __setitem__(self,key,value):
        self.put(key,value)


    def __delitem__(self,key):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)

    def __str__(self):
        for i in self.buckets:
            i.traverse()

        return ""




    def get(self, key):
        bucket_index = self.hash_function(key)
        res = self.buckets[bucket_index].search(key)

        if res == -1:
            return "not found"
        else:
            node = self.buckets[bucket_index].get_node_at_index(res)
            return node.data

    
    def __getitem__(self,key):
        return self.get(key)
    

    def get_node_index(self,bucket_index,key):
        node_index = self.buckets[bucket_index].search(key)

        return node_index


    def hash_function(self, key):
        return abs(hash(key))% self.capacity


e = Dictionaries(2)
e.put("python",4)
e.put("pytho",4)
e.put("thon",4)
e["java"]=89
e["c"]=90


print(e)


