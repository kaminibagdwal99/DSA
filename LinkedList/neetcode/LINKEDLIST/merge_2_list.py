class Node:
    def __init__(self,value=0):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)


def merge_two_list(list1,list2):
    dummy = Node()
    cur = dummy
    while list1 and list2:
        if list1.value < list2.value:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
    return dummy.next

def print_ll(head):
    cur  = head
    while cur:
        print(cur.value, "->", end = " ")
        cur = cur.next
    print("None")

a.next = b
b.next = c

d.next = e
e.next = f

print("list 1 is ")
print_ll(a)
print("list 2 is ")
print_ll(d)
merged_list = merge_two_list(a,d)
print("merged list is ")
print_ll(merged_list)
