"""divide n conquer

1. select the entore array
2. split the selected array( as evenly as possible)
3. select the left subarray
4.  split the selected array( as evenly as possible)
5. repeat 3,4 until only 1 item will left in subarray
6. an array of 1 item cannot be split so it is ready for compare n  merge"""

def merge_sorted(arr1,arr2):
    """this will compare ang merge two given sotered array into single sorted array"""
    i = j=0
    merged_list =[]

    while i < len(arr1) and j < len(arr2):
        if arr1[i]<arr2[j]:
            merged_list.append(arr1[i])
            i+=1
        else:
            merged_list.append(arr2[j])
            j+=1
    return merged_list


v = merge_sorted([1,2,5],[3,4,7])
print(v)