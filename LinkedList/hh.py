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



