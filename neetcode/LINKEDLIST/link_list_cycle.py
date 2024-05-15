class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None


def linkded_list(head):
    slow , fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast : 
            return True
    
    return False

a = Node(1)
b = Node(2)
c = Node(3)
d  = Node(4)

a.next = b
b.next = c
c.next = d
d.next = b 

print(linkded_list(a))