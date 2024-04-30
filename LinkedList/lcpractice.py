# # reverse the linked list

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def reverse(head):

#     cur = head
#     p = None

#     while cur:
#         next = cur.next
#         cur.next =p
#         p = cur
#         cur = next
#     return p


# def print_ll(head):
#     cur = head

#     while cur :
#         print(cur.value, "->" , end = " ")
#         cur = cur.next
#     print()



# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)

# n1.next = n2
# n2.next = n3
# n3.next = n4


# print_ll(n1)
# x =reverse(n1)
# print_ll(x)


# class Node:
#     def __init__(self, value):

#         self.value = value
#         self.next = None

# def printll(head):
#     cur = head

#     while cur:
#         print(cur.value, "->" , end = " ")
#         cur = cur.next
#     print()


# def middle(head):
#     slow,fast = head, head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow


# a = Node(1)
# b= Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
# f = Node(6)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# printll(a)
# v = middle(a)
# print(v.value)

# remove nth node from last

class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None

def LL(a):
    cur = a
    while cur:
        print(cur.value, "->", end =" ")
        cur = cur.next
    print("None")

def delete_from_node(cur,n):
    slow, fast = cur, cur

    for i in (n):
        fast = fast.next







a = Node(1)
b= Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

LL(a)
