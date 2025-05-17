def longestConsecutive(nums):
    numset= set(nums)
    longest=0
    for i in numset:
        if (i-1) not in numset:
            length=1
            while (i+length) in numset:
                length +=1
            longest = max(longest, length
                          )
    return longest


print(longestConsecutive(nums = [2,20,4,10,3,4,5]))
