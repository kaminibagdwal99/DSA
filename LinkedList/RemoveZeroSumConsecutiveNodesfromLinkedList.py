class Node:
    def __init__(self,val =0):
        self.val = val
        self.next = None

def remove_zero_sum_consecutive_node(head):

        arr =[]
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr.sort()

        if cur:
            pass




a = Node(1)
b = Node(2)
c= Node(3)
d= Node(-3)
e = Node(1)
a.next = b
b.next = c
c.next = d
d.next = e


remove_zero_sum_consecutive_node(a)