class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):

    if not head or not head.next:
        return head

    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None


    # reverse second half
    cur = second_half
    prev = None
    while cur :
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next


    first_half, second_half  = head, prev
    print_ll(head)
    print_ll(prev)
    while second_half:
        temp1, temp2 = first_half.next, second_half.next
        first_half.next = second_half
        second_half.next = temp1
        first_half, second_half = temp1,temp2

    return head


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

reorder_list(a)

print_ll(a)
