# def binary(arr,target):
#     left = 0
#     right = len(arr)-1

#     while left <=right:
#         mid = (left+right)//2

#         if arr[mid]==target:
#             return True
#         elif arr[mid]<target:
#             left = mid +1
#         else:
#             right = mid -1
#     return -1

# nums = [1,2,4,6,8,9,12]
# # print(binary(nums, 8))

# def search_in_2d(arr,target):
#     Row, Col = len(arr), len(arr[0])
#     top, bottom = 0, Row-1

#     print(top, bottom)

#     while top <=bottom:
#         row = (top+bottom)//2
#         if arr[row][-1] < target:
#             top = row+1
#         elif arr[row][0]> target:
#             bottom=row-1
#         else:
#             break

#     row = (top+bottom)//2

#     left,right = 0, Col-1

#     while left <=right:
#         mid = (left+right)//2
#         if arr[row][mid] == target:
#             return True
#         elif arr[row][mid] < target:
#             left = mid+1
#         else:
#             right = mid-1

#     return -1



# arr = [[1,2,4],[12,13,21],[23,33,34]]
# print(search_in_2d(arr, 4))


for i in range(1,5):
    for j in range(1, i+1):
        print(j, end = "")
    for k in range(i-1,0,-1):
        print(k, end = "")
    print()