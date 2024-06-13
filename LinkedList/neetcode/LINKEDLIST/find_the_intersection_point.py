class Node:
    def __init__(self, val =0):
        self.val = val
        self.next = None

def intersection(head):
    slow, fast = head, head
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow1= head
    while slow !=slow1:
        slow = slow.next
        slow1= slow1.next
    return slow.val
        
    
a = Node(1)
b = Node(9)
c = Node(7)
d = Node(2)
e = Node(4)
f = Node(3)
a.next = b
b.next =c
c.next = d
d.next = e
e.next = f
f.next=d

print(intersection(a))
