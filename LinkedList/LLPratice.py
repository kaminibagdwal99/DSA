class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None



a = Node(0)
a.next = Node(1)
a.next.next = Node(2)
a.next.next.next = Node(3)



b = Node(1)
b.next = Node(5)
b.next.next = Node(4)

def printll(head):
    cur = head
    while cur:
        print(str(cur.val) +"->", end=" ")
        cur = cur.next
    print()
    
    
def add(head, head2):
    dummy = Node()
    cur = dummy
    carry =0

    while head or head2 or carry:
        if head:
            carry += head.val
            head = head.next
        if head2:
            carry += head2.val
            head2 = head2.next

        cur.next =Node(carry %10)
        cur = cur.next
        carry = carry//10

    return dummy.next

 



printll(a)
printll(b)
v = add(a,b)
printll(v)

