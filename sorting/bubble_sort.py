"""tc : o(n^2)    sc : o(1) 
successive passes and largest item goes to back and the smallest one come to first such
as if we throw a stone into water stone will go the bootom while bubble will com eto the upper layer

TC SHOULD BE SEEN AS NO OF COMPARISON IF comparison decrese from o(n2) the it
 is adaptive also the input is sorted arr, buuble sort is not adaptive as no of comaprison are same
 cana bubble sort can be make adaptive
 
 no pf passed item -1 so loop will run for len(arr)-1
 inside loop will be no of pair  """


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print("printing for",{j},arr)


arr = [23, 12, 34, 11, 100, 56, 78]
bubble_sort(arr)


"""adaptive :a sorting alggo falls into adaptive sort category if takes the the advantage of
 existing order in its input"""


"""to make it adaptive we take a flag"""


def bubble_sort_adaptive(arr):
    flag = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 0:
            break

    print(arr)


arr = [23, 12, 34, 11, 100, 56, 78]
bubble_sort_adaptive(arr)


"""for this adaptive algo o(n) tc"""

"""stable : A sorting algo  is said to be stable if 2 objects with equal keys  appear  in the same order
in the sorted output as they appear  in the input array that is to be sorted. 
bubble sort is stable """
