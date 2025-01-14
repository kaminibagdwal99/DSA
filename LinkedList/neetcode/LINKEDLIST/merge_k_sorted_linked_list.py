"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

[1,4,5],[1,3,4],[2,6]

a = ListNode(1)
b = ListNode(4)
c  = ListNode(5)
a.next = b
b.next = c
e = ListNode(1)
f = ListNode(3)
g = ListNode(4)

e.next = f
f.next = g

h = ListNode(2)
i = ListNode(6)

h.next = i
class Solution:
    def mergeKLists(self, lists):
        if len(lists)==0:
            return []

        for i in range(1,len(lists)):
            lists[i] = self.merge(lists[i-1], lists[i])

        return lists[-1]

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next = l1
                l1=l1.next

            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next =l2
        return dummy.next



def print_ll(cur):
    while cur:
        print(cur.val ,"->", end="")
        cur = cur.next
    print(None)

print_ll(a)
print_ll(e)
print_ll(h)

z = Solution() 
lists = [a,e,h]
res = z.mergeKLists(lists)
print_ll(res)