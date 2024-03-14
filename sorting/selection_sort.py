"""
tc: o(n2)
sc: o(1)

betwenn bs and ss which is faster : selection sort is faster as we have lesser no of  swapping in 
Selection sort 
stable: no
adaptive: not adaptive

benefit :
lesse swapping os it take less time
after each passes there will be confirm sorting
"""

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min]=arr[min],arr[i]
    print(arr)





arr = [23,12,34,11,100,56,78]
selection_sort(arr)
