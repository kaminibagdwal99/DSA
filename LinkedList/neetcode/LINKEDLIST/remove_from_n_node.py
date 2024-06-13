class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_n_node(head, n):
    slow, fast = head, head

    if fast is None:
        return head.next 

    for i in range(n):
        fast = fast.next

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next
    slow.next = slow.next.next
    return head.next
 


def print_ll(head):
    cur = head
    while cur:
        print(cur.val, "->",end = " ")
        cur = cur.next
    print("None")

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print_ll(a)

remove_n_node(a, 2)

print_ll(a)
