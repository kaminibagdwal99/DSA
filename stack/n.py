def next_greater_element(arr):
    res = [-1] * len(arr)
    stack = []

    for i in range(len(arr)-1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            index = stack.pop()
            res[index]= arr[i]
        stack.append(i)
    return res

print(next_greater_element([4,5,2,10,8]))