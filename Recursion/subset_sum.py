def subsetsum(arr, n):
    ans = []
    def subsetsumhelper(index, sum):
        if index ==n:
            ans.append(sum)
            return
        subsetsumhelper(index+1,sum+arr[index])
        subsetsumhelper(index+1,sum)
    subsetsumhelper(0,0)
    ans.sort()
    return ans

arr = [3,1,2]
ans = subsetsum(arr,len(arr))
print(ans)
