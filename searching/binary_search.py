"""BS have a sorted array TC : nlogn+logn ammortaziation concept for k is very """

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


arr=[12,14,16,28,29,31,67]
item = 31
print(binary(arr,0,len(arr)-1,item))