"""
tc: o(n^2)
sc: o(1)

betwenn bs and ss which is faster :selection sort is faster as selectoin sort has lesser
no of swapping in 

Selection sort 
stable: no
adaptive: not adaptive

benefit :
lesse swapping so it take less time
after each passes there will be confirm sorting

passes : n-1
comparison: n(n-1)*2 
swap : n-1
"""
import random
import time

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i], arr[min]=arr[min], arr[i]
    return arr

l=[]
for i in range(10000):
    l.append(random.randint(1,1000))

l1=l[:]

start = time.time()
bubble_sort(l)
print("time taken ", time.time()-start)


start = time.time()
selection_sort(l1)
print("time taken ", time.time()-start)