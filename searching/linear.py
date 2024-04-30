"""
brute force : O(n) tc no sorting required

"""



def linear(arr,item):
    for i in range(len(arr)):
        if arr[i] ==item:
            return i

    return -1

arr = [8, 9 , 6, 3, 0]
k = 0
print(linear(arr,k))


