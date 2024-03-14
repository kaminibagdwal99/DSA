class Node:
    def __init__(self,val =0):
        self.val = val
        self.next = None


def print_LL(b):
    a = b

    while a:
        print(a.val, end =">>")
        a=a.next
    print("None")

def  remove_node_from_last(a, n):
    slow , fast = a,a
    for i in range(n):
        fast = fast.next

    if not fast:
        return fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return a




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
m = remove_node_from_last(a,2)

print("middle element")
print_LL(m)