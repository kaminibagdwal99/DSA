class Node:
    def __init__(self, val =0):
        self.val = val 
        self.next = None


def reorder_list(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    prev = None
    cur = second
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    first_half, seconf_half = head, prev
    while seconf_half:
        t1, t2 = first_half.next, seconf_half.next
        first_half.next = seconf_half
        seconf_half.next=t1
        first_half , seconf_half= t1, t2
    return head

def print_ll(root):
    cur= root
    while cur:
        print(cur.val, "->", end = " ")
        cur = cur.next
    print(None)




