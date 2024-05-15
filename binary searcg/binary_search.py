def binary_Search(arr, target):
    low, high = 0 , len(arr)-1

    while low <= high:
        mid = (low+high) //2
        if target == arr[mid]:
            return True
        elif target >arr[mid]:
            low = mid+1
        else:
            high = mid -1

    return -1

arr=[1,5,7,9,12,34]
print(binary_Search(arr, 2))