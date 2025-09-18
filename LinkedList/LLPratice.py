class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

a = Node(7)
b = Node(13)
c = Node(11)
d = Node(10)
e = Node(1)

a.next = b
b.next= c
c.next = d
d.next = e

a.random = None
b.random = a
c.random = e
d.random = c
e.random = a

def print_ll(root):
    cur = root 
    while cur:
        print(cur.val,"->",end = " ")
        random_val = cur.random.val if cur.random else None
        print(random_val,">>>>", end=" ")
        cur = cur.next


class Solution:
    def copyRandomList(self, head):
        oldtonew ={None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldtonew[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy = oldtonew[cur]
            copy.next = oldtonew[cur.next]
            copy.random = oldtonew[cur.random]
            cur=cur.next
        return oldtonew[head]
        
z = Solution()
print_ll(a)
print()
print_ll(z.copyRandomList(a))