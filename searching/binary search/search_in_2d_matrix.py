def search_in_2d(arr, target):
    Row, Col = len(arr), len(arr[0])

    top , bottom = 0, Row-1

    while top <= bottom:
        row = (top+bottom)//2
        if target>arr[row][-1]:
            top = row+1
        elif target<arr[row][0]:
            bottom = row-1
        else:
            break

    left, right = 0, Col-1
    row = (top+bottom)//2


    while left <= right:
        mid = (left+right)//2

        if target >arr[row][mid]:
            left = mid+1
        elif target < arr[row][mid]:
            right = mid-1
        else:
            return True
    return False




arr = [[1,2,4],[12,13,21],[23,33,34]]
print(search_in_2d(arr, 4))