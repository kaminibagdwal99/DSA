class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class Solution:

    def reverseKGroup(self, a, k):
        dummy = Node(0,a)
        groupPrev= dummy

        while True :
            kth = self.getkth(groupPrev,k)
            if not kth:
                break

            groupNext= kth.next

            prev, cur = kth.next, groupPrev.next

            while cur !=groupNext:
                temp= cur.next
                cur.next = prev
                prev=cur
                cur=temp

            tmp = groupPrev.next
            groupPrev.next= kth
            groupPrev=tmp

        return dummy.next

    def getkth(self, cur, k):
        while cur and k>0:
            cur=cur.next
            k=k-1
        return cur
    


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


def print_ll(head):
    cur = head
    while cur:
        print(cur.value, "->",end = " ")
        cur = cur.next
    print("None")



print_ll(a)
b = Solution()
print_ll(b.reverseKGroup(a, k=2))