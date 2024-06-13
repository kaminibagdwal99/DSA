class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Creating the linked list 4 -> 5 -> 1 -> 9
head = ListNode(4)
node1 = head.next = ListNode(5)
node2 = head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

# Print the original list
print("Original list:")
printList(head)

# Delete node with value 5
deleteNode(node1)

# Print the modified list
print("List after deleting node with value 5:")
printList(head)