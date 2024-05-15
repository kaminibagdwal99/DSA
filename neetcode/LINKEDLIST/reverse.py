class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def print_ll(head):
    cur = head
    while cur:
        print(cur.value, "->",end = " ")
        cur = cur.next
    print("None")

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print_ll(a)
b = reverse(a)
print_ll(b)

