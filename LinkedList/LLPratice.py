class Node :
    def __init__(self, value=0):
        self.value = value
        self.next = None


def print_LL(head):
    while head:
        print( head.value ,"=>", end=" ")
        head = head.next
    print("None")

def add_two_number(list1):
    slow,fast = list1, list1

    while fast :
        slow = slow.next
        fast= fast.next.next
        if slow ==fast:
            return True
    return False


    

        


a = Node(1)
b = Node(2)
c = Node(3)



d = Node(6)
e  = Node(4)
f = Node(5)

a.next = b
b.next  = c

c.next =d
d.next = e
e.next = f




# print_LL(a)

# z =add_two_number(a)
# print(z)


def duplicate(nums):
    slow , fast = 0,0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break
    slow1 = 0

    while True:
        slow1 = nums[slow1]
        slow = nums[slow]

        if slow == slow1:
            return slow1
        
    
        


a =duplicate([1,2,3,4,2,5])
print(a)

