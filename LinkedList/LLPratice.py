class Node :
    def __init__(self, value=0):
        self.value = value
        self.next = None


def print_LL(head):
    while head:
        print( head.value ,"=>", end=" ")
        head = head.next
    print("None")

def add_two_number(list1,k):
    cur = list1

    if not cur  or k == 0:
        return cur
    len = 1

    while cur.next :
        len = len+1
        cur = cur.next

    cur.next = list1

    k=k %len
    end = len-k

    for _ in range(end):
        cur=cur.next

    list1 = cur.next
    cur.next = None
    return list1


    

        


a = Node(1)
b = Node(2)
c = Node(3)



d = Node(6)
e  = Node(4)
f = Node(5)

a.next = b
b.next  = c
c.next =d
d.next = e
e.next = f




print_LL(a)

z =add_two_number(a, k=3)
print_LL(z)



from collections import OrderedDict

class LRUCache:
    def __init__(self,capacity) :
        
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self,key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif self.capacity <= len(self.cache):
            self.cache.popitem(last = False)

        self.cache[key]=value  




obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))