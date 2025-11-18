class Node:
    def __init__(self, val=0):
        self.val=val
        self.next = None
def reverse(a):
    cur=a
    prev=None
    while cur:
        temp=cur.next

        cur.next = prev
        prev = cur
        cur=temp
    return prev

def merge_two_list(l1, l2):
    dummy = Node()
    cur = dummy 

    while l1 and l2:
        if l1.val<=l2.val:
            cur.next = l1
            l1=l1.next
        else:
            cur.next = l2
            l2= l2.next
        cur=cur.next
    if l1:
        cur.next=l1
    if l2:
        cur.next=l2
    return dummy.next


def print_ll(a):
    cur=a
    while cur:
        print(cur.val,"->", end="")
        cur=cur.next
    print(None)

def linkded_list(a):
    slow, fast = a,a
    while fast and fast.next:
        slow=slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False

def reorder_list(a):
    slow, fast = a, a.next
    while fast and fast.next:
        slow= slow.next
        fast = fast.next.next
    cur = slow.next

    slow.next = None
    prev=None

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    first_haf, second_hlf = a, prev

    while second_hlf:
        t1, t2 = first_haf.next, second_hlf.next


        first_haf.next =second_hlf
        second_hlf.next = t1
        first_haf, second_hlf= t1, t2
    return a


def remove_n_node(a, n):
    slow, fast = a, a
    for i in range(n):
        fast = fast.next

    while fast and fast.next:
        slow=slow.next
        fast = fast.next

    slow.next = slow.next.next
    return a
    

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c

d.next = e
e.next = f

print("list 1 is ")
print_ll(a)
print("list 2 is ")
print_ll(d)
merged_list = add_two_list(a,d)
print("added list is ")
print_ll(merged_list)