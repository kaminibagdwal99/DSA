# 

# def extend_list(val, list1=[]):
#     list1.append(val)
#     return list1

 

 

# list2 = extend_list(10)
# list3 = extend_list(456, [])
# list4 = extend_list('a')

 

# print(list2, list3, list4)


# def palindrome(st):
#     temp = st
#     reverse = 0
#     while (temp >0):
#         digit = temp%10
#         reverse= reverse *10+digit
#         temp = temp//10
#     return st == reverse

    
# print(palindrome(1232))


# aaaabbbbffffaaaiii


# def compress(s):
   
    
#     n = len(s)
#     new_str = ""
#     count=1
#     for i in range(n-1):

#         if s[i]==s[i+1]:
#             count = count+1
#         else:
#             new_str= new_str + s[i]+str(count)
            
#             count = 1
#     new_str= new_str + s[-1]+str(count)
#     return new_str

# s = "aaaabbbbffffaaaiii"
# print(compress(s))



# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if i % 3 ==0 and i %5 ==0:
#             print("frizzbuzz")
#         elif i%3==0:
#             print("frizz")
#         elif i%5==0:
#             print("buzz")
#         else:
#             print(i)
# fizzbuzz(20)


# fibobnacci

# from collections import Counter
# def least_occur(s):
#     si = Counter(s)
#     min_ovvur = min(si.values())
    
#     for k,v in si.items():
#         if v ==min_ovvur:
#             print(k)

# least_occur("ggbhdgshsnnb")



# def minMovesToSeat( seats, students):  
#     print(sorted(seats) )
#     x =  zip(sorted(seats),sorted(students))
#     res = 0
#     for i,j in x:
#         res = res +abs(j-i)
#     return res 

        
# seats = [12,14,19,19,12]
# students=[19,2,17,20,7]              
                


# print(minMovesToSeat(seats,students))


# def minIncrementForUnique( nums):
#     nums.sort()
#     moves =0
#     for i in range(1,len(nums)):
#         if nums[i]<=nums[i-1]:
#             increment = nums[i - 1] + 1 - nums[i]  # Calculate the needed increment
#             nums[i] += increment  # Increment the current element
#             moves += increment  # Add to the tota
#     return moves
                
                


# nums = [1,2,6,6,6]
# print(minIncrementForUnique(nums))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def detectcycle(head):
    slow, fast = head, head
    while fast:
        slow = slow.next

        fast = fast.next.next

        if slow == fast:
            break
    slow1 = head
    while slow:
        slow1 = slow1.next
        slow = slow.next
        if slow == slow1:


            return slow.value


a =Node(1)
b = Node(2)
c = Node(3)
d= Node(4)
a.next = b
b.next = c
c.next = d
d.next = b

print(detectcycle(a))
