class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def insert_head(self,value):
        new_node = Node(1)
        new_node.next = self.head
        self.head = new_node


