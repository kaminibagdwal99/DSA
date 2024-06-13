class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

def printLL(head):

    cur = head
    while cur:
        print(cur.value,"->", end = "")
        cur = cur.next
    print()


def add(l1):
    a,b = l1,l1
    while True:
        a = a.next
        b = b.next.next
        if a==b:
            break
    slow1 = l1
    while slow1 !=a:
        slow1= slow1.next
        a = a.next
    return slow1.value
        
    return a.value
    

        

a = Node(4)
b = Node(1)
c = Node(5)
d = Node(6)
e = Node(1)
f= Node(8)
g= Node(4)
h = Node(1)


a.next = b
b.next = c
c.next = d
d.next = e

e.next = f
f.next = g
g.next = h
h.next = f

# printLL()
s = add(a)
print(s)
