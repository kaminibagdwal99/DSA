class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_LL(b):
    a = b

    while a:
        print(a.val, end =">>")
        a=a.next
    print("None")

def middle_ll(a):
    slow, fast = a,a
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

a = Node(1)
b = Node(2)
c= Node(3)
d= Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e

m = middle_ll(a)


print("Initial linked list:")
print_LL(a)
print("middle element")
print(m.val)
