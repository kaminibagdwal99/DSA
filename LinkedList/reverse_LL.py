class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


def reverse_LL(head):
    cur= head
    prev = None

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def print_LL(head):
    cur = head
    while cur:
        print(cur.data, end=">>")
        cur = cur.next
    print()



a = Node(1)
b = Node(2)
c= Node(3)
d= Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e


print("Initial linked list:")
print_LL(a)
r = reverse_LL(a) 
print("reverse linked list:")

print_LL(r)

    