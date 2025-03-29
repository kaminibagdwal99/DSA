class Node:
    def __init__(self,value=0):
        self.value = value
        self.next = None

a = Node(9)
b = Node(2)
c = Node(4)
d = Node(9)
e = Node(4)
f = Node(6)


def add_two_list(list1,list2):
    dummy = Node()
    cur = dummy
    carry = 0
    while list1 or list2 or carry:
        if list1:
            carry += list1.value 
            list1 = list1.next
        if list2:
            carry += list2.value
            list2 = list2.next

        cur.next = Node(carry%10)
        cur = cur.next
        carry = carry //10

        
    return dummy.next

def print_ll(head):
    cur  = head
    while cur:
        print(cur.value, "->", end = " ")
        cur = cur.next
    print()

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
