"""ou are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:



Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]
Example 2:



Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]"""

class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = Node(0,head)
        groupprev = dummy
        while True:
            kth = self.kth(groupprev, k)
            if not kth:
                break
            groupnext= kth.next # node agter kth node
            # reverse
            prev, cur = kth.next, groupprev.next
            while cur != groupnext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp

        return dummy.next
    
    def kth(sel, cur, k):
        while cur and k >0:
            cur= cur.next
            k =k-1
        return cur


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f= Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


def print_ll(head):
    cur = head
    while cur:
        print(cur.value, "->",end = " ")
        cur = cur.next
    print("None")



print_ll(a)
b = Solution()
print_ll(b.reverseKGroup(a, k=3))