class Node:
    def __init__(self, val =0):
        self.val = val
        self.next = None

def intersection(headA,headB):
    a,b = headA, headB
    while a!=b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a.val
    
a = Node(1)
b = Node(9)
c = Node(1)
d = Node(2)
e = Node(4)
f = Node(3)
a.next = b
b.next =c
c.next = d
d.next = e

f.next=d

print(intersection(a,f))
