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

def linear_2d(arr,item):
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] [j]==item:
                return arr[i][j]

    return -1

arr = [[8, 9] ,[ 6, 3],[9,7] ]
k = 9
print(linear_2d(arr,k))


