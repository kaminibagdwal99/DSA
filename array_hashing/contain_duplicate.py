"""
Given an integer array nums, return true if any value appears at least twice in the array, and return 
false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# brute force tc : o(n2) sc : o(1)

def contain_duplicates(arr):
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]==arr[j]:
                return True

    return False
        

nums = [1,2,3,1]
print(contain_duplicates(nums))



# better tc : nlogn sc : o(1)
def contain_duplicatess(arr):
    arr.sort()
    a = arr[0]
    for i in range(1,len(arr)):

        if arr[i]==a:
            return True
        a = arr[i] 

    return False
        

nums = [1,2,3,4]
print(contain_duplicatess(nums))


# optimal tc : o(n) sc : o(n)
def contain_duplicate(arr):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

nums = [1,2,3,1]
print(contain_duplicate(nums))
