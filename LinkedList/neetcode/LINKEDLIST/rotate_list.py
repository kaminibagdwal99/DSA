class Node:
    def __init__(self,val =0):
        self.val = val
        self.next = None


def rotate(a, k):
    # compute the length of LL:
    head = a
    
    len = 1
    if not head or k == 0:
        return head
    while head.next != None:
        len +=1
        head = head.next
    head.next = a #make a circular link


    if k >=len:
        k = k%len # if k >= len

    k = len-k
    for _ in range(k):
        head= head.next # goes upto that node where you have to break the connection

    a = head.next #shift head to new head
    head.next = None # make the node where we have to break the connection pointing to Null

    return a


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
a = rotate(a,7)
print_ll(a)