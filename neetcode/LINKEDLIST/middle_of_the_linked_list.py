class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next  = None

    def middle_of_the_list(self):
        slow, fast = self, self
        while fast and fast.next:
            slow = slow.next
            fast  = fast.next.next
        return slow.val


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
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print_ll(a)
print(a.middle_of_the_list())
