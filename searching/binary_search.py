"""
we need a sorted array for binary search.
BS have a sorted array TC : nlogn+logn 
ammortaziation concept for k is very """

def binary(arr, low, high, item):

    if low <=high:
        mid = (low + high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] >item:
            return binary(arr,low,mid-1,item)
        else:
            return binary(arr,mid+1,high,item)
    else:
        return -1

def binary_loop(arr,item):
    low = 0
    high = len(arr)-1

    while low<= high:
        mid= (low+high)//2
        if arr[mid] ==item:
            return mid
        elif arr[mid]>item:
            high = mid-1
        else:
            low = mid+1


arr=[1,2,3,4,6,8,9]
item = 6
print(binary(arr,0,len(arr)-1,item))
print(binary_loop(arr,item))


