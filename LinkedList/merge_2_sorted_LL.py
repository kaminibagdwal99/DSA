class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None



def print_LL(head):
    cur = head
    while cur:
        print(cur.val, end=">>")
        cur = cur.next
    print(None)

def sum_of_sortd_list(a,d):
    cur = dummy = Node()
    if not a:
        return d
    if not d:
        return a
    while a and d:
        if a.val < d.val:
            cur.next =a
            a,cur = a.next, a
        else:
            cur.next =d
            d,cur = d.next, d

        if a or d:
            cur.next = a if a else d
    return dummy.next



a = Node(1)
b = Node(2)
c= Node(3)
d= Node(1)
e = Node(3)
f = Node(4)
a.next = b
b.next = c
d.next = e
e.next = f


print("Initial linked list:")
print_LL(a)
print_LL(d)
s = sum_of_sortd_list(a,d)

print("After merged")
print_LL(s)