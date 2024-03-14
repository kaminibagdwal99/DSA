#Implementing a queue using two stacks in Python can be achieved by using one stack for enqueue 
# operations and another stack for dequeue operations. Here's a basic implementation:



class QueueUsingTwoStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        # Push item onto the enqueue stack
        self.enqueue_stack.append(item)

    def dequeue(self):
        # If dequeue stack is empty, transfer elements from enqueue stack 
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                raise IndexError("Queue is empty")
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        
        # Pop and return the front element from the dequeue stack
        return self.dequeue_stack.pop()

    def is_empty(self):
        # Check if both stacks are empty
        return not self.enqueue_stack and not self.dequeue_stack

    def size(self):
        # Return the total number of elements in the queue
        return len(self.enqueue_stack) + len(self.dequeue_stack)

# Example Usage:
queue = QueueUsingTwoStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: 3

print("Dequeue:", queue.dequeue())   # Output: 1
print("Dequeue:", queue.dequeue())   # Output: 2

print("Is Empty:", queue.is_empty())  # Output: False

queue.enqueue(4)
print("Queue size:", queue.size())  # Output: 2
